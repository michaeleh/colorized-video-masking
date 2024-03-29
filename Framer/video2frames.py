import os

import cv2


def extract_frames(movie_path, max_frames=None, rotate_angle=0, use_grayscale=False):
    """
    From Movie Path return frames
    :param movie_path: movie path
    :param max_frames: max frames to extract, in practice we take MIN(max_frames > accusal frame)
    :param rotate_angle: should we rotate the frame 90,180 or 270 degrees
    :param use_grayscale: transfrom frame to black and white but keep 3 channels!
    :return: list of frames
    """
    if not os.path.exists(movie_path):
        print("Input video file is not found")
        return 1

    # load video
    cap = cv2.VideoCapture()
    cap.open(movie_path)

    if not cap.isOpened():
        print("Failed to open input video")
        return 1

    # get frame count
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)

    # get frame delta jump
    skip_delta = 0
    if max_frames and frame_count > max_frames:
        skip_delta = frame_count / max_frames

    frame_id = 0
    frames = []
    # while we didn't finish getting frames
    while frame_id < frame_count:
        ret, frame = cap.read()
        if not ret:
            print("Failed to get the frame {f}".format(f=frame_id))
        else:
            # Rotate if needed:
            if rotate_angle > 0:
                if rotate_angle == 90:
                    frame = cv2.transpose(frame)
                    frame = cv2.flip(frame, 1)
                elif rotate_angle == 180:
                    frame = cv2.flip(frame, -1)
                elif rotate_angle == 270:
                    frame = cv2.transpose(frame)
                    frame = cv2.flip(frame, 0)

            if use_grayscale:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
            else:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            frames.append(frame)
            print(f"added frame {frame_id}/{frame_count}")
        frame_id += int(1 + skip_delta)
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_id)

    return frames
