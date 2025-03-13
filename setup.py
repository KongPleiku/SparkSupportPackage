from setuptools import setup, find_packages

setup(
    name="sparky",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    author="KongBeng",
    description="This is a simple package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/KongPleiku/SparkSupportPackage",
    classifiers=[
    ],
    python_requires='>=3.10',
)