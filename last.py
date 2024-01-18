from tkinter import *
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

steps = 0

def alpha():
    return 0

root = Tk()

icon = PhotoImage(file = r"D:\66f1c9fde9d64b999420808f67b22604_fuse_27552964_0.png")
root.iconphoto(False, icon)

root.title("AI")

root.geometry("300x150")

from PIL import Image
def relu(x): 
    return max(0.0, max(x))
def find_brightest_pixel():
    image = Image.open(r"C:\Users\User\Desktop\фото\1.jpeg")
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
loss_h = []
# Компилируем модель
model.compile(optimizer='adam', loss='mean_squared_error')

step_entry = Entry(root)
step_entry.insert(0, "0")
step_entry.pack()

lbl2 = Label(root, text=f'количество эпох: {alpha()} ')
lbl2.pack()

lbl3 = Label(root, text='результат: NN')
lbl3.pack(anchor=N)

def alpha():
    global lbl2, step_entry, lbl3
    steps = int(step_entry.get())
    lbl2['text'] = f'количество эпох: {steps} '
    for i in range(int(steps)):
        data = np.random.random((10, 1)) * 100
        data_1 = np.max(data, axis = 1)
        a = model.fit(data, data_1, epochs=1)
        loss = model.train_on_batch(data, data_1)
        loss_h.append(loss)
        # Обновляем метку после каждой итерации
        lbl2['text'] = f'количество эпох: {i + 1} '
    data = np.arange(find_brightest_pixel())
    predictions = relu(model.predict(data))
    lbl3['text'] = f'результат: {int(predictions[0])} '
    plt.plot(loss_h)
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Loss over epochs')
    plt.show()

run_button = Button(root, text="Run", command=alpha)
run_button.pack()

root.mainloop()