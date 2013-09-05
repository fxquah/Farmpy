import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='farmpy',
    version='0.1',
    description='Package to run farm jobs - currently LSF supported',
    long_description=read('README'),
    author='Martin Hunt',
    author_email='mh12@sanger.ac.uk',
    url='https://github.com/martinghunt/farmpy',
    packages=find_packages(),
    scripts=[os.path.join('scripts', 'bsub.py')],
    test_suite='nose.collector',
    install_requires=['nose >= 1.3'],
    license='GPL'
)
