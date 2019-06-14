import os

import cv2


def to_vid(frames, video_name):
    """
    Transform Frames to avi video
    :param frames: array of frames
    :param video_name: video name to save to video
    """
    video_name += '.avi'
    height, width, layers = frames[0].shape
    # 30 fps
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video = cv2.VideoWriter(video_name, fourcc, 30, (width, height))
    i = 0
    for frame in frames:
        frame = cv2.resize(frame, (width,height))
        print(f"{i}/{len(frames)}")
        i += 1
        video.write(frame)
    cv2.destroyAllWindows()
    video.release()


def to_vid_from_dir(dir_name):
    """
    Transform from a folder that contains the frames saved as png
    then read all the png to framed and call above method
    :param dir_name: storing the frames as png
    """
    image_folder = f'../Mask_RCNN/results/{dir_name}'

    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    frames = [cv2.imread(os.path.join(image_folder, image)) for image in images]
    to_vid(frames, dir_name)


