from setuptools import setup, find_packages

setup(
    name='booklover',
    version='0.1.0',
    url='https://github.com/cmclaugh3/booklover',
    author='Conor McLaughlin',
    description='Package containing Python Scripts for DS5100 hw09',
    packages=find_packages().
    license='MIT',
    install_requires=['pandas >= 0.20.0']
)

