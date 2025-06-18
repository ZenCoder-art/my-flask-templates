# setup.py
from setuptools import find_packages, setup

setup(
    name="flaskx",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask",
        "click",
    ],
    entry_points={
        "console_scripts": [
            "flaskx=flaskx.cli:cli",
        ],
    },
)
