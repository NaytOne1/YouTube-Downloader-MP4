from pytube import YouTube

def download_video(url, save_path, resolution):
    try:
        yt = YouTube(url)
        formats = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
        video = formats.filter(res=resolution).first()
        if video:
            video.download(output_path=save_path)
            print("Download completed!")
        else:
            print(f"The resolution {resolution} is not available for this video.")
    except Exception as e:
        print("An error occurred during the download:", str(e))

save_path = input("Specify the path to save the videos: ")

while True:
    url_video = input("Enter the URL of the YouTube video (or type 'exit' to quit): ")
    if url_video.lower() == 'exit':
        break
    resolution = input("Insert the resolution (720p, 480p, etc.): ")
    download_video(url_video, save_path, resolution)
