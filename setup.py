from setuptools import setup

setup(
   name='frost',
   version='1.0',
   description='A modern password manager wr,itten in python',
   author='Baran Gokalp',
   author_email='oxydess@protonmail.com',
   packages=['frost'],  #same as name
   install_requires=['argparse'], #external packages as dependencies
)
