from setuptools import find_packages, setup

setup(
    name='nexus_api',
    packages=find_packages(include=['nexus_api']),
    version='0.2.0',
    description='NexusAPI',
    install_requires=['pandas'],
    setup_requires = [],
    tests_require = [],
    author='Nexus Integra',
    license='UNLICENSED: private Nexus Integra',
)
