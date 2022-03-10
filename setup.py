from setuptools import find_packages, setup

setup(
    name='nexus_api',
    packages=find_packages(include=['nexus_api']),
    version='0.3.1',
    description='Nexus API connection methods',
    install_requires=['pandas','requests'],
    setup_requires = [],
    author='Nexus Integra',
    license='UNLICENSED: private Nexus Integra',
)
