"""The python wrapper for IQ Option API package setup."""

from setuptools import setup, find_packages

setup(
    name="exnova",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["requests", "websocket-client"],
    include_package_data=True,
    description="Best IQ Option API for python",
    long_description="Best IQ Option API for python",
    url="https://github.com/zagmi/exnova",
    author="Santiago Ramirez",
    zip_safe=False,
)
