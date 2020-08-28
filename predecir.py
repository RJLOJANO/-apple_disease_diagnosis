import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
from setuptools import setup, Extension, Feature
import name 'Feature'
import os
import index
from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
longitud, altura = 100, 100
modelo = 'C:/Users/usuario/anaconda3/redneuro/templates/image/modelo/modelo.h5'
pesos_modelo = 'C:/Users/usuario/anaconda3/redneuro/templates/image/modelo/pesos.h5'
image_path = "C:/Users/usuario/anaconda3/redneuro/"
imgs = os.listdir(image_path)
cnn = load_model(modelo)# cargar nurto modelo  creado 
cnn.load_weights(pesos_modelo)# cargar los pesos de nuetro modelo 

def predict(file):
    x = load_img(file, target_size=(longitud, altura))#carga la imagen 
    x = img_to_array(x)# en arreglo se covierte nustra imagen 
    x = np.expand_dims(x, axis=0)# poder procesar nuert dimencion sin problemas 
    array = cnn.predict(x)# trae arreglo de 2 domensiones [[1,0,0]]
    result = array[0]# nos trae la 1 demencion 
    answer = np.argmax(result)# trae el indice del valor msas alto
    if answer == 0:
        print("pred: costra")
        
    elif answer == 1:
        print("pred: oxido")

    elif answer == 2:
      
        print("pred: saludable")
        
    elif answer == 3:

        print("pred: podrir")


    return answer
