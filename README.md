# Object Masking in a ( RGB, B&W and recolorized) Video

## the pipeline:
* using tensorflow framework and opencv for video manipulations
1. extract frames from the video
2. convert them to black and white [optional]
3. recolor the frames using transfer learning on VGG16
4. run object masking with Mask RCNN
5. collect the frames to a video

## How To Use
1. model.py -- the main. specify the models to use. run it with video path as an argument
```
python model.py ./myVideo.mp4
```

2. Colorize -- directory for recolor black and white models
3. Framer -- directory to convert frames to video and vice versa
4. Mask_RCNN -- directory of Mask RCNN model and code
5. requirements.txt -- requirement for this project.
    NOTE: some requirement can't be installed with pip alone. there are comments in this file read them!

## Futue Work and How You Can Contribute!
[] improve preformance without scaling the GPU
[] run model on a live video with minimal latency
[] ???

## Demo
coming soon

## Thank You
1. <a href="https://github.com/matterport/Mask_RCNN">Mask RCNN model</a>
2. <a href="https://github.com/sksq96/cnn-colorize">Colorize Model</a>
