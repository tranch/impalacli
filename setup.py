import re
import ast

from setuptools import setup, find_packages

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('impalacli/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

description = 'CLI for Impala Database. With syntax highlighting.'

install_requirements = [
    'click',
    'cli-helpers==1.0.2',
    'docopt==0.6.2',
    'impyla==0.14.1',
    'prompt-toolkit==1.0.15',
    'Pygments==2.2.0',
]

setup(
    name='impalacli',
    packages=find_packages(),
    version=version,
    description=description,
    long_description=description,
    install_requires=install_requirements,
    url='https://github.com/tranch/impalacli',
    license='BSD',
    author='tranch',
    author_email='tranch.xiao@gmail.com',
    platforms=['any'],
    entry_points={
        'console_scripts': ['impalacli = impalacli.main:cli'],
    }
)
