from setuptools import find_packages, setup

setup(
    name='nexus_api',
    packages=find_packages(include=['nexus_api']),
    version='0.1.0',
    description='NexusAPI',
    install_requires=['pandas'],
    setup_requires = ['pytest-runner'],
    tests_require = ['pytest'],
    author='Nexus Integra',
    license='UNLICENSED: private Nexus Integra',
)
