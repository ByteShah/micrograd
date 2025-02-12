from setuptools import setup, find_packages

setup(
    name="micrograd",
    version="0.1.0",
    description="A tiny autograd engine and neural network library",
    author="Jaimin Shah",
    author_email="s1.jaimin@gmail.com",
    packages=find_packages(),
    install_requires=[
        "graphviz",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)