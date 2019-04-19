import numpy as np
from PIL import Image
import click

from deblurgan.model import generator_model
from deblurgan.utils import load_images, deprocess_image,list_image_files,preprocess_image,load_image
import os
import glob
import tqdm
os.environ['CUDA_VISIBLE_DEVICES'] = '1'

idx = 0

def test_and_gen_pic(g,images_A,images_B,batch_size,weight_file):
    global idx
    y_test, x_test = np.array(images_B), np.array(images_A)
    generated_images = g.predict(x=x_test, batch_size=batch_size)
    generated = np.array([deprocess_image(img) for img in generated_images])
    x_test = deprocess_image(x_test)
    y_test = deprocess_image(y_test)
    for i in range(generated_images.shape[0]):
        y = y_test[i, :, :, :]
        x = x_test[i, :, :, :]
        img = generated[i, :, :, :]
        output = np.concatenate((y, x, img), axis=1)
        im = Image.fromarray(output.astype(np.uint8))
        im.save('result/{} results{}.png'.format(os.path.basename(weight_file), idx))
        idx += 1


def test_1(batch_size,weight_file):
    # data = load_images('images/test', batch_size)
    g = generator_model()
    g.load_weights(weight_file)
    # g.load_weights('../generator.h5')
    path='images/test'
    n_images=256
    A_paths, B_paths = os.path.join(path, 'A'), os.path.join(path, 'B')
    all_A_paths, all_B_paths = list_image_files(A_paths), list_image_files(B_paths)
    images_A, images_B = [], []
    for path_A, path_B in zip(all_A_paths, all_B_paths):
        img_A, img_B = load_image(path_A), load_image(path_B)
        images_A.append(preprocess_image(img_A))
        images_B.append(preprocess_image(img_B))
        if len(images_A) > n_images - 1:
            test_and_gen_pic(g,images_A,images_B,batch_size,weight_file)
            images_A.clear()
            images_B.clear()
    test_and_gen_pic(g,images_A, images_B, batch_size,weight_file)
    images_A.clear()
    images_B.clear()


def test(batch_size):
    base_path='weights'
    os.makedirs('result',exist_ok=True)
    files=glob.iglob(os.path.join(base_path,'generator_*.h5'),recursive=True)
    test_1(batch_size, os.path.join(base_path,'generator_29_637.h5'))
    # for weight_file in tqdm.tqdm(files):
    #     test_1(batch_size, weight_file)
    print('ok')

@click.command()
@click.option('--batch_size', default=8, help='Number of images to process')
def test_command(batch_size):
    return test(batch_size)


if __name__ == "__main__":
    test_command()
