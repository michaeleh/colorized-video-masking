from Mask_RCNN.api.rcnn import RCNN
import os
import time

rcnn_model = RCNN()


def get_img_default_():
    # Root directory of the project
    root_dir = os.path.abspath("../")
    # Directory of images to run detection on
    image_dir = os.path.join(root_dir, "images/")
    return image_dir


img_dir = get_img_default_()
imgs = os.listdir(img_dir)
imgs = [img_dir + img for img in imgs]

img_index = 1

for img in imgs:
    start_time = int(round(time.time() * 1000))
    rcnn_model.detect_and_save(img)
    end_time = int(round(time.time() * 1000))
    print(f"Finished {img_index}/{len(imgs)} at {end_time - start_time}")
    img_index += 1
