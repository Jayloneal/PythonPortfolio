# Install Pytube
# type 'pip install pytube' in Git Bash or 'Windows Terminal once you've opened Python.

from pytube import YouTube

def download_video(url, save_path='.'):
    """Download a video from YouTube.

    Arguments:
    url(str): The URL of the  YouTube video to be downloaded.
    save_path(str): It's the directory path where the video will be saved on the computer. Where will the video go? 
    """
    try:
        # Create a YouTube object with the URL
        yt = YouTube(url)
        
        # Get the highest resolution possible
        video = yt.streams.get_the_highest_resolution()

        # Download the video and audio streams
        video.download(output_path=save_path)
        print(f"{yt.title} has been successfully downloaded.")

    except Exception as e:
        print(f"The video didn't download, my guy! This is the problem: {e}")
    

# Example Usage:
if __name__ == "__main__":
    video_url = input("Drop that YouTube link right here: ")
    download_video(video_url)

# Make sure to update pytube periodically so that it's always current with the changes that the people at YouTube make on the site! 
# Type 'pip install pytube --upgrade' to upgrade it!

