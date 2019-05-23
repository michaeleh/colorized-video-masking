import os

from Framer.video2frames import extract_frames
from Mask_RCNN.api.img_detector import Detector

# from video path
base_dir = "C:/michael/work/Practice/Drone/RGB/"
paths = os.listdir(base_dir)
for movie_path in paths:
    frames = extract_frames(base_dir + movie_path, max_frames=5)
    # mask frames
    detector = Detector()
    detector.detect_images(frames)
