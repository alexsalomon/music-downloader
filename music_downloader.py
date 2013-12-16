#!/usr/bin/python

from argparse import ArgumentParser
from subprocess import call

def main():
	parser = getInputParser()
	args = parser.parse_args()

	downloadYoutubeSong(args.song_url)

def getInputParser():
	parser = ArgumentParser()
	parser.add_argument(
		"song_url",
		help="The URL of a song to be downloaded.",
	)

	return parser

def downloadYoutubeSong(url):	
	if validateYoutubeURL(url):
		print "Downloading song..."
		call([
			"youtube-dl",
			"--restrict-filenames",
			"-o Downloaded Songs/%(title)s.%(ext)s", #output file name and path
			"--format=22/18",
			"--min-filesize=50k",			
			"--no-overwrites",
			"--no-part",
			"--extract-audio",
			"--audio-quality=0", #best quality
			"--audio-format=mp3",
			url
		])
		print "Song successfully downloaded."
	else:
		print "Invalid URL."

def validateYoutubeURL(url):
	return "youtube" in url

if __name__ == "__main__":
	main()
