# plt-editor-tool

This module provides a GUI editor tool for editing the parameters of some basic matplotlib plots. The aim is to be able to modify the plotting parameters without going back to the root code and then to be able to save high quality publication ready plots.

The plt-editor-tool provides some of the functionality of the Matlab figure editor to the Matplotlib.pyplot system.

  - Easily change axis and title text and text properties
  - Manipulate data into plots in different grid layouts
  - Change line and marker colors and other parameters
  - Modify the properties of errorbars
  - Modify the properties of a fill_between plot
  - and more...

The plt-editor-tool is open source with a [public repository](https://github.com/RichardCouperthwaite/plt-editor-tool)
 on GitHub.

### Installation

The plt-editor-tool can be installed using PYPI.

```sh
$ pip install pltEditorTool
```

### Usage

The plt-editor-tool is straightforward to use. There is only a single class that can be imported from the package:

```py
from pltEditorTool import plotEditor
```

## Initialization

This class takes several inputs as shown below (the inputs marked with a * are required inputs):

```py
plotEditor(X, Y, x_err, y_err, fill, fill_alt, labels)
```

 - X*: the x-data for the plots
 - Y*: the y-data for the plots
 - x_err: the error in the x-measurement (used for plotting error bars on the data)
 - y_err: the error in the y-measurement (used for plotting error bars on the data)
 - fill: the distance away from the y-value to fill with color (if no fill_alt value is given, this value will be filled above and below the y-value)
 - fill_alt: the distance below the y-value to fill with color (use this if the area required to be filled is different above and below the y-value)
 - labels: the legend labels for each pair of x and y values
 
The data is provided to the tool in a series of lists to prevent problems with data of different sizes, for example one dataset has 10 values on x while a second has 100. Providing labels is not required but highly recommended to aid in determining which plot data is being manipulated in the tool. These can be added and modified later if so desired.

## Graphical User Interface Guide

When the plotEditor function is called a GUI will be generated. This GUI will be used to manipulate the appearance of the data for plotting and to also generate and save plots. This GUI is divided into two sections, at the top are the tools for changing the options associated with each of the X, Y pairs in the data.

 - Label: This is the legend label assigned to the line
 - Fill Label: If a fill is plotted, this will have an additional label in the legend
 - Errorbars: These features will change the appearance of x and y errorbars
 - Line: These features will change the appearance of the line plot
 - Markers: These features will change the appearance of the markers on the line plot
 - Fill: These features change the fill
 - Scatter: Select these features for a scatter plot (note: to modify the size of the scatter plot markers, use the marker size option)
 
For all feature changes, to change the color, click on the colored button and a separate dialog box for choosing the color will appear.
 
The second section determines which sets of data will appear on which plot axes in the final figure. It is possible to generate multiple plots in a single figure using the grid options. The general process will be as follows:

 - Select the size of the grid
 - Select to share x or y axis labels 
   * sharing x and y requires plots aligned to a square grid (axis values will be those for the top or left plot in each column or row)
 - Add the required number of axes
   * a first axis with all the data imported will be generated automatically
 - Select which plots to include in the axis
   * green arrow adds the plot in the all data box, red arrow removes the plot in the selected data box
 - Define the axis position
   * row and column values are 0 indexed
   * x- and y-ticks can be removed to improve appearance when x- and y-axes are shared
 - Change axis labels and adjust limits if necessary
   * axis limits are automatically adjusted to the maximum and minimum in the data when a plot is added to the axes
 - Change font settings for axis labels
 - Change plot title and font settings
 - Change preference for legend position
 
 
A few final notes:
 - Labels can include latex commands for symbols, e.g. ($\sigma$)
 - currently no option for changing the size of the legend text
 - Several of the most common errors that could occur will provide a pop-up warning detailing what went wrong
 

