import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="print-msg",
    version="0.9",
    author="Shvetsov Dmitry",
    author_email="shvetsovdmitry1996@gmail.com",
    description="Print colored status messages.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shvetsovdmitry/print-msg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)