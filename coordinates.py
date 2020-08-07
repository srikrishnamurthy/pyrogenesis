from deepforest import deepforest
from deepforest import get_data
import pandas as pd
import sys
import os
import time
start_time = time.time()
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

test_model = deepforest.deepforest()
test_model.use_release()

"""--------------------------------------------------------------
Predict test image and return boxes.
Find path to test image. While it lives in deepforest/data,
For non-tutorial images, you do not need the get_data function,
just provide the full path to the data anywhere on your computer.
-----------------------------------------------------------------"""

image_path = get_data("ABBY_064.tif")
boxes = test_model.predict_image(image_path=image_path, show=False, return_plot = False)
print("Computation Time --- %s seconds ---" % (time.time() - start_time))
sys.stdout = open("coordinates.txt", "w")   
print(boxes)
sys.stdout.close()