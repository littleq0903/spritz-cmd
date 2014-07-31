from distutils.core import setup

setup(
    name='spritz',
    version='0.1',
    authors=['Colin Su', 'Stephen Margheim'], 
    author_emails=['littleq0903@gmail.com', 'stephen.margheim@gmail.com'],
    scripts=['bin/spritz.py'],
    license='LICENSE',
    description='Command-line version of Spritz',
    long_description=open('README.md').read(),
)
