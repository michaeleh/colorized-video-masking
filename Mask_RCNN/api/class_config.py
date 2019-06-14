from Mask_RCNN.mrcnn.visualize import random_colors

# COCO Class names
# Index of the class in the list is its ID. For example, to get ID of
# the teddy bear class, use: class_names.index('teddy bear')
class_names = ['BG', 'person', 'bicycle', 'car', 'motorcycle', 'airplane',
               'bus', 'train', 'truck', 'boat', 'traffic light',
               'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird',
               'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear',
               'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie',
               'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
               'kite', 'baseball bat', 'baseball glove', 'skateboard',
               'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup',
               'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
               'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
               'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed',
               'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote',
               'keyboard', 'cell phone', 'microwave', 'oven', 'toaster',
               'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors',
               'teddy bear', 'hair drier', 'toothbrush']


def init_labels_color():
    """
    get only the labels you want, you can group labels such as each GROUP gets a different color.
    you can group labels to the same color --- labels = ['person',['car','bus'],['hair drier','teddy bear']]
    :return: label to color dictionary
    """
    color_labels_dict = {}

    labels = [['person', 'bicycle'], ['car', 'motorcycle',
                                      'bus', 'train', 'truck'], ['traffic light',
                                                                 'stop sign']]
    colors = random_colors(len(labels))

    for index in range(0, len(labels)):

        label = labels[index]
        if isinstance(label, list):
            for l in label:
                color_labels_dict[l] = colors[index]
        else:
            color_labels_dict[label] = colors[index]

    return color_labels_dict


color_labels = init_labels_color()
