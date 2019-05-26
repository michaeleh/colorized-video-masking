# -*- coding: utf-8 -*-
# @Author: shubham
# @Date:   2016-12-05 06:11:54
# @Last Modified by:   shubham
# @Last Modified time: 2017-01-07 02:58:39

import tensorflow as tf
from skimage import img_as_ubyte
from skimage.transform import resize


def load_image(img):
    # crop image from center
    short_edge = min(img.shape[:2])
    yy = int((img.shape[0] - short_edge) / 2)
    xx = int((img.shape[1] - short_edge) / 2)
    crop_img = img[yy: yy + short_edge, xx: xx + short_edge]
    # resize to 224, 224
    img = resize(crop_img, (224, 224))
    # desaturate image
    return (img[:, :, 0] + img[:, :, 1] + img[:, :, 2]) / 3.0


# return img

def model():
    with open("Colorize/model/colorize.tfmodel", mode='rb') as f:
        model = f.read()
    return model


def recolor(imgs):
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(model())
    grayscale = tf.placeholder(tf.float32, [1, 224, 224, 1])
    inferred_rgb, = tf.import_graph_def(graph_def,
                                        input_map={"grayscale": grayscale},
                                        return_elements=["inferred_rgb:0"])
    recolored = []
    with tf.Session() as sess:
        for img in imgs:
            in_img = load_image(img)
            input_vector = in_img.reshape(1, 224, 224, 1)
            inferred_batch = sess.run(inferred_rgb, feed_dict={grayscale: input_vector})

            out_img = img_as_ubyte(inferred_batch[0])
            recolored.append(out_img)

    return recolored
