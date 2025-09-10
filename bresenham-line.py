import matplotlib.pyplot as plt
def bresenham_line(x0, y0, x1, y1):
    points = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    #шаги
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = 2 * dy - dx
    x, y = x0, y0
    points.append((x, y))

    while x != x1 or y != y1:
        if err >= 0:
            #двигаемся по диагонали (x и y)
            y += sy
            err -= 2 * dx  #e = e + 2*(dy - dx)

        #всегда двигаемся по x
        x += sx
        err += 2 * dy  #e = e + 2*dy
        points.append((x, y))
    return points


def draw_line(points, x0, y0, x1, y1):
    fig, ax = plt.subplots(figsize=(10, 8))

    ax.plot([x0, x1], [y0, y1], 'b--', linewidth=1.5, alpha=0.7) #рисуем линию
    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]
    ax.plot(x_coords, y_coords, 'ro', markersize=6) #рисуем точки брезенхема

    for x, y in points:
        ax.text(x + 0.1, y + 0.1, f'({x},{y})', fontsize=8)

    ax.grid(True, linestyle='--', alpha=0.5) #сетка
    ax.set_aspect('equal')
    margin = 2
    ax.set_xlim(min(x_coords) - margin, max(x_coords) + margin)
    ax.set_ylim(min(y_coords) - margin, max(y_coords) + margin)
    plt.title(f'Линия от ({x0},{y0}) до ({x1},{y1})\nАлгоритм Брезенхема')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.tight_layout()
    plt.show()


def main():
    print("Алгоритм Брезенхема")
    print("=" * 40)
    x0 = int(input("x начальной точки: "))
    y0 = int(input("y начальной точки: "))
    x1 = int(input("x конечной точки: "))
    y1 = int(input("y конечной точки: "))
    points = bresenham_line(x0, y0, x1, y1)
    print(f"\nТочки линии:")
    for i, (x, y) in enumerate(points):
        print(f"{i + 1:2d}. ({x:2d}, {y:2d})")
    draw_line(points, x0, y0, x1, y1)

if __name__ == "__main__":
    main()