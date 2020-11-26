from setuptools import setup, find_packages

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'pltEditorTool',
  packages = ['pltEditorTool'],
  version = '2.2.5', 
  license='GNU Lesser General Public License v3 (LGPLv3)',
  description = 'This package provides a GUI for editing matplotlib plots',   
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Richard Couperthwaite', 
  author_email = 'richard.couperthwaite@gmail.com',
  url = 'https://github.com/RichardCouperthwaite/plt-editor-tool',
  download_url = 'https://github.com/RichardCouperthwaite/plt-editor-tool/archive/2.2.5.tar.gz',
  keywords = ['Matplotlib', 'Pyplot', 'GUI', 'Editor'], 
  include_package_data = True,
  data = ['pltEditorTool/icon2.png', 
          'pltEditorTool/pltEditorGUI-1.ui', 
          'pltEditorTool/pltEditorGUI-2.ui',
          ],
  install_requires=[
          'tkcolorpicker',
          'numpy',
          'matplotlib',
          'PyQt5',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable', 
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
    'Programming Language :: Python :: 3', 
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)