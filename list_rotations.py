def list_rotations(cubepart, dimension=3, reference_matrix = None):
    import numpy as np
    rotations = []
    for i in range(0, dimension):
        for j in range(0, dimension):
            for k in range(0, dimension+1):
                if i != j:
                    rotations.append(np.rot90(cubepart.swapaxes(i, j), k+1))
    return rotations
