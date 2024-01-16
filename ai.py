import tensorflow as tf
from PIL import Image
import numpy as np

def relu(x): 
    return max(0.0, max(x))

def find_brightest_pixel(image_path):
    image = Image.open(image_path)
    image = image.convert('L')  # Конвертация в черно-белое изображение
    image = image.resize((1, 1))  # Уменьшение размера до одного пикселя
    pixel_value = image.getpixel((0, 0))  # Получение значения пикселя
    return pixel_value
# Создаем простую нейросеть
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(1,), dtype=tf.float32),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(1)
])
k = 0
# Компилируем модель
model.compile(optimizer='adam', loss='mean_squared_error')\

for i in range(500):
    data = np.random.random((10, 1)) * 100
    data_1 = np.max(data, axis = 1)
    model.fit(data, data_1, epochs=1)
for i in range(500):
    data = np.random.random((10, 1)) * 100
    data_1 = np.max(data, axis = 1)
    model.fit(data, data_1, epochs=1)
    if i % 1000 == 0:
        k+=1
        print(k)
data = np.arange(find_brightest_pixel(r'C:\Users\User\Desktop\фото\2.jpg'))
predictions = model.predict(data)
print((relu(predictions)))