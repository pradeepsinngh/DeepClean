import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-your-username",
    version="0.0.1",
    author="Pradeep Singh",
    author_email="pdeepsingh91@gmail.com",
    description="A python package for pre-processing text, image and speech data for machine learning.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pradeepsinngh/pre-process",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
