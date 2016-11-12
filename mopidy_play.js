#!/usr/bin/env nodejs

/*
 * mopdiy_play.js -- play an URI in mopidy
 */

var mopidy_host = "localhost:6680"

var args = process.argv.slice(2);
if (args.length < 1) {
  console.log("usage: mopidy_play.js <uri>");
  process.exit(1);
}

// e.g, spotify:album:321LzecEFfm8HJ1dzyYted
var spotify_uri = args[0];

var Mopidy = require('mopidy');
var mopidy = new Mopidy({webSocketUrl: 'ws://' + mopidy_host + '/mopidy/ws/',
                         callingConvention: 'by-position-or-by-name',
                         autoConnect: true
                        });

function play_spotify(uri) {
  mopidy.tracklist.clear().then(function () {
    mopidy.tracklist.add({uri: uri}).then(function () {
      mopidy.playback.play();
      process.exit(0);
    }, function(err) {
      process.exit(1);
    })
  });
}

console.log("playing: " + spotify_uri);

mopidy.on("state:online", function () {
  play_spotify(spotify_uri);
});

console.log("end");
