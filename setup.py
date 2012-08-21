from setuptools import setup, find_packages

name='transliteration'

setup (
    name=name,
    version="0.3",
    url="http://silpa.org.in/Transliterate",
    license="LGPL 3.0",
    description="Indian Language Transliteration Library",
    author='Santhosh Thottingal',
    author_email="santhosh.thottingal@gmail.com",
    long_description="""This library helps in transliteration
from English to Indian Language and from one Indian Language
to another Indian Language.""",
    include_package_data=True,    
    packages=find_packages(exclude='tests'),
    setup_requires=['setuptools-git'],
    install_requires=['setuptools','normalizer'],
    zip_safe=False,
    )
