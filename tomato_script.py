import numpy as np
import keras
from keras.models import load_model
from keras.preprocessing import image

path_img = "/content/gdrive/My Drive/tomato/test.jpg"	# Exemple de chemin vers image
path_model = '/content/gdrive/My Drive/tomato/tomato_final.h5' 

model = load_model(path_model) # chemin du modÃ¨le Ã  changer


def has_tomatoes(img_path,optimal_threshold=0.07752345):
    img = image.load_img(img_path, target_size=(299, 299))
    img_tensor = image.img_to_array(img) # (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0) 
    img_tensor /= 255.
 
    pred = model.predict(img_tensor)
 
    return True if pred[0][0] > optimal_threshold else False



    if __name__ == '__main__':
    print(has_tomatoes(img_path=path_img))
  