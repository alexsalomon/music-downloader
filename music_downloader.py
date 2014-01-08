#!/usr/bin/python

from argparse import ArgumentParser
from subprocess import call

def main():
	parser = getInputParser()
	args = parser.parse_args()

	if validateYouTubeURL(args.url, args.username, args.password):
		downloadYoutubeSongs(args.url)

def getInputParser():
	parser = ArgumentParser()
	parser.add_argument(
		"url",
		help="The URL of a song or a playlist on YouTube to be downloaded, or a path to a file containing multiple URLs.",
	)
	parser.add_argument(
		'-u',
		dest='username',
		default=None,
        help="The user's YouTube username [required when downloading playlists]."
	)
	parser.add_argument(
		'-p',
		dest='password',
		default=None,
        help="The user's YouTube password [required when downloading playlists]."
	)		

	return parser

def validateYouTubeURL(url, username, password):
	isValid = True

	if "youtube" not in url:
		print "*** Invalid YouTube URL: '" + url + "'."
		isValid = False
	elif "playlist" in url and (username is None or password is None):
		print "*** You must specify your YouTube username and password to download a playlist.\n" + "URL: '" + url + "'"
		isValid = False

	return isValid

def downloadYoutubeSongs(url):	
	''' Function that downloads a video in the MP4 format from YouTube and converts it to MP3.
	The url parameter can be an URL for a single video or a playlist.
	In the case of a playlist, the whole playlist will be downloaded. 
	'''
	print "Downloading song..."
	call([
		"youtube-dl",
		"--restrict-filenames",						#restrict file names to only ASCII characters, avoiding '&' and spaces in the name
		"-o Downloaded Songs/%(title)s.%(ext)s", 	#output file name and path
		"--format=22/18",							#format of the file
		"--min-filesize=50k",						#minimum file size
		"--no-overwrites",							#specifies no file overwrites during the process
		"--extract-audio",							#extract audio from video
		"--audio-quality=0", 						#best audio quality
		"--audio-format=mp3",						#specifies the audio format to mp3
		url
	])
	print "Process completed."

if __name__ == "__main__":
	main()
