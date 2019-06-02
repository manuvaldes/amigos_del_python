#! /usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools

long_description = open('README.rst', 'rb').read().decode('utf-8')

install_requires = ["requests<=2.21.0", "beautifulsoup4<=4.7.1"]


setuptools.setup(
    name="pyramide",
    version="0.0.1",
    url="https://github.com/manuvaldes/amigos_del_python",
    download_url = "https://github.com/manuvaldes/amigos_del_python.git",
    author="manuvaldes",
    author_email="manuvaldes@gmail.com",
    description="pyramide es un simple crawler basado en crawlerino",
    packages=["pyramide"],
    install_requires= install_requires,
    license='MIT License',
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
