# qr-card-music

Hardware-based user interface for music.

Uses two-sided cards -- one with album art, back with QR codes, to control your music player (mopidy or spotify).

## Demo

Demo video from 2016: https://ixd.ai/musiccard .. an update is due soon =)

## History

- 2012 :: initial concept inspired by RFID/NFC-based cards
- 2016 :: first public implementation using QR cards
- 2018 :: shareable, ready-for-public-beta implementation

## Similar projects

- https://github.com/mattvenn/qr-music-player .. very similar project, was unaware of this until 181128

## Prerequisites

  * nodejs
  * python
    * pyzbar
    * PIP
    * opencv2

## Installation

TODO: Writeme

## Usage

TODO: Writeme


# Unfinished Docs/Notes

## MQTT installation

good notes: https://github.com/suiluj/pi-adhoc-mqtt-cluster/wiki/VerneMQ

## manual install

```
sudo apt install erlang

`vernemq console`
```

## docker

docker run -e "DOCKER_VERNEMQ_ALLOW_ANONYMOUS=on" -p 1883:1883 --name vernemq1 erlio/docker-vernemq


pip install paho-mqtt

## test 
mosquitto_pub -h localhost -p 1883 -t musiccard/detection -m spotify:album:321LzecEFfm8HJ1dzyYted
