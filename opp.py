# Installing pytube first:
# pip install pytube

from pytube import YouTube

# Download YouTube video function
def download_video(url):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download()
    print(f"Downloaded: {yt.title}")

# Example usage
download_video('https://www.youtube.com/watch?v=example_video')
