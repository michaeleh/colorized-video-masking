# Object Masking in a ( RGB, B&W and recolorized) Video

## The Pipeline:
* using tensorflow framework and opencv for video manipulations and Python 3.6.8
1. extract frames from the video
2. convert them to black and white [optional]
3. recolor the frames using transfer learning on VGG16 [optional]
4. run object masking with Mask RCNN
5. collect the frames to a video

<img src="https://i.imgur.com/w0rgKV9.png"/>

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
[] better model for colorization, as vgg16 accept low resolution images
[] faster detection algorithm to support live stection, maybe mot masking only detection
[] improve preformance without scaling the GPU
[] run model on a live video with minimal latency
[] ???

## Demo
for this demo i only wanted to look for:
* person, bicycle, car, motorcycle, bus, train, truck, traffic light, stop sign
* you can have much more <a href="https://github.com/michaeleh/colorized-video-masking/blob/master/Mask_RCNN/api/class_config.py">labels<a/>
    
### RGB
<img src="https://media.giphy.com/media/fUGxDnnnMGBVbzjkwM/giphy.gif"/>

### Black and White
<img src="https://media.giphy.com/media/JO3wCbZ0JkjhLjwca2/giphy.gif"/>

## Recolored
<img src="https://media.giphy.com/media/lSfwCGI8YSCPfFauEb/giphy.gif"/>
    
    
## Thank You
1. <a href="https://github.com/matterport/Mask_RCNN">Mask RCNN model</a>
2. <a href="https://github.com/sksq96/cnn-colorize">Colorize Model</a>
3. <a href="https://youtu.be/f7TLW6qeX4M">Video for demo (0:25 ~ 0:35)</a>
