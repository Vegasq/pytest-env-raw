"""pytest-env setup module."""

from setuptools import setup

DESCRIPTION = 'py.test plugin that allows you to add environment variables.'

setup(
    name='pytest-envraw',
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    version='0.1',
    author='mail@mkla.dev',
    author_email='mail@mkla.dev',
    url='https://github.com/Vegasq/pytest-env-raw',
    packages=['pytest_envraw'],
    entry_points={'pytest11': ['envraw = pytest_envraw.plugin']},
    install_requires=['pytest>=2.6.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ]
)
