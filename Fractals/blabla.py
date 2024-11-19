import numpy as np
import matplotlib.pyplot as plt

# Define image size and iteration limits
width, height = 800, 800
max_iter = 256

# Create a function to calculate the Mandelbrot set
def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

# Create an empty image and fill it
image = np.zeros((height, width))
for x in range(width):
    for y in range(height):
        print(x,y)
        # Scale pixel coordinates to the complex plane
        real = (x - width / 2) * 4.0 / width
        imag = (y - height / 2) * 4.0 / height
        c = complex(real, imag)
        # Apply Mandelbrot function to each point
        color = mandelbrot(c, max_iter)
        image[y, x] = color

# Plot the Mandelbrot set
plt.imshow(image, cmap="magma", extent=(-2, 2, -2, 2))
plt.colorbar()
plt.title("Mandelbrot Set")
plt.xlabel("Re")
plt.ylabel("Im")
plt.show()
