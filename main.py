# Please pip install pillow before any of this
from PIL import Image

# In the brackets after ./ Write the file name
img = Image.open('./WhatsApp Image 2022-07-07 at 8.00.41 PM.jpeg')
img.thumbnail((400, 400))
# To save the image inside the brackets inside '' write th file name
img.save('thumbnail.jpg')
# Thank you!
