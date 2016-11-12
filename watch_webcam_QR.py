#!/usr/bin/env python
import zbar

from PIL import Image
import cv2

import time
from subprocess import call
from timeit import default_timer as timer

# argument according to opencv VideoCapture() documentation
# 0 = webcam
CAPTURE_DEVICE = 0

# set TARGET_FPS to give desired CPU load
TARGET_FPS = 10

# Whether to show a visualization of what the webcam is seeing
# red square = no detection, green square = OK detection
SHOW_UI = True

# allowed URI preferences, set to avoid unnecessary calls to mopidy
ALLOWED_URI_PREFIXES = ['spotify']

def main():
    capture = cv2.VideoCapture(CAPTURE_DEVICE)
    current_album = None

    while True:
        # To quit this program press q.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # start timer for measuring FPS
        _start = timer()

        # Breaks down the video into frames
        ret, frame = capture.read()

        # Converts image to grayscale.
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Uses PIL to convert the grayscale image into a numpy ndary array that ZBar can understand.
        image = Image.fromarray(gray)
        width, height = image.size
        zbar_image = zbar.Image(width, height, 'Y800', image.tobytes())

        # Scans the zbar image.
        scanner = zbar.ImageScanner()
        scanner.scan(zbar_image)

        # Check detections for valid QR codes
        found_image = False
        for decoded in zbar_image:
            found_image = True
            if decoded.data and decoded.data.startswith(tuple(ALLOWED_URI_PREFIXES)):
                if decoded.data != current_album:
                    # call mopidy to start playing
                    current_album = decoded.data
                    print("New album: " + decoded.data)
                    call(["nodejs", "mopidy_play.js", current_album])

	# Displays the current frame
        if SHOW_UI:
            rect_color = (0,255,0)
            if not found_image:
                rect_color = (0,0,255)
            cv2.rectangle(frame, (0,0), (20,20), rect_color, 2)
            cv2.imshow('Current', frame)

        # calc FPS and sleep between webcam acq to avoid CPU overload
        _end = timer()
        elapsed_s = (_end - _start)
        current_fps = 1.0 / elapsed_s
        if (current_fps > TARGET_FPS):
          frame_time = 1.0 / TARGET_FPS
          wait_time = frame_time - elapsed_s
          # print("{} > {} -- wait --> {}".format(current_fps, TARGET_FPS, wait_time))
          time.sleep(wait_time)

if __name__ == "__main__":
    main()
