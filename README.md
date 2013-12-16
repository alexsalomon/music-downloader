Music Downloader
================

Application that downloads songs from YouTube given a video URL.
Tested only on Mac OS X 10.8.5.

Set up
------

Mac OS X:

If you don't have Homebrew installed, visit the http://brew.sh/ for instructions.

```
sudo pip install --upgrade youtube_dl
brew install ffmpeg
chmod u+x music_downloader.py
```

Downloading Songs:
------------------

You can download a song from YouTube by providing the script with a URL of a video containing the song:

```
./music_downloader.py "http://www.youtube.com/watch?v=r0a-o16i_Gw"
```
