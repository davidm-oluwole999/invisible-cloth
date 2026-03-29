

import cv2
import os

images = []
def create_video_from_images(folder_path, output_name='output.avi', fps=2):
    global images
    # Loop through files in the folder
    for filename in os.listdir(folder_path):
        img_path = os.path.join(folder_path, filename)
        img = cv2.imread(img_path)

        if img is not None:
            # Step 1: Resize to 400 x 300
            resized_img = cv2.resize(img, (400, 300))
            images.append(resized_img)

    if not images:
        print("No valid images found.")
        return
create_video_from_images('C:\\Users\\funmi\\Downloads\\Python\\OpenCV\\images')
# Step 2: Initialize Video Writer
# 'XVID' is a common codec for .avi files
fourcc = cv2.VideoWriter_fourcc(*'XVID')
video = cv2.VideoWriter('output_name', fourcc, 20, (400, 300))

# Step 3: Write frames to video
for frame in images:
    video.write(frame)

video.release()
print(f"Video saved as {'output_name'}")

# Usage:

