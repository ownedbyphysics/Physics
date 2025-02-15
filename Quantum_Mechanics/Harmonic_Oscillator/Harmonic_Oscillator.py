import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh_tridiagonal

# Define parameters
L = 5.0  # Length of the potential region
N = 500  # Number of grid points
x = np.linspace(-L, L, N)  # Position grid
dx = x[1] - x[0]  # Grid spacing
m = 1.0  # Mass of the particle
omega = 1.0  # Angular frequency of the oscillator
hbar = 1.0  # Reduced Planck's constant

# Create the Hamiltonian matrix using finite differences
V = 0.5 * m * omega**2 * x**2  # Harmonic oscillator potential
diagonal = np.full(N, 2.0)  # Main diagonal (2/h^2 term)
off_diagonal = np.full(N - 1, -1.0)  # Off-diagonals (-1/h^2 term)

# Kinetic energy term
T = -0.5 * hbar**2 / m * (np.diag(-2 * np.ones(N)) + np.diag(np.ones(N - 1), 1) + np.diag(np.ones(N - 1), -1)) / dx**2

# Hamiltonian matrix: H = T + V
H = T + np.diag(V)

# Solve for eigenvalues (energies) and eigenvectors (wavefunctions)
eigenvalues, eigenvectors = eigh_tridiagonal(np.diagonal(H), np.diagonal(H, 1))

# Normalize wavefunctions
wavefunctions = eigenvectors / np.sqrt(dx)

# Plot the first three wavefunctions and their probability densities
fig, ax = plt.subplots(2, 1, figsize=(8, 6))

for n in range(3):  # Plot the first three energy states
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

# Print the first few energy levels (in units of hbar * omega)
print("First few energy levels (in units of hbar * omega):")
for i in range(3):
    print(f"n={i}, Energy = {eigenvalues[i]:.2f}")
