# Object Masking in a ( RGB, B&W and recolorized )Video

## the pipeline:
1. extract frames from the video
2. convert them to black and white [optional]
3. recolor the frames using transfer learning on VGG16
4. run object masking with Mask RCNN
5. collect the frames to a video



