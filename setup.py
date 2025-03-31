from setuptools import setup, find_packages

setup(
    name='ansible_demo',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'ansible',
    ],
    entry_points={
        'console_scripts': [
            'demo=ansible_demo.cli:main',
        ],
    },
)
