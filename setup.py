from distutils.core import setup

setup(
    name='spritz-cmd',
    version='0.1',
    author='Colin Su',
    author_email='littleq0903@gmail.com',
    scripts=['bin/spritz.py'],
    license='LICENSE',
    description='Command-line version of Spritz',
    long_description=open('README.md').read(),
)
