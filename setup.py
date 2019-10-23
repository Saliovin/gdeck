import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gdeck",
    version="1.0.0",
    author="Jonas",
    author_email="jonas.eukan@gmail.com",
    description="A module for implementing playing cards",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Saliovin/gdeck",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7'
)