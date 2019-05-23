from Framer.video2frames import extract_frames
from Mask_RCNN.api.img_detector import Detector
# from video path
movie_path = "C:/michael/work/Practice/Drone/RGB/jog.mp4"
frames = extract_frames(movie_path, max_frames=20)

# mask frames
detector = Detector()
detector.detect_images(frames)


