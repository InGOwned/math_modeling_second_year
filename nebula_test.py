import matplotlib.pyplot as plt
import numpy as np
from skimage import io
import skimage.color as color


def rotate(A, B, C):
    '''Функция определяет, с какой стороны от вектора AB находится точка C'''
    return (B[0] - A[0]) * (C[1] - B[1]) - (B[1] - A[1]) * (C[0] - B[0])


def grahamscan(A):
    '''Алгоритм Грэхема'''
    n = len(A)  # число точек
    P = list(range(n))  # список номеров точек
    for i in range(1, n):
        if A[P[i]][0] < A[P[0]][0]:  # если P[i]-ая точка лежит левее P[0]-ой точки
            P[i], P[0] = P[0], P[i]  # меняем местами номера этих точек
    for i in range(2, n):  # сортировка
        j = i
        while j > 1 and (rotate(A[P[0]], A[P[j - 1]], A[P[j]]) < 0):
            P[j], P[j - 1] = P[j - 1], P[j]
            j -= 1
    S = [P[0], P[1]]  # стек
    for i in range(2, n):
        while rotate(A[S[-2]], A[S[-1]], A[P[i]]) < 0:
            del S[-1]
        S.append(P[i])
    return S


image = io.imread('Nebula_dotted.png')

# Определяем, какие пиксели являются зелёными
green_mask = (image[:, :, 0] == 0) & (image[:, :, 1] >= 200) & (image[:, :, 2] == 0)

# Создаём новое изображение по найденным пикселям
green_image = np.zeros_like(image)
green_image[green_mask] = image[green_mask]

# Преобразуем RGBA в Gray
pre_gray_image = color.rgba2rgb(green_image)
gray_image = color.rgb2gray(pre_gray_image)

# Находим координаты всех точек, которые являются зелёными
points = np.argwhere(green_mask)

# Применяем алгоритм Грэхема
s = grahamscan(points)

fig, ax = plt.subplots()

# Отображаем изображение
ax.imshow(np.zeros_like(image))

# Соединяем все точки, которые являются зелёными
for i in range(len(s) - 1):
    ax.plot([points[s[i], 1], points[s[i + 1], 1]], [points[s[i], 0], points[s[i + 1], 0]], 'g')
ax.plot([points[s[-1], 1], points[s[0], 1]], [points[s[-1], 0], points[s[0], 0]], 'g')

# Границы
ax.axis('image')

# Удаляем метки на осях
ax.set_xticks([])
ax.set_yticks([])

plt.savefig('Nebula_dotted_done.png')
