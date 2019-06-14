import sys
from Colorize import colorize
from Framer.video2frames import extract_frames
from Mask_RCNN.api.img_detector import Detector


class Model:
    """
    Abstract model
    """
    def __init__(self, detector) -> None:
        self.detector = detector
        self.max_frames = None

    def run(self):
        pass


class RgbModel(Model):
    """
    RGB impl
    """
    def run(self):
        frames = extract_frames(movie_path, max_frames=self.max_frames)
        self.detector.detect_images(frames)


class BnWModel(Model):
    """
    Black and White impl
    """
    def run(self):
        frames = extract_frames(movie_path, max_frames=self.max_frames, use_grayscale=True)
        self.detector.detect_images(frames)


class RecolorModel(Model):
    """
    Recolor impl
    """
    def run(self):
        frames = extract_frames(movie_path, max_frames=self.max_frames, use_grayscale=True)
        frames = colorize.recolor(frames)
        self.detector.detect_images(frames)


if __name__ == '__main__':
    # from video path
    movie_path = sys.argv[1]
    # models to use
    models = [RgbModel(Detector('rgb')), BnWModel(Detector('b_w')), RecolorModel(Detector('recolor'))]
    for model in models:
        model.run()
