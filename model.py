import os

from Framer.video2frames import extract_frames
from Mask_RCNN.api.img_detector import Detector

# from video path
base_dir = "./Drone/RGB/"
paths = os.listdir(base_dir)
for movie_path in paths:
    # mask frames
    detector = Detector()
    frames = extract_frames(base_dir + movie_path, max_frames=10, use_grayscale=False)
    detector.detect_images(frames)
    frames = extract_frames(base_dir + movie_path, max_frames=10, use_grayscale=True)
    detector.detect_images(frames)
