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
# print (my_video.thumbnail_url)
# for stream in my_video.streams:
#     print(streams)
my_video.download()




# import requests

# video_url = 'https://youtu.be/gvYGIhuiJQI'
# def download_video(url=''):
#     try:
#         # response = requests.get(url=url)
#         # with open ('req_video.jpg', 'wb') as file:
#         #     file.write(response.content)
#         # return 'Video successfully downloaded !'
#         response = requests.get(url=url, stream=True)
#         with open ('req_video.mp4', 'wb') as file:
#             for chunk in response.iter_content(chunk_size=1024*1024):
#                 if chunk:
#                     file.write(chunk)
#         return 'Video successfully downloaded !'

#     except Exception as _ex:
#         return 'Upps... Check the URL, please !'

# def main ():
#     print(download_video(url=video_url))

# if __name__=='__main__':
#     main()