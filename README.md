# Object Masking in a ( RGB, B&W and recolorized )Video

## the pipeline:
1. extract frames from the video
2. convert them to black and white [optional]
3. recolor the frames using transfer learning on VGG16
4. run object masking with Mask RCNN
5. collect the frames to a video

## How to use
1. model.py -- the main. specify the models to use. run it with video path as an argument
'''
python model.py ./myVideo.mp4
'''
2. Colorize -- directory for recolor black and white models
3. Framer -- directory to convert frames to video and vice versa
4. Mask_RCNN -- directory to
5. requirements.txt -- requirement for this project.
    NOTE: some requirement can't be installed with pip alone. there are comments in this file read them!
