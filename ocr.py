from PIL import Image
import pytesseract

def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(filename), config='--psm 6 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ');  
    # text = pytesseract.image_to_string(Image.open(filename), config='-l eng+spa');  
     
    return text

print(ocr_core('images\original.png'))