import tensorflow as tf
import numpy as np

# Создаем простую нейросеть
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(1,), dtype=tf.float32),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(1)
])

# Компилируем модель
model.compile(optimizer='adam', loss='mean_squared_error')

# Генерируем случайные данные для обучения
data = np.random.random((100, 1)) * 100
labels = np.max(data, axis=1)

# Обучаем модель
model.fit(data, labels, epochs=1000)

# Генерируем новые данные для предсказания
new_data = np.array([[5], [2], [3], [4]])

predictions = model.predict(new_data)
print(new_data)
print(int(max(predictions)))