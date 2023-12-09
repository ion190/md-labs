# Write a program that prints the Sierpinski carpet for the depth `n`, where `n` is an input value.

import matplotlib.pyplot as plt
def draw_carpet(ax, depth, x, y, size):
    if depth == 0:
        ax.add_patch(plt.Rectangle((x, y), size, size, facecolor='black'))
    else:
        smaller_size = size / 3
        for i in range(3):
            for j in range(3):
                if i != 1 or j != 1:
                    draw_carpet(ax, depth - 1, x + i * smaller_size, y + j * smaller_size, smaller_size)

def draw_sierpinski_carpet(depth):
    fig, ax = plt.subplots()
    ax.set_aspect('equal', 'box')
    ax.axis('off')
    draw_carpet(ax, depth, 0, 0, 1)
    plt.show()
depth = int(input("Enter the depth of the Sierpinski carpet: "))
if depth > 0:
    draw_sierpinski_carpet(depth)
