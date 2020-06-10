import numpy as np

# Definimos el tamaño del array que vamos a construir
big_array_size = 1000000

# Definimos la semilla del generador random
seed_cualquier_numero = 2843

# Creamos el generador
random_generator_seed = np.random.default_rng(seed_cualquier_numero)

# Creamos el array con elementos de distribución uniforme
low = 1
high = 100
big_array = random_generator_seed.uniform(low, high, size=big_array_size)


# Alternativa lite
np.random.normal(3, 2.5, size=(2, 4))
