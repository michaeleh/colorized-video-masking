import skimage.io

from Mask_RCNN.api.model_config import config
from Mask_RCNN.api.rcnn import RCNN


class Detector:
    """
    RCNN wrapper
    """

    def __init__(self, name="video"):
        self.rcnn_model = RCNN()
        self.name = name

    def detect_images(self, imgs):
        """
        detect images array and transform to a video. reads images in batches
        :param imgs: images array

        """
        total_len = len(imgs)
        index = 0
        while imgs:
            self.rcnn_model.detect(imgs[:config.BATCH_SIZE])
            del imgs[:config.BATCH_SIZE]
            index += config.BATCH_SIZE
            print(f"detect {index}/{total_len}")

        if self.rcnn_model.frames:
            from Framer.frames2video import to_vid
            to_vid(self.rcnn_model.frames, self.name)


def detect_from_img_paths(self, paths):
    """
    Detect from saved frames
    :param paths: paths of directory of images
    """
    images = []
    for path in paths:
        image = skimage.io.imread(path)
        images.append(image)

    self.detect_images(images)
