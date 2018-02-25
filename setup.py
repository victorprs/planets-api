from setuptools import setup, find_packages

setup(
    name='planetsapi',
    version='0.1.0',
    author='Victor Peres',
    url='https://github.com/victorprs/planetsapi',
    description='Star Wars Planets Api',
    license='MIT',
    packages=['resources',],
    zip_safe=True,
    test_suite='tests'
)