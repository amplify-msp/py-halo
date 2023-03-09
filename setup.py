from setuptools import setup

setup(
    name='pyhalo',
    version='0.0.1',
    description='Library for the HaloPSA API',
    url='https://github.com/amplify-msp/py-halo',
    author='Matt Keathley',
    author_email='matt.keathley@amplifymsp.com',
    packages=[
        'pyhalo'
    ],
    requires=[
        'requests'
    ]
)
