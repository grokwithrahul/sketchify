from setuptools import setup
import os

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(name='sketchify',
      version='0.0.1',
      description='A simple sketching package which converts images into drawings.',
      long_description=open("README.md").read(),
      author='Rahul Prabhu',
      author_email='rahul@grokwithrahul.com',
      url='https://github.com/Redstomite/sketchify',
      packages=['sketchify'],
     )