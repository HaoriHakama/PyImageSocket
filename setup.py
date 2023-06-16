from setuptools import setup


setup(
    name="PyImageSocket",
    version="1.0.1",
    description="My Library for send and receive image files using socket",
    author="HaoriHakama678",
    packages=["pyimagesocket", "pyimagesocket.image_socket"],
    install_requires=["opencv-python"],
)
