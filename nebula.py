import matplotlib.pyplot as plt
import numpy as np
from skimage import measure, io
import skimage.color as color

image = io.imread('Nebula_line.png')

# Определяем, какие пиксели являются зелёными
green_mask = (image[:, :, 0] == 0) & (image[:, :, 1] >= 200) & (image[:, :, 2] == 0)

# Создаём новое изображение по найденным пикселям
green_image = np.zeros_like(image)
green_image[green_mask] = image[green_mask]

# Преобразуем RGBA в Gray
pre_gray_image = color.rgba2rgb(green_image)
gray_image = color.rgb2gray(pre_gray_image)

# Находим контур
contours = measure.find_contours(gray_image, 0.8)

fig, ax = plt.subplots()

# Отображание
image2 = color.gray2rgba(gray_image)
ax.imshow(image2)

# Проводим зелёную линию по контуру
for contour in contours:
    ax.plot(contour[:, 1], contour[:, 0], '.-g')

# Границы
ax.axis('image')

# Удаляем метки на осях
ax.set_xticks([])
ax.set_yticks([])

plt.savefig('Nebula_line_done.png')
