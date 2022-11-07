from setuptools import setup, find_namespace_packages

setup(
    name='healdata_utils',
    version='0.0.1',
    author='',
    author_email='',
    description='Data packaging tools for the HEAL data ecosystem',
    url='https://github.com/norc-heal/heal-data-dictionaries/code/healdata-utils',
    package_dir={'': 'code'},
    packages=find_namespace_packages(where='code'),
    install_requires=[
        'petl',
        'jsonschema',
        'requests',
        'pyyaml',
        'frictionless',
        'gen3'
    ]
)
