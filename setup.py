import pathlib
from pathlib import Path
from setuptools import setup
import os
from cheatsheets import CHEAT_DIRECTORY

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

if not os.path.exists(CHEAT_DIRECTORY):
    os.makedirs(CHEAT_DIRECTORY)

setup(
    name="cheatsheets",
    version="0.0.4",
    description="Cheatsheets",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Tlalocan/cheatsheets",
    author="Tlaloc-Es",
    author_email="",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["cheatsheets"],
    include_package_data=True,
    install_requires=["simple-term-menu", "pygments", "click"],
    entry_points={
        "console_scripts": [
            "cheatsheets=cheatsheets.__main__:main",
        ]
    },
)