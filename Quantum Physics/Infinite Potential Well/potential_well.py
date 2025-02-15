import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh_tridiagonal

# Define parameters
L = 1.0  # Length of the potential well
N = 500  # Number of grid points
x = np.linspace(0, L, N)  # Position grid
dx = x[1] - x[0]  # Grid spacing

# Create the Hamiltonian matrix using finite differences
diagonal = np.full(N, 2.0)  # Main diagonal (2/h^2 term)
off_diagonal = np.full(N - 1, -1.0)  # Off-diagonals (-1/h^2 term)
H = np.diag(diagonal) + np.diag(off_diagonal, k=1) + np.diag(off_diagonal, k=-1)

# Solve for eigenvalues (energies) and eigenvectors (wavefunctions)
eigenvalues, eigenvectors = eigh_tridiagonal(diagonal, off_diagonal)

# Normalize wavefunctions
wavefunctions = eigenvectors / np.sqrt(dx)

# Plot the first three wavefunctions and their probability densities
fig, ax = plt.subplots(2, 1, figsize=(8, 6))

for n in range(3):  # Plot the three frist energy states
    ax[0].plot(x, wavefunctions[:, n], label=f'ψ_{n+1}(x)')
    ax[1].plot(x, wavefunctions[:, n]**2, label=f'|ψ_{n+1}(x)|²')

ax[0].set_title("Wavefunctions ψ(x)")
ax[1].set_title("Probability Densities |ψ(x)|²")
ax[0].set_ylabel("ψ(x)")
ax[1].set_ylabel("|ψ(x)|²")
ax[1].set_xlabel("Position x")
ax[0].legend()
ax[1].legend()
plt.tight_layout()
plt.show()
