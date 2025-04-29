##CHECK FOR DEPENDENCIES (pip, yt-dlp, ffmpeg, ffprobe)
import subprocess

# Switches to Desktop directory.
subprocess.run("cd \"C:/Users/Cody/Desktop\"", shell=True)
print("YOUTUBE MP3 EXTRACTOR\n")

while True:
	print("URL: ")
	url = input()
	print("\nLet's do this!\n--------------")

	# Downloads best audio format from URL, then converts it to mp3.
	subprocess.run(f'yt-dlp --no-playlist -f "ba" --extract-audio --audio-format mp3 "{url}"', shell=True)
	print("--------------\nDownload Complete!\n")
