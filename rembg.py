#pip install rembg
from rembg import remove

input_path = 'image.jpg'
output_path = 'output.png'

with open(input_path, 'rb') as input_file:
    with open(output_path, 'wb') as output_file:
        output_file.write(remove(input_file.read()))
