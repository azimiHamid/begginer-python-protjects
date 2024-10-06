import qrcode

data = input('Enter your text or URL: ').strip()
filename = input('Enter the the filename (e.g., image.png): ').strip()

if not filename.endswith('.png'):
    filename += '.png'

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)

qr.make(fit=True)

image = qr.make_image(fill_color='black', back_color='white')
image.save(filename)

print(f'QRCode saved as {filename}')

# Don't forget to install pillow
#   pip install pillow