import matplotlib.pyplot as plt
import numpy as np
#a,b = map(int, input().split())
a=1
b =2
def circle_plotter(a,b):
    
    x = np.arange(-a**2, a**2, 0.1)
    y = np.arange(-b**2, b**2, 0.1)
 
    # Переход к неявнозаданным координатам
    X, Y = np.meshgrid(x, y)
 
    fxy = (X**2/a**2 + Y**2/b**2) - 1
 
    # Команда рисования
    plt.contour(X, Y, fxy, levels=[0])
    plt.savefig('pic_3.png')
    
if __name__ == '__main__':
	circle_plotter(a,b)
 