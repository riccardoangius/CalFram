from setuptools import setup, find_packages

setup(
    name='calfram',
    version='0.1.0',
    url=https://github.com/lorenzofamiglini/CalFram',
    author='Lorenzo Famiglini',
    author_email='lorenzofamiglini@gmail.com',
    description='A comprehensive framework for assessing calibration in machine and deep learning models',
    packages=find_packages(),
    install_requires=[
    'pandas',
    'numpy',
    'matplotlib',
    'sklearn',
    'ipdb',
]
)
