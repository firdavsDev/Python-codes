from pytube import YouTube

link=input("link ")
video=YouTube(link)
stream=video.streams.get_highest_resolution()
stream.download()
