from model import *
from data import *

# os.environ["CUDA_VISIBLE_DEVICES"] = "1"

data_set='brain'
train_num = 1500
test_num = 10
batch_size = 1
epochs=10

data_gen_args = dict(rotation_range=0.2,
                     width_shift_range=0.05,
                     height_shift_range=0.05,
                     shear_range=0.05,
                     zoom_range=0.05,
                     horizontal_flip=True,
                     fill_mode='nearest')
model = unet(lr=1e-3)
model.load_weights('checkpoint-020e_e_l.hdf5', by_name=True)
testGene = testGenerator("data/{}/test/image".format(data_set))
results = model.predict_generator(testGene, test_num, verbose=1)
saveResult("data/{}/test/pred".format(data_set), results)
