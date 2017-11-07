from setuptools import setup, find_packages

setup(
    name='django-weasy-cache',
    version='0.4dev',
    packages=['djangoweasycache', ],
    requires=['python (>= 2.7)', 'django (>=1.8)'],
    license='Apache2',
    long_description=open('README.txt').read(),
    keywords='django simple cache',
)
