from asyncio import streams
from pytube import YouTube

url = 'https://www.youtube.com/watch?v=7BXJIjfJCsA'
my_video = YouTube(url)

print ('*******Video Title*******')
print (my_video.title)

print ('*******Tumbnail Image*******')
print (my_video.thumbnail_url)

print ('*******Download video*******')

# set stream resolution
my_video = my_video.streams.get_highest_resolution()
# or
# my_video = my_video.streams.first()

# for stream in my_video.streams:
#     print(streams)
my_video.download()



