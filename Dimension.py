from PIL import Image

# Abre la imagen
im = Image.open("C:/Users/Rode/Downloads/mouredev_github_profile.png")

# Muestra la imagen

# Obtener el ancho y el alto de la imagen
width, height = im.size

aspect_ratio = width / height

im.show()

print(f'Ancho: {width}, Alto: {height}')
print(f'Relación de aspecto: {aspect_ratio:.2f}')