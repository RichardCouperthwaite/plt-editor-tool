from distutils.core import setup

setup(
  name = 'pltEditorTool',         # How you named your package folder (MyLib)
  packages = ['pltEditorTool'],   # Chose the same as "name"
  version = '1.0.14',    # Start with a small number and increase it with every change you make
  license='GNU Lesser General Public License v3 (LGPLv3)',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'This module provide a GUI based approach for setting up and editing matplotlib plots',   # Give a short description about your library
  long_description='This module provide a GUI based approach for setting up and editing matplotlib plots',
  author = 'Richard Couperthwaite',                   # Type in your name
  author_email = 'richard.couperthwaite@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/RichardCouperthwaite/plt-editor-tool',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/RichardCouperthwaite/plt-editor-tool/archive/1.0.14.tar.gz',    # I explain this later on
  keywords = ['Matplotlib', 'Pyplot', 'GUI', 'Editor'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'tkcolorpicker',
          'numpy',
          'matplotlib',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)