import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
import os
import sys
longitud, altura = 100, 100
modelo = 'C:/Users/usuario/anaconda3/redneuro/templates/image/modelo/modelo.h5'
pesos_modelo = 'C:/Users/usuario/anaconda3/redneuro/templates/image/modelo/pesos.h5'
cnn = load_model(modelo)
cnn.load_weights(pesos_modelo)

def clasificar(file):
    x = load_img(file, target_size=(longitud, altura))#carga la imagen 
    x = img_to_array(x)# en arreglo se covierte nustra imagen 
    x = np.expand_dims(x, axis=0)# poder procesar nuert dimencion sin problemas 
    array = cnn.predict(x)# trae arreglo de 2 domensiones [[1,0,0]]
    result = array[0]# nos trae la 1 demencion 
    answer = np.argmax(result)# trae el indice del valor msas alto
    if answer == 0:
        print("pred: unaen")
        
    elif answer == 1:
        print("pred: dosen")

    elif answer == 2:
      
        print("pred: tresen")
        
    elif answer == 3:

        print("pred: buena")


    return answer

