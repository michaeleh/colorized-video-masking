import os
import sys

import Mask_RCNN.mrcnn.model as modellib
from Mask_RCNN.api.class_config import class_names
from Mask_RCNN.api.model_config import config
from Mask_RCNN.mrcnn import utils
from Mask_RCNN.mrcnn import visualize

"""

INIT MODEL CONFIGS AND LOAD TO MEMORY

"""


class RCNN:

    def __init__(self) -> None:
        # Root directory of the project
        root_dir = os.path.abspath("./Mask_RCNN")
        # Import Mask RCNN
        sys.path.append(root_dir)  # To find local version of the library
        # Import COCO config
        sys.path.append(os.path.join(root_dir, "samples/coco/"))  # To find local version
        # Directory to save logs and trained model
        model_dir = os.path.join(root_dir, "logs")
        # Local path to trained weights file
        coco_model_path = os.path.join(root_dir, "mask_rcnn_coco.h5")
        # Download COCO trained weights from Releases if needed
        if not os.path.exists(coco_model_path):
            utils.download_trained_weights(coco_model_path)

        # Create model object in inference mode.
        self.model = modellib.MaskRCNN(mode="inference", model_dir=model_dir, config=config)
        # Load weights trained on MS-COCO
        self.model.load_weights(coco_model_path, by_name=True)

    def detect_and_save(self, images):
        results = self.model.detect(images, verbose=0)
        # Visualize results
        for img in images:
            r = results.pop()
            visualize.display_instances(img, r['rois'], r['masks'], r['class_ids'],
                                        class_names, r['scores'])
