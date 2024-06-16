import subprocess

def download_video(video_url, output_file):
    # Call yt-dlp_x86.exe to download the video
    # process = subprocess.Popen(['yt-dlp_x86.exe', video_url, '-o', output_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process = subprocess.Popen(['R:\Rana Universe\yt-dlp_x86.exe', video_url, '-o', output_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


    # Print the output in real-time
    for line in process.stdout:
        print(line, end='')

    for line in process.stderr:
        print(line, end='')

    process.wait()

    if process.returncode == 0:
        print("Video downloaded successfully.")
    else:
        print(f"Error downloading video: {process.stderr.read()}")

if __name__ == "__main__":
    # Example video URL
    video_url = ""
    video_url = ""
    video_url = "https://www.youtube.com/watch?v=sOZ656_WhG4"
    video_url = "https://www.youtube.com/watch?v=qvSjZ6AKfXQ"

    # Example output file path
    output_file = "5downloaded_video.mp4"

    download_video(video_url, output_file)
