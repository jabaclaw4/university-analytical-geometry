import numpy as np
import matplotlib.pyplot as plt
import time

def flood_fill_with_visual(image, x, y, target_color, new_color, delay=0.3):
    #рекурсивный алгоритм
    height, width = image.shape[:2] #берем только ширину и высоту
    if x < 0 or x >= width or y < 0 or y >= height:
        return
    current_color = image[y, x] #получаем цвет
    if not np.array_equal(current_color, target_color) or np.array_equal(current_color, new_color): #если текущий цвет не равен целевому
        return #если текущий цвет уже равен новому цвету
    image[y, x] = new_color

    #визуализация
    plt.imshow(image)
    plt.axis('off')
    plt.draw()
    plt.pause(delay)
    #рекурсия
    flood_fill_with_visual(image, x + 1, y, target_color, new_color, delay)
    flood_fill_with_visual(image, x - 1, y, target_color, new_color, delay)
    flood_fill_with_visual(image, x, y + 1, target_color, new_color, delay)
    flood_fill_with_visual(image, x, y - 1, target_color, new_color, delay)
def create_figure(): #создаем квадрат с границами (сначала фул блэк, потом внутри маленький белый)
    img = np.zeros((8, 8, 3), dtype=np.uint8)
    img[:, :] = [0, 0, 0]
    img[2:6, 2:6] = [255, 255, 255]
    return img
def main():
    img = create_figure()
    print("Исходное изображение:")
    plt.figure(figsize=(5, 5))
    plt.imshow(img)
    plt.title("Исходное изображение")
    plt.axis('off')
    plt.show()
    #ждем перед началом заливки
    time.sleep(1)
    #создаем новое окно для анимации заливки
    print("Начинаем заливку...")
    plt.figure(figsize=(5, 5))
    #параметры заливки
    flood_fill_with_visual(img, 4, 4, np.array([255, 255, 255]), np.array([255, 0, 0]), 0.2)
    print("Заливка завершена!")
    plt.figure(figsize=(5, 5))
    plt.imshow(img)
    plt.title("Финальный результат")
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    main()
