import matplotlib.pyplot as plt # used to create a plot to visualize the Sierpinski carpet and save it as an image file
import subprocess # run system commands for opening the generated image file with the default image viewer
import platform # retrieve information about the underlying platform, such as the operating system, version, and architecture


def draw_subcarpet(ax, depth, x, y, size):
    if depth == 0:
        # Draw a filled square at the specified position and size
        ax.add_patch(plt.Rectangle((x, y), size, size, facecolor='black'))
    else:
        # Calculate the size of the smaller squares
        smaller_size = size / 3

        # Recursively draw the 8 smaller carpets
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    # Skip the center square
                    continue
                draw_subcarpet(ax, depth - 1, x + i * smaller_size, y + j * smaller_size, smaller_size)


def draw_full_carpet(depth):
    # Set up the plot
    fig, ax = plt.subplots()
    ax.set_aspect('equal', 'box')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    # Call the recursive function to draw the carpet
    draw_subcarpet(ax, depth, 0, 0, 1)

    # Generate the output filename based on the input depth
    output_filename = f"{depth}_sierpinski_carpet.png"

    # Save the plot as an image file
    plt.savefig(output_filename, bbox_inches='tight', pad_inches=0)
    print(f"Image saved as {output_filename}")

    # Open the image file using the default image viewer
    try:
        system = platform.system().lower()
        if system == "darwin":
            subprocess.run(["open", output_filename])
        elif system == "linux":
            subprocess.run(["xdg-open", output_filename])
        elif system == "windows":
            subprocess.run(["start", "", output_filename], shell=True)
        else:
            print("Unsupported operating system.")
    except Exception as e:
        print(f"Error opening the image file: {e}")



try:
    depth = int(input("Enter the depth of the Sierpinski carpet: "))
    if depth < 0:
        raise ValueError("Depth must be a non-negative integer.")

    draw_full_carpet(depth)
except ValueError as e:
    print(f"Error: {e}")
