import base64
import cv2


def cv2_to_base64(image) -> bytes:
    """
    encode cv2 image to base64 bytes as PNG

    parameters
    ---------
    image: np.ndarray
    """
    _, dst_data = cv2.imencode(".png", image)
    return base64.b64encode(dst_data)