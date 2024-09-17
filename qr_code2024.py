import qrcode
from PIL import Image

def get_user_input():
    # Get user input for QR code data and parameters
    data = input("Enter the data for the QR code: ")
    box_size = int(input("Enter the box size (e.g., 10): "))
    border = int(input("Enter the border size (e.g., 4): "))
    fill_color = input("Enter the fill color (e.g., 'red'): ")
    back_color = input("Enter the background color (e.g., 'blue'): ")
    
    return data, box_size, border, fill_color, back_color

def generate_qr_code(data, box_size, border, fill_color, back_color):
    # Create a QRCode object with specified parameters
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=border
    )

    # Add data to the QRCode instance
    qr.add_data(data)
    qr.make(fit=True)

    # Generate the image with specified colors
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    
    return img

def main():
    # Get user input
    data, box_size, border, fill_color, back_color = get_user_input()
    
    # Generate QR code and save the image
    img = generate_qr_code(data, box_size, border, fill_color, back_color)
    img.save("QR.png")
    print("QR code generated and saved as 'QR.png'.")

if __name__ == "__main__":
    main()
