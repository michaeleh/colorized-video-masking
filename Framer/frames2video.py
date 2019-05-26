import os

import cv2

def to_vid(dir_name):
    image_folder = f'../Mask_RCNN/results/{dir_name}'
    video_name = f'{dir_name}.avi'

    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape
    # 30 fps
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video = cv2.VideoWriter(video_name, fourcc, 30, (width, height))
    i = 0
    for image in images:
        print(f"{i}/{len(images)}")
        i += 1
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()

to_vid("recolor")
to_vid("rgb")
to_vid("bw")