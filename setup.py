from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import codecs
import os
import sys
import re

here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    # intentionally *not* adding an encoding option to open
    return codecs.open(os.path.join(here, *parts), 'r').read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['--strict', '--verbose', '--tb=long', 'tests']
        self.test_suite = True

    def run_tests(self):
        import pytest

        errno = pytest.main(self.test_args)
        sys.exit(errno)

long_description = read('README.md')

setup(
    name='turnkey_tools',
    version=find_version('src', '__init__.py'),
    url='https://github.com/kefniark/turnkey-tools',
    license='[MIT License]',
    author='Destrem Kevin',
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    test_suite='tests.test_app',
    install_requires=[],
    description='Automated Test',
    long_description=long_description,
    entry_points={
        'console_scripts': [
            'turnkey-tools = src.app_cli:main',
        ],
    },
    packages=['src', 'src.model', 'src.plugins'],
    include_package_data=True,
    platforms='any',
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: Beta',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: MIT License',
        'Operating System :: OS Independent',
    ],
    extras_require={
        'testing': ['pytest'],
    }
)
