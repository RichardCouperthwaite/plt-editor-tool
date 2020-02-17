from distutils.core import setup

long_description = "This module provides a GUI editor tool for editing the \
parameters of some basic matplotlib plots. The aim is to be able to modify \
the plotting parameters without going back to the root code and then to be \
able to save high quality publication ready plots. \n \n\
The plt-editor-tool provides some of the functionality of the Matlab figure \
editor to the Matplotlib.pyplot system, including: \n \n\
- Easily change axis and title text and text properties\n \
- Manipulate data into plots in different grid layouts\n\
- Change line and marker colors and other parameters\n\
- Modify the properties of errorbars\n\
- Modify the properties of a fill_between plot\n"


setup(
  name = 'pltEditorTool',         # How you named your package folder (MyLib)
  packages = ['pltEditorTool'],   # Chose the same as "name"
  version = '1.0.10',    # Start with a small number and increase it with every change you make
  license='GNU Lesser General Public License v3 (LGPLv3)',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'This module provide a GUI based approach for setting up and editing matplotlib plots',   # Give a short description about your library
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Richard Couperthwaite',                   # Type in your name
  author_email = 'richard.couperthwaite@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/RichardCouperthwaite/plt-editor-tool',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/RichardCouperthwaite/plt-editor-tool/archive/1.0.10.tar.gz',    # I explain this later on
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