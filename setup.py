#!/usr/bin/env python

from distutils.core import setup

with open('README.rst') as readme:
    long_description = readme.read()

requirements = [
    'Django>=1.8',
    'psycopg2',
]

setup(
    name='django-pg-array-lookups',
    version='0.1.1',
    description='ANY/ALL lookups for PostgreSQL arrays',
    long_description=long_description,
    author="Omar Khan",
    author_email='omar@omarkhan.me',
    url='https://github.com/omarkhan/django-pg-array-lookups',
    py_modules=['pg_array_lookups'],
    install_requires=requirements,
    license='MIT',
    keywords='django postgresql',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
