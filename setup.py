from setuptools import setup

setup(
   name='frost',
   version='1.0',
   description='A modern password manager written in Python',
   author='Baran Gokalp',
   author_email='oxydess@protonmail.com',
   packages=['frost'],  # Same as the name of the package
   install_requires=['argparse'],  # external dependencies here if needed
)
