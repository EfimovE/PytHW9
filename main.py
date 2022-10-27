from asyncio import streams
from pytube import YouTube
from pytube.exceptions import RegexMatchError

url = input('Введите ссылку на видео Youtube:')
# url = 'https://www.youtube.com/watch?v=7BXJIjfJCsA'

def download_video(url=''):
    try:
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
        my_video.download()
        return 'Video successfully downloaded !'
    # except Exception as _ex:
    except RegexMatchError:
        return 'Upps... Check the URL, please !'

def main ():
    print(download_video(url=url))

if __name__=='__main__':
    main()




