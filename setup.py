from setuptools import setup

setup(name='automlk',
      version='0.1',
      description='Auto Machine Learning package for Python',
      url='https://github.com/karlloic/automlk.git',
      author='Karl Kamdem',
      author_email='karlloic@gmail.com',
      license='',
      packages=['automlk'],
      install_requires=[
          'sklearn',
          'pandas',
          'imblearn'
      ],
      zip_safe=False)
