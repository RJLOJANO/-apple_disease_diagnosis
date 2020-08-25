import sys
import os
from tensorflow.python import keras
from tensorflow.python.keras.optimizers import Adam
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras import optimizers
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dropout, Flatten, Dense, Activation
from tensorflow.python.keras.layers import  Convolution2D, MaxPooling2D
from tensorflow.keras.models import load_model
from tensorflow.python.keras import backend as K


K.clear_session()


data_entrenamiento = 'C:/Users/usuario/anaconda3/redneuro/templates/image/dato/entrenamiento'
data_validacion = 'C:/Users/usuario/anaconda3/redneuro/templates/image/dato/validacion'
#C:/Users/usuario/anaconda3/redneuro/templates/image/modelo/
"""
Parameters
"""
epocas=20
longitud, altura = 100, 100
batch_size = 32
pasos = 4000
validation_pasos = 1000
filtrosConv1 = 32
filtrosConv2 = 64
tamano_filtro1 = (3, 3)
tamano_filtro2 = (2, 2)
tamano_pool = (2, 2)
clases = 4


##Preparamos nuestras imagenes

entrenamiento_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

validacion_datagen = ImageDataGenerator(rescale=1. / 255)

imagen_entrenamiento = entrenamiento_datagen.flow_from_directory(
    data_entrenamiento,
    target_size=(altura, longitud),
    batch_size=batch_size,
    class_mode='categorical')

imagen_validacion = validacion_datagen.flow_from_directory(
    data_validacion,
    target_size=(altura, longitud),
    batch_size=batch_size,
    class_mode='categorical')
#red neuronal
cnn = Sequential()
cnn.add(Convolution2D(filtrosConv1, tamano_filtro1, padding ="same", input_shape=(altura, longitud, 3), activation='relu'))
cnn.add(MaxPooling2D(pool_size=tamano_pool))

cnn.add(Convolution2D(filtrosConv2, tamano_filtro2, padding ="same"))
cnn.add(MaxPooling2D(pool_size=tamano_pool))

cnn.add(Flatten())
cnn.add(Dense(256, activation='relu'))
cnn.add(Dropout(0.5))
cnn.add(Dense(clases, activation='softmax'))

cnn.compile(loss='categorical_crossentropy',
 #           optimizer=optimizers.Adam(lr=lr),
           metrics=['accuracy'])
#Scnn.compile(optimizer="",loss=tf.keras.losser.categorical_crossentropy, metrics=['accuracy']) 
cnn.fit(
    imagen_entrenamiento,
    steps_per_epoch=int(pasos/batch_size),
    epochs=epocas,
    validation_data=imagen_validacion,
    validation_steps=int(validation_pasos/batch_size))

target_dir = 'C:/Users/usuario/anaconda3/redneuro/templates/image/modelo/'
if not os.path.exists(target_dir):
  os.mkdir(target_dir)
cnn.save('C:/Users/usuario/anaconda3/redneuro/templates/image/modelo/modelo.h5')
cnn.save_weights('C:/Users/usuario/anaconda3/redneuro/templates/image/modelo/pesos.h5')