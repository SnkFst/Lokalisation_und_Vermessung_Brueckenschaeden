import os
import imageio

# Path to the MP4 file
video_path = r"D:\Masterarbeit\MonoDacl_230508\11_BrueckeKelheimSaalSt2230Affecking\MavicMini\DCIM\100MEDIA\DJI_0884.MP4"

# Output folder path for the extracted images
output_folder = r"C:\Users\49151\OneDrive\Desktop\Maverik"

# Create the main output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Read the MP4 file
vid = imageio.get_reader(video_path, 'ffmpeg')

# Number of frames to extract per subfolder
frames_per_subfolder = 60

# Calculate the total number of frames in the video
total_frames = len(vid)

# Calculate the number of subfolders needed
num_subfolders = (total_frames + frames_per_subfolder - 1) // frames_per_subfolder

# Extract and save frames in subfolders
frame_counter = 0  # Track the overall frame count

for subfolder_index in range(num_subfolders):
    # Create the subfolder
    subfolder_path = os.path.join(output_folder, f"Subfolder{subfolder_index+1}")
    os.makedirs(subfolder_path, exist_ok=True)
    
    # Extract and save every sixth frame in the subfolder
    for i in range(frames_per_subfolder):
        frame_index = subfolder_index * frames_per_subfolder * 20 + i * 20
        if frame_index >= total_frames:
            break
        
        frame = vid.get_data(frame_index)
        imageio.imwrite(f"{subfolder_path}/{frame_counter}.jpg", frame)
        print(f"Extracted Frame {frame_counter} in Subfolder{subfolder_index+1}")
        frame_counter += 1

# Close the video file
vid.close()

