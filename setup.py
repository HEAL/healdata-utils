from setuptools import setup, find_namespace_packages

setup(
    name='healdata_utils',
    version='0.0.1',
    author='',
    author_email='',
    description='Data packaging tools for the HEAL data ecosystem',
    url='https://github.com/norc-heal/heal-data-dictionaries/src/healdata-utils',
    package_dir={'': 'src'},
    packages=find_namespace_packages(where='src'),
    install_requires=[
        'petl',
        'jsonschema',
        'requests',
        'pyyaml',
        'frictionless',
        'pyreadstat',
        'dataforge[redcap] @ git+https://gitlab.com/mbkranz/data-forge.git@0afa429d6b7d1f1ec04ff8c4ee127291b3b058d4',
        'xmltodict' #NOTE:used until schemas put into dataforge
    ],
    entry_points='''
        [console_scripts]
        vlmd=healdata_utils.cli:main
    ''',

)
