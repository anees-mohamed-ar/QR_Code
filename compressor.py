import zlib
import base64

def compress_text(text):
    compressed_data = zlib.compress(text.encode('utf-8'))
    encoded_data = base64.b64encode(compressed_data).decode('utf-8')
    return encoded_data

def decompress_text(encoded_data):
    compressed_data = base64.b64decode(encoded_data.encode('utf-8'))
    text = zlib.decompress(compressed_data).decode('utf-8')
    return text

def is_compressed(text):
    try:
        # Attempt to decompress the text to check if it is compressed
        zlib.decompress(base64.b64decode(text.encode('utf-8')))
        return True
    except (zlib.error, base64.binascii.Error):
        return False
