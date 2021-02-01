import qrcode

def create_qr(data: str, store: str):
    qr = qrcode.QRCode()
    qr.add_data(data)
    img = qr.make_image()
    img.save(f'images/{store}.png')

    return "OK"