import qrcode, time

# input Data
text:str = input("Please inter your text:")
file_name:str = input("Please inter your file name:")

# Make QRcode
qr = qrcode.make(text)
qr.save(f"{file_name}.png")
