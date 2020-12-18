from setuptools import setup
import os

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(name='sketchify',
      version='0.0.6',
      description='A simple sketching package which converts images into drawings.',
      long_description=open("README.md").read(),
      long_description_content_type='text/markdown',
      author='Rahul Prabhu',
      author_email='rahul@grokwithrahul.com',
      url='https://github.com/grokwithrahul/sketchify',
      packages=['sketchify'],
      install_requires=['opencv-contrib-python']
     )