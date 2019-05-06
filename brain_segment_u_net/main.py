from model import *
from data import *

os.environ["CUDA_VISIBLE_DEVICES"] = "0"

data_set='brain'
train_num = 1500*20
test_num = 10
batch_size = 16
epochs=20

data_gen_args = dict(rotation_range=0.2,
                     width_shift_range=0.05,
                     height_shift_range=0.05,
                     shear_range=0.05,
                     zoom_range=0.05,
                     horizontal_flip=True,
                     fill_mode='nearest')
myGene = trainGenerator(batch_size, 'data/{}/train'.format(data_set), 'image', 'label', data_gen_args, save_to_dir=None)
model = unet(lr=1e-4)
model_checkpoint = ModelCheckpoint('checkpoint-{epoch:03d}e.hdf5', monitor='loss', verbose=1, save_best_only=True)
model.fit_generator(myGene, steps_per_epoch=int(train_num / batch_size)+1, epochs=epochs, callbacks=[model_checkpoint])
model.save_weights('unet_{}.hdf5'.format(data_set))
model.load_weights('unet_{}.hdf5'.format(data_set), by_name=True)
testGene = testGenerator("data/{}/test/image".format(data_set))
results = model.predict_generator(testGene, test_num, verbose=1)
saveResult("data/{}/test/pred".format(data_set), results)
