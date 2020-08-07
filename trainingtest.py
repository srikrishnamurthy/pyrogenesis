from deepforest import deepforest
from deepforest import get_data

test_model = deepforest.deepforest()

# Example run with short training
test_model.config["epochs"] = 1
test_model.config["save-snapshot"] = False
test_model.config["steps"] = 1

#Path to sample file
annotations_file = get_data("testfile_deepforest.csv")
test_model.train(annotations=annotations_file, input_type="fit_generator")

#save trained model
test_model.model.save("pyrogenesis/final_model.h5")
