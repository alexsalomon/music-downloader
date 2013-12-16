Music Downloader
================

Application that downloads songs from YouTube given a video or playlist  URL.\n
In the case of a playlist, all the songs will be downloaded.\n
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

You can download a song from YouTube by providing an URL of a video containing the song:
```
./music_downloader.py "http://www.youtube.com/watch?v=r0a-o16i_Gw"
```

You can also download all the songs on a playlist by providing the playlist URL with your YouTube username and password:
```
./music_downloader.py -u myusername@gmail.com -p mypassword123 "http://www.youtube.com/playlist?list=PLLMgg-xBAzEwEIDofx_nGPApLDIL5IkUx"
```
