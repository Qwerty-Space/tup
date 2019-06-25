from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='tup',  
    version='0.1',
    entry_points={"console_scripts": ["tup = tup:main"]},
    author="Oliver Duce",
    author_email="oliver_duce@live.co.uk",
    description="CLI Telegram file uploder",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Qwerty-Space/tup",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPLv3 License",
        "Operating System :: OS Independent",
    ],
)