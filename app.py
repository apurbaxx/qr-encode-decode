
import os
import sys
from datetime import datetime

import qrcode
from PIL import Image
from pyzbar import pyzbar


def print_banner():
    print("=" * 50)
    print("QR Code Generator & Decoder")
    print("=" * 50)
    print()


def get_user_choice():
    print("What would you like to do?")
    print("1. Generate QR Code (Encode)")
    print("2. Read QR Code (Decode)")
    print("3. Exit")
    print()
    
    while True:
        choice = input("Enter your choice (1-3): ").strip()
        if choice in ['1', '2', '3']:
            return choice
        print("Invalid choice! Please enter 1, 2, or 3.")


def encode_qr():
    print("\nQR Code Generator")
    print("-" * 20)
    
    # Get text to encode
    text = input("Enter the text/message to encode: ").strip()
    if not text:
        print("Text cannot be empty!")
        return
    
    # Get output filename
    default_name = f"qrcode_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    filename = input(f"Enter filename (press Enter for '{default_name}'): ").strip()
    if not filename:
        filename = default_name
    
    # Add .png extension if not present
    if not filename.lower().endswith('.png'):
        filename += '.png'
    
    try:
        # Create QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)
        
        # Create image
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(filename)
        
        print(f"QR code saved successfully as '{filename}'")
        
        # Ask if user wants to view the image
        view = input("Would you like to view the image? (y/n): ").strip().lower()
        if view in ['y', 'yes']:
            try:
                img.show()
            except Exception as e:
                print(f"Could not display image: {e}")
                
    except Exception as e:
        print(f"Error creating QR code: {e}")


def decode_qr():
    """Interactive QR code decoding"""
    print("\nQR Code Decoder")
    print("-" * 18)
    
    # Get image path
    image_path = input("Enter the path to the QR code image: ").strip()
    
    # Remove quotes if present
    image_path = image_path.strip('"\'')
    
    if not image_path:
        print("Path cannot be empty!")
        return
    
    if not os.path.exists(image_path):
        print(f"File not found: {image_path}")
        return
    
    try:
        # Open and decode image
        img = Image.open(image_path)
        decoded_objects = pyzbar.decode(img)
        
        if not decoded_objects:
            print("No QR code found in the image or could not decode.")
            return
        
        print(f"Found {len(decoded_objects)} QR code(s):")
        print("-" * 30)
        
        for i, obj in enumerate(decoded_objects, 1):
            decoded_text = obj.data.decode('utf-8')
            print(f"QR Code {i}: {decoded_text}")
        
        print("-" * 30)
        
        # Ask if user wants to view the image
        view = input("Would you like to view the image? (y/n): ").strip().lower()
        if view in ['y', 'yes']:
            try:
                img.show()
            except Exception as e:
                print(f"Could not display image: {e}")
                
    except Exception as e:
        print(f"Error reading image: {e}")


def main():
    """Main application loop"""
    print_banner()
    
    while True:
        choice = get_user_choice()
        
        if choice == '1':
            encode_qr()
        elif choice == '2':
            decode_qr()
        elif choice == '3':
            print("\nThank you for using QR Code Generator & Decoder!")
            break
        
        print("\n" + "=" * 50)
        
        # Ask if user wants to continue
        continue_choice = input("\nWould you like to do something else? (y/n): ").strip().lower()
        if continue_choice not in ['y', 'yes']:
            print("\nThank you for using QR Code Generator & Decoder!")
            break
        print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGoodbye!")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
