import os

from Colorize import colorize
from Framer.video2frames import extract_frames
from Mask_RCNN.api.img_detector import Detector


class Model:
    def __init__(self, detector) -> None:
        self.detector = detector
        self.max_frames = None

    def run(self):
        pass


class RgbModel(Model):
    def run(self):
        frames = extract_frames(movie_path, max_frames=self.max_frames)
        self.detector.detect_images(frames)


class BnWModel(Model):
    def run(self):
        frames = extract_frames(movie_path, max_frames=self.max_frames, use_grayscale=True)
        self.detector.detect_images(frames)


class RecolorModel(Model):
    def run(self):
        frames = extract_frames(movie_path, max_frames=self.max_frames, use_grayscale=True)
        frames = colorize.recolor(frames)
        self.detector.detect_images(frames)


if __name__ == '__main__':
    # from video path
    movie_path = "./Drone/drone.mp4"
    detector = Detector()
    models = [RgbModel(detector), BnWModel(detector), RecolorModel(detector)]
    for model in models:
        model.run()
