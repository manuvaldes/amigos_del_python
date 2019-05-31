#! /usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools

setuptools.setup(
    name="pyramide",
    version="0.0.1",
    url="https://github.com/manuvaldes/pyramide",
    download_url = "https://github.com/manuvaldes/pyramide.git",

    author="manuvaldes",
    author_email="manuvaldes@gmail.com",

    description="pyramide es un simple crawler basado en crawlerino",
    long_description='\n\n'.join(
        open(f, 'rb').read().decode('utf-8')
        for f in ['README.rst', 'HISTORY.rst']),

    packages=setuptools.find_packages(),

    install_requires=[],

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
