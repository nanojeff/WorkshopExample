from setuptools import setup, find_packages

setup(name='WorkshopExample',
      version='0.0.1',
      description='Random example project for coding workshop',
      url='http://github.com/nanojeff/WorkshopExample',
      author='Samuel Hinton',
      author_email='jeffrey.barber@gmail.com',
      license='MIT',
      install_requires=['numpy'],
      packages=find_packages(exclude=('tests', 'doc', 'data'))
      )
