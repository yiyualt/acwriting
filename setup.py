from setuptools import setup, find_packages


with open("README.md", "r") as f:
    long_description = f.read()


setup(
    name= "acwrite",
    version = "1.1",
    author="Yi Yu",
    author_email="q1499114179@gmail.com",
    description="A python package for writing academic papers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Yoki0/acwriting",
    packages = find_packages(),
    classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=["httpcore","httpx","nltk","goslate","bs4","requests"],
    scripts=['bin/acword']
    )
