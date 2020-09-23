import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="JogoDaVelha-Elielson68", # Replace with your own username
    version="0.0.1",
    author="Elielson Barbosa",
    author_email="elielsonbr.com@gmail.com",
    description="is a simples 'jogo da velha' game",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Elielson68/JogoDaVelha",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)