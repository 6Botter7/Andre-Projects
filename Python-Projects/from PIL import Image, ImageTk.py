from PIL import Image, ImageTk
from urllib import request
import PySimplegui
# Get one PNG file from website and save to file
url = (
    "https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/"
    "images/for_readme/Logo%20with%20text%20for%20GitHub%20Top.png")
headers = {
    'User-Agent': (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36')}
req = request.Request(url, headers=headers)
response = request.urlopen(req)
if response.status != 200:
    print("Failed to load image from website !")
    exit()
data = response.read()

filename = "example.png"
with open(filename, "wb") as f:
    f.write(data)

# Resize PNG file to size (300, 300)
size = (300, 300)
im = Image.open(filename)
im = im.resize(size, resample=Image.BICUBIC)

sg.theme('DarkGreen3')

layout = [
    [sg.Image(size=(300, 300), key='-IMAGE-')],
]
window = sg.Window('Window Title', layout, margins=(0, 0), finalize=True)