"""
Zinc Python Tools

A collection of Qt widgets and utilities building on the Python bindings for the OpenCMISS-Zinc Visualisation Library.
"""

classifiers = """\
Development Status :: 5 - Production/Stable
Intended Audience :: Developers
Intended Audience :: Education
Intended Audience :: Science/Research
License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)
Programming Language :: Python
Operating System :: Microsoft :: Windows
Operating System :: Unix
Operating System :: MacOS :: MacOS X
Topic :: Scientific/Engineering :: Medical Science Apps.
Topic :: Scientific/Engineering :: Visualization
Topic :: Software Development :: Libraries :: Python Modules
"""

from setuptools import setup

doc_lines = __doc__.split("\n")
requires = ['opencmiss.utils']

setup(
    name='ZincPythonTools',
    version='1.0.0',
    author='H. Sorby',
    author_email='h.sorby@auckland.ac.nz',
    packages=['opencmiss', 'opencmiss.zincwidgets'],
    platforms=['any'],
    url='http://pypi.python.org/pypi/ZincPythonTools/',
    license='LICENSE.txt',
    description=doc_lines[0],
    classifiers=filter(None, classifiers.split("\n")),
    install_requires=requires,
)
