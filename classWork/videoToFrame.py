import cv2
import os

def split_video_into_frames(video_path, output_folder, num_frames, start_frame_count):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Capture the video
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video {video_path}")
        return start_frame_count

    # Get the total number of frames in the video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_interval = total_frames // num_frames

    frame_count = 0
    saved_frame_count = start_frame_count

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % frame_interval == 0:
            frame_filename = os.path.join(output_folder, f"img_{saved_frame_count:05d}.png")
            cv2.imwrite(frame_filename, frame)
            saved_frame_count += 1

        frame_count += 1

    cap.release()
    print(f"Saved {saved_frame_count - start_frame_count} frames from {video_path} to {output_folder}")
    return saved_frame_count

# Define the path to the video folder and output folder
video_folder = r"C:\Users\sebas\Desktop\Video"
output_folder = r"C:\Users\sebas\Desktop\Video\frames"
num_frames = 10  # Number of frames to extract

# Process each video in the folder
total_saved_frames = 0
for video_file in os.listdir(video_folder):
    if video_file.endswith(('.mp4', '.avi', '.mov')):
        video_path = os.path.join(video_folder, video_file)
        total_saved_frames = split_video_into_frames(video_path, output_folder, num_frames, total_saved_frames)