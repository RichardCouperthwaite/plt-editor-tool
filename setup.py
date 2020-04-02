from distutils.core import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.txt'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'pltEditorTool',
  packages = ['pltEditorTool'],
  version = '2.0.2', 
  license='GNU Lesser General Public License v3 (LGPLv3)',
  description = 'This package provides a GUI for editing matplotlib plots',   
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Richard Couperthwaite', 
  author_email = 'richard.couperthwaite@gmail.com',
  url = 'https://github.com/RichardCouperthwaite/plt-editor-tool',
  download_url = 'https://github.com/RichardCouperthwaite/plt-editor-tool/archive/2.0.2.tar.gz',
  keywords = ['Matplotlib', 'Pyplot', 'GUI', 'Editor'], 
  install_requires=[
          'tkcolorpicker',
          'numpy',
          'matplotlib',
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