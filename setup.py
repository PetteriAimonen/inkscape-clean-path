#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# sudo zypper in python-setuptools
# http://docs.python.org/2/distutils/setupscript.html#installing-additional-files
#
import sys,os,glob,re

from distutils.core import setup
from setuptools.command.test import test as TestCommand
import clean_path 	# for author(), version()

e = clean_path.CleanPath()
m = re.match('(.*)\s+<(.*)>', e.author())

# print ('.',['Makefile'] + glob.glob('clean_path*'))

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)



setup(name='clean-path',
      version = e.version(),
      description='Inkscape extension to workaround typical path issues.',
      author=m.groups()[0],
      author_email=m.groups()[1],
      url='https://github.com/jnweiger/inkscape-clean-path',
      scripts=filter(os.path.isfile, ['clean_path.py', 'clean_path.inx', 'README.md' ] ),

      packages=['clean-path'],
      license='GPL-2.0',
      classifiers=[
          'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
          'Environment :: Console',
          'Development Status :: 5 - Production/Stable',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
                  ],
      cmdclass={'test': PyTest},
      long_description="".join(open('README.md').readlines()),
      # tests_require=['pytest', 'scipy'],
      #packages=['pyPdf','reportlab.pdfgen','reportlab.lib.colors','pygame.font' ],
# 
)
