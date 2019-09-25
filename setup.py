from setuptools import setup, find_packages

setup(
    name="py_multislice",
    version="0.1",
    description="An open-source Python multislice package",
    author="Hamish Brown",
    author_email="hamishgallowaybrown@gmail.com",
    url="https://github.com/HamishGBrown/py_multislice/",
    packages=find_packages(),
     install_requires=[
        'numpy >= 1.15, < 2.0',
        'torch >= 1.2, < 2.0',
        'tqdm >= 4.0'
        ]

)
