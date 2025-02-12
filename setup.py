from setuptools import setup, find_packages

setup(
    name="grad-mlp",
    version="0.1.1",
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