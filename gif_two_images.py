import sys
from PIL import Image

# Verificar que se proporcionen exactamente dos imágenes
if len(sys.argv) != 3:
    print("Por favor, proporciona exactamente dos imágenes.")
    sys.exit(1)

images = []

# Cargar las imágenes
for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

# Crear una lista de imágenes alternadas
frames = [images[0], images[1], images[0], images[1]]

# Guardar el GIF animado con las imágenes alternadas
frames[0].save(
    "costumes.gif", save_all=True, append_images=frames[1:], duration=200, loop=0
)

print("GIF creado exitosamente como 'costumes.gif'.")
