from setuptools import setup, find_packages

setup(
    name='django-weasy-cache',
    version='0.6dev',
    packages=['djangoweasycache', ],
    requires=['python (>= 2.7)'],
    license='Apache2',
    long_description=open('README.txt').read(),
    keywords='django simple cache',
)
