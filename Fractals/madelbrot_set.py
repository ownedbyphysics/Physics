import numpy as np
import matplotlib.pyplot as plt

# Canvas size and iteration limits
width, height = 800, 800
max_iter = 256



def mandelbrot(c, max_iter):
    """
    Determines whether a complex number `c` is in the Mandelbrot set.

    The Mandelbrot set is defined by the iterative sequence:
        z_(n+1) = z_n^2 + c, starting with z_0 = 0.

    Parameters:
    - c (complex): The complex number to test.
    - max_iter (int): The maximum number of iterations to test for divergence.

    Returns:
    - int: The number of iterations before divergence.
           If the point does not diverge within `max_iter` iterations, 
           it is assumed to be part of the Mandelbrot set.
    """
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

image = np.zeros((height, width))
# Loop over each pixel in the image
for x in range(width):
    for y in range(height):
        print(x,y)
        real = (x - width / 2) * 4.0 / width
        imag = (y - height / 2) * 4.0 / height
        c = complex(real, imag)

        # Calculate the "escape time" for this point
        color = mandelbrot(c, max_iter)
        image[y, x] = color

        

# Plot the Mandelbrot set
plt.imshow(image, cmap="viridis", extent=(-2, 2, -2, 2))
plt.colorbar()
plt.title("Mandelbrot Set")
plt.xlabel("Re")
plt.ylabel("Im")
plt.show()