# QRGen-using-Python
This Python script generates a customized QR code based on user input, using the qrcode and PIL (Python Imaging Library) libraries. The user is prompted to enter the following details for the QR code:

Data: The information to be encoded in the QR code.
Box Size: The size of each box in the QR code grid.
Border Size: The thickness of the border around the QR code.
Fill Color: The color of the QR code itself.
Background Color: The background color of the QR code image.
Main Functions:
get_user_input(): Gathers input parameters from the user.
generate_qr_code(): Generates the QR code image based on user-defined parameters.
main(): Calls the input function, generates the QR code, and saves it as an image file (QR.png).
After running the script, the QR code is saved as an image file named QR.png in the working directory.

Requirements:
qrcode
Pillow (PIL)
