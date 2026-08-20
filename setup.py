#Copyright (c) 2026 Benjamin Winter
#This file is part of BasicMemManip which is released under the MIT License.
#See file LICENSE or go to https://github.com/core2000-eU/BasicMemManip for full license details.

#DESCRIPTION
#setup.py for BasicMemManip, a Python module that extends Python with some low-level, C/C++ -related features (intended to be used in combination with Pythons ctypes library)

import                          setuptools

setuptools.setup (
    name =                      "BasicMemManip", 
    version =                   '0.0.1',
    author =                    "Benjamin Winter",
    license=                    "MIT",
    description =               "BasicMemManip, a Python module that extends Python with some low-level, C/C++ -related features (intended to be used in combination with Pythons ctypes library)",
    long_description =          "BasicMemManip, a Python module that extends Python with some low-level, C/C++ -related features (intended to be used in combination with Pythons ctypes library)",
    keywords =                  ['C', 'C++', 'low-level', 'ctypes', 'WSTR', 'memory'],
    classifiers =               [
                                    "Development Status :: 4 - Beta",
                                    "Programming Language :: Python :: 3",
                                    "Operating System :: OS Independent"
                                ],
    packages =                  setuptools.find_namespace_packages(where="src/P"),
    package_dir =               {"": "src/P"},
    install_requires =          [],
    package_data =              {},
)
