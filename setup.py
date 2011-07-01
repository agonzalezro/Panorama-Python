from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='Panorama',
      version=version,
      description="Wrapper class to manage video services in a standarized way. It is an easy way to obtain a few basics about a video only through its url.",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='panorama python video wrapper vimeo youtube',
      author='\xc3\x81lex Gonz\xc3\xa1lez',
      author_email='agonzalezro@gmail.com',
      url='http://github.com/agonzalezro/Panorama-Python',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
