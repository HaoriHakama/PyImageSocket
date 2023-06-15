import socket

from image_socket import format


def send_cv2_image(image, text, host="localhost", port=9008):
    """
    To send cv2 format image to port 9008

    Parameters:
    ---------
    image: Mat(np.ndarray)
    text: str
        text which is sent with the image
    host: str
    port: int
    """
    b64_image = format.cv2_to_base64(image)
    encoded_text = text.encode("utf-8")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(len(b64_image).to_bytes(4, byteorder="big"))
        s.sendall(b64_image)
        s.sendall(len(encoded_text).to_bytes(4, byteorder="big"))
        s.sendall(encoded_text)

