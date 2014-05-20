#!/usr/bin/python

from argparse import ArgumentParser
from subprocess import call

def main():
	parser = getInputParser()
	args = parser.parse_args()

	isValid = validateArguments(args)

	if isValid and isPlaylistDownloadRequest(args):
		downloadYoutubePlaylist(args.playlistName, args.url, args.username, args.password)
	elif isValid and isIndividualSongDownloadRequest(args):
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
	parser.add_argument(
		'-n',
		dest='playlistName',
		default=None,
        help="The playlist name [required when downloading playlists]."
	)			

	return parser

def validateArguments(args):
	isValid = True

	if "youtube" not in args.url:
		print "*** Invalid YouTube URL: '" + args.url + "'."
		isValid = False
	elif "playlist" in args.url and (args.username is None or args.password is None or args.playlistName is None):
		print "*** You must specify the playlist name and your YouTube username and password to download a playlist.\n" + "URL: '" + args.url + "'"
		isValid = False

	return isValid

def isPlaylistDownloadRequest(args):
	return "playlist" in args.url

def isIndividualSongDownloadRequest(args):
	return not isPlaylistDownloadRequest(args)

def downloadYoutubeSong(url):	
	''' Function that downloads a video in the MP4 format from YouTube and converts it to MP3.
	'''
	print "Downloading song..."
	call([
		"youtube-dl",
		"--restrict-filenames",							#restrict file names to only ASCII characters, avoiding '&' and spaces in the name
		"-o Downloaded Songs/%(title)s.%(ext)s", 		#output file name and path
		"--format=22/18",								#format of the file
		"--min-filesize=50k",							#minimum file size
		"--no-overwrites",								#specifies no file overwrites during the process
		"--extract-audio",								#extract audio from video
		"--audio-quality=0", 							#best audio quality
		"--audio-format=mp3",							#specifies the audio format to mp3
		url
	])
	print "Process completed."

def downloadYoutubePlaylist(playlistName, url, username, password):
	''' Function that downloads a video in the MP4 format from YouTube and converts it to MP3.
		If the url parameter is a playlist, the whole playlist will be downloaded.
	'''
	print "Downloading playlist..."
	call([
		"youtube-dl",
		"--restrict-filenames",						 	
		"-o Downloaded Playlists/" + playlistName + "/%(title)s.%(ext)s",	
		"--format=22/18",								
		"--min-filesize=50k",						
		"--no-overwrites",							
		"--extract-audio",							
		"--audio-quality=0", 						
		"--audio-format=mp3",							
		"--username=" + username,						#user's YouTube account username to download private playlists
		"--password=" + password,						#user's YouTube account password to download private playlists
		url
	])
	print "Process completed."	

if __name__ == "__main__":
	main()
