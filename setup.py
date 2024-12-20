from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="spips",
    version="0.2.0",
    description="spips a framework for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["spips"],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "spips=spips.cli:main",
        ],
    },
)