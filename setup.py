from setuptools import setup

setup(
  name = 'featureflagtech',
  version = '0.0.8',
  author = 'Charlie Hodgkinson',
  author_email = 'charlotte.hodgkinson4@gmail.com, info@featureflag.tech',
  description = 'Feature flag service built for developers',
  long_description = open('README.md').read(),
  long_description_content_type = 'text/markdown',
  url = 'https://github.com/featureflagtech/featureflagtechpython',
  packages = ['featureflagtech'],
  install_requires=[
    'requests'
  ],
  classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: Apache Software License",
    "Operating System :: OS Independent",
  ],
  python_requires='>=3.5',
)