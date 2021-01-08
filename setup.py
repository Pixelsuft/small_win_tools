from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="small_win_tools",
    version="1.0.0",
    author="Pixelsuft",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Pixelsuft/small_win_tools/",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows :: Windows 10",
    ],
    python_requires='>=3.5',
    license='MIT', 
    keywords='small_win_tools',
    install_requires=[''] 
)