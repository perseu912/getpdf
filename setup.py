from setuptools import setup
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='getpdf',
    version='0.0.4',
    url='https://github.com/perseu912/getpdf',
    license='MIT License',
    author='Reinan Br',
    entry_points = {
         'console_scripts': ['getpdf=getpdf.get_pdf_line:main'],
     },
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='slimchatuba@gmail.com',
    keywords='kit tools dev works',
    description=u'Library for getting PDF  from google search',
    packages=find_packages(),
    install_requires=['requests','googlesearch-python'],)
