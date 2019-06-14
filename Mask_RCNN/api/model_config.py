import Mask_RCNN.samples.coco.coco as coco


class InferenceConfig(coco.CocoConfig):
    """
     Set batch size to 1 since we'll be running inference on
     one image at a time. Batch size = GPU_COUNT * IMAGES_PER_GPU
     IMAGE_PER_GPU = ( YOUR GPU RAM ) / 6 GB
    """

    GPU_COUNT = 1
    IMAGES_PER_GPU = 1


config = InferenceConfig()
