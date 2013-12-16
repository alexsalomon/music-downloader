#!/usr/bin/python

from argparse import ArgumentParser
from subprocess import call

def main():
	parser = getInputParser()
	args = parser.parse_args()

	if validateArguments(args):
		downloadYoutubeSongs(args.url)

def getInputParser():
	parser = ArgumentParser()
	parser.add_argument(
		"url",
		help="The URL of a song or a playlist on YouTube to be downloaded.",
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

def downloadYoutubeSongs(url):	
	''' Function that downloads a video in the MP4 format from YouTube and converts it to MP3.
	The url parameter can be an URL for a single video or a public playlist.
	In the case of a playlist, the whole playlist will be downloaded. 
	'''
	print "Downloading song..."
	call([
		"youtube-dl",
		"--restrict-filenames",
		"-o Downloaded Songs/%(title)s.%(ext)s", #output file name and path
		"--format=22/18",
		"--min-filesize=50k",			
		"--no-overwrites",
		"--extract-audio",
		"--audio-quality=0", #best quality
		"--audio-format=mp3",
		url
	])
	print "Song successfully downloaded."

def validateArguments(args):
	isValid = True

	if "youtube" not in args.url:
		print "*** You must insert a valid YouTube URL."
		isValid = False
	elif "playlist" in args.url and (args.username is None or args.password is None):
		print "*** You must specify your YouTube username and password to download a playlist."
		isValid = False

	return isValid

if __name__ == "__main__":
	main()
