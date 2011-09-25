from setuptools import setup, find_packages

name='transliteration'

setup (
    name=name,
    version="0.1",
    url="http://silpa.org.in/Transliterate",
    license="LGPL 3.0",
    description="Indian Language Transliteration Library",
    author='Santhosh Thottingal',
    author_email="santhosh.thottingal@gmail.com",
    long_description="""This library helps in transliteration
from English to Indian Language and from one Indian Language
to another Indian Language.""",
    packages=find_packages('src'),
    package_dir={'':'src'},
    package_data={'transliteration':['cmudict.0.7a_SPHINX_40']},    
    include_package_data=True,
    namespace_packages=['transliteration'],
    install_requires=['setuptools'],
    zip_safe=False,
    )
