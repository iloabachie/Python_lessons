import qrcode

# Create QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2,
)

# Add data to encode
qr.add_data('https://cosyoumatter.com/')
qr.make(fit=True)

# Create and save the image
img = qr.make_image(fill_color="black", back_color="white")
img.save('qrcode.png')
