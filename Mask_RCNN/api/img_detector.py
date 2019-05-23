import skimage.io

from Mask_RCNN.api.model_config import config
from Mask_RCNN.api.rcnn import RCNN


class Detector:

    def __init__(self):
        self.rcnn_model = RCNN()

    def detect_images(self, imgs):
        while imgs:
            self.rcnn_model.detect_and_save(imgs[:config.BATCH_SIZE])
            del imgs[:config.BATCH_SIZE]

    def detect_from_img_paths(self, paths):
        images = []
        for path in paths:
            image = skimage.io.imread(path)
            images.append(image)

        self.detect_images(images)
