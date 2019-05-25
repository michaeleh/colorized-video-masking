import cv2
import os

# image_folder = '../Mask_RCNN/results/rgb'
image_folder = '../Mask_RCNN/results/bw'
video_name = 'bw_mask.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 30, (width, height))
i = 0
for image in images:
    print(f"{i}/{len(images)}")
    i+=1
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()
