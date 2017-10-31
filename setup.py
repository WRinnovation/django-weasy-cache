from distutils.core import setup

setup(
    name='django-weasy-cache',
    version='0.1dev',
    packages=['djangoweasycache', ],
    requires=['python (>= 2.7)', 'django (>=1.8)'],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.txt').read(),
)
