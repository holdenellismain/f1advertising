import yt_dlp
import cv2
import os

# Download video
# make sure url does not include &list
video_url = "https://www.youtube.com/watch?v=YSFtvjLPwMA"
output_filename = "downloaded_video.mp4"
# number of frames to sample per second
per_second = 0.5
ydl_opts = {
    'format': 'best[ext=mp4]',
    'outtmpl': output_filename,
}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

print(f"Downloaded video saved as {output_filename}")

# Extract frames to a folder
frames_folder = "frames"
os.makedirs(frames_folder, exist_ok=True)

cap = cv2.VideoCapture(output_filename)

fps = cap.get(cv2.CAP_PROP_FPS)
frame_interval = int(int(fps) / per_second)

frame_count = 0
saved_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    if frame_count % frame_interval == 0:
        frame_filename = os.path.join(frames_folder, f"frame_{saved_count:04d}.jpg")
        cv2.imwrite(frame_filename, frame)
        print(f"Saved {frame_filename}")
        saved_count += 1
    frame_count += 1

cap.release()
print(f"Done. {saved_count} frames saved in folder '{frames_folder}'")
