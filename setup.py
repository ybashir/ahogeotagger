from setuptools import setup

setup(name='ahogeotagger',
      version='0.1',
      description='Uses efficient ahocorasick search to tag cities and countries in text',
      url='http://github.com/storborg/funniest',
      author='Yasser Bashir',
      author_email='yasser.bashir@arbisoft.com',
      license='MIT',
      packages=['ahogeotagger'],
      install_requires=[
          'pyahocorasick',
      ],
      zip_safe=False)
