import matplotlib.pyplot as plt
from deepforest import deepforest
from deepforest import get_data
import time
start_time = time.time()

test_model = deepforest.deepforest()
test_model.use_release()

#predict image
image_path = get_data("ABBY_064.tif")
image = test_model.predict_image(image_path = image_path)

#Show image, matplotlib expects RGB channel order, but keras-retinanet predicts in BGR
plt.imshow(image[...,::-1])
print("Computation Time --- %s seconds ---" % (time.time() - start_time))
plt.show()
