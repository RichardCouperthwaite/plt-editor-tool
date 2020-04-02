import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkcolorpicker import askcolor
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from .plot_code import write_code_file


# Defined Colours
BG_BLUE = '#409fff'
BG_GREEN = '#6AD535'
BG_RED = '#F22140'

class window(tk.Frame):
    """
    The window class creates the TkInter window for the post-processor and
    controls all its functions
    """

    def __init__(self, data_dict, master=None):
        self.Directory = ''
        super().__init__(master)
        # Define the variables for controlling the system
        self.data_dict = data_dict
        self.axis_dict = {}
        self.data_list = ['']
        self.axis_list = ['']
        self.dat_lab = tk.StringVar()
        self.dat_lab2 = tk.StringVar()
        self.current_data = tk.StringVar()
        self.multi_select = tk.IntVar()
        self.multi_list = tk.StringVar()
        self.selected_data_value = ''
        self.selected_axis_value = ''
        self.ebar_exist = tk.IntVar()
        self.ebar_color = tk.StringVar()
        self.ebar_linew = tk.IntVar()
        self.ebar_caps = tk.IntVar()
        self.ebar_capt = tk.IntVar()
        self.line_exist = tk.IntVar()
        self.line_color = tk.StringVar()
        self.line_style = tk.StringVar()
        self.line_width = tk.IntVar()
        self.styles = [':', '-.', '--', '-', '']
        self.line_alpha = tk.DoubleVar()
        self.mark_exist = tk.IntVar()
        self.mark_type = tk.StringVar()
        self.mark_ec = tk.StringVar()
        self.mark_ew = tk.IntVar()
        self.mark_fc = tk.StringVar()
        self.mark_sz = tk.IntVar()
        self.marker_types = [".", ",", "o", "v", "^", "<", ">", "1", "2", "3",
                             "4", "8", "s", "p", "P", "*", "h", "H", "+", "x",
                             "X", "D", "d", "|", "_", "None"]
        self.fill_exist = tk.IntVar()
        self.fill_alpha = tk.DoubleVar()
        self.fill_ec = tk.StringVar()
        self.fill_fc = tk.StringVar()
        self.fill_linew = tk.IntVar()
        self.fill_lines = tk.StringVar()
        self.scat_exist = tk.IntVar()
        self.scat_type = tk.StringVar()
        self.scat_color_list = ['']
        self.scat_size_list = ['']
        self.scat_color = tk.StringVar()
        self.scat_size = tk.StringVar()
        self.scat_faces = ['none', 'face', 'blue', 'green',
                           'red', 'cyan', 'magenta', 'yellow',
                           'black', 'white']
        self.scat_edge = tk.StringVar()
        self.scat_alpha = tk.DoubleVar()
        self.cmap_list = ['viridis', 'plasma', 'inferno', 'magma', 'ocean',
                          'gist_earth', 'terrain', 'gist_stern', 'gnuplot',
                          'gnuplot2', 'CMRmap', 'cubehelix', 'brg', 'hsv',
                          'gist_rainbow', 'rainbow', 'jet', 'nipy_spectral',
                          'gist_ncar', 'Greys', 'Purples', 'Blues', 'Greens',
                          'Oranges', 'Reds', 'YlOrBr', 'YlOrRd', 'OrRd',
                          'PuRd', 'RdPu', 'BuPu', 'GnBu', 'PuBu', 'YlGnBu',
                          'PuBuGn', 'BuGn', 'YlGn', 'binary', 'gist_yarg',
                          'gist_gray', 'gray', 'bone', 'pink', 'spring',
                          'summer', 'autumn', 'winter', 'cool', 'Wistia',
                          'hot', 'afmhot', 'gist_heat', 'copper']
        self.cb_exist = tk.IntVar()
        self.cmap_pick = tk.StringVar()
        self.cmap_pick.set('viridis')
        self.gridrow = tk.IntVar()
        self.gridcol = tk.IntVar()
        self.sharex = tk.IntVar()
        self.sharey = tk.IntVar()
        self.alldat_selected = tk.StringVar()
        self.seldat_selected = tk.StringVar()
        self.selected_axis_data = ['']
        self.current_axis = tk.StringVar()
        self.axrow = tk.IntVar()
        self.axcol = tk.IntVar()
        self.axrowspan = tk.IntVar()
        self.axcolspan = tk.IntVar()
        self.xlab = tk.StringVar()
        self.ylab = tk.StringVar()
        self.axsize = tk.DoubleVar()
        self.xlimlow = tk.DoubleVar()
        self.xlimhi = tk.DoubleVar()
        self.xticks = tk.IntVar()
        self.xlog = tk.IntVar()
        self.ylimlow = tk.DoubleVar()
        self.ylimhi = tk.DoubleVar()
        self.yticks = tk.IntVar()
        self.ylog = tk.IntVar()
        self.axbold = tk.IntVar()
        self.axitalic = tk.IntVar()
        self.title = tk.StringVar()
        self.tsize = tk.DoubleVar()
        self.tbold = tk.IntVar()
        self.titalic = tk.IntVar()
        self.legend = tk.StringVar()
        self.lgSize = tk.DoubleVar()
        self.legend_pos_list = ['best', 'None', 'upper left', 'upper center',
                                'upper right', 'center left', 'center',
                                'center right', 'lower left', 'lower center',
                                'lower right']
        # Call the function to obtain the initial values for all the variables
        # defined above and set the axis count to 1 since this will create the
        # first axis
        self.populate_variables()
        self.axis_count = 1
        # Create the Grid object for the layout of the window
        self.grid()
        # populate the window with the widgets
        self.create_widgets()

    def create_widgets(self):
        #************************************************************#
        #************************************************************#
        # Create a frame to hold the plot details information
        self.plotsFrame = tk.LabelFrame(self, text='Plot Details',
                                        labelanchor='nw', height='100',
                                        width='400', bg=BG_BLUE,
                                        font=('Courier New', '12', 'bold'))
        self.plotsFrame.grid(row=0, column=0, columnspan=3, rowspan=2,
                             padx=10, pady=4, sticky=tk.W+tk.E)

        #************************************************************#
        #************************************************************#
        self.data_sel_frame = tk.Frame(self.plotsFrame, bg=BG_BLUE)
        self.data_sel_frame.grid(row=0, column=0, rowspan=2)

        # Option menu for selecting the current set of data
        self.data_select = tk.OptionMenu(self.data_sel_frame, self.current_data,
                                         *self.data_list,
                                         command=self.plot_changed)
        self.data_select['bg'] = BG_BLUE
        self.data_select['activebackground'] = BG_BLUE
        self.data_select['width'] = '20'
        self.data_select['height'] = '1'
        self.data_select['borderwidth'] = '1'
        self.data_select['pady'] = '1'
        self.data_select['padx'] = '2'
        self.data_select['relief'] = tk.RAISED
        self.data_select['anchor'] = tk.W
        self.data_select['highlightthickness'] = '0'
        self.data_select.grid(row=0, column=0, columnspan=3, sticky=tk.W+tk.E,
                              padx=1)

        self.label = tk.Label(self.data_sel_frame, text='Multiple:', bg=BG_BLUE,
                              font=('Courier New', '10', 'bold'))
        self.label.grid(row=1, column=0)
        self.multi_select_check = tk.Checkbutton(self.data_sel_frame,
                                                 variable=self.multi_select,
                                                 bg=BG_BLUE,
                                                 activebackground=BG_BLUE,
                                                 command=self.multi_select_finish)
        self.multi_select_check.grid(row=1, column=1)
        self.multi_clear = tk.Button(self.data_sel_frame,
                                     bg=BG_BLUE, text='Clear Selection',
                                     activebackground=BG_BLUE,
                                     font=('Courier New', '10', 'bold'),
                                     command=self.clear_multi_choice)
        self.multi_clear.grid(row=1, column=2, pady=3, padx=1)

        self.selection_list = tk.Listbox(self.data_sel_frame,
                                         exportselection=0,
                                         listvariable=self.multi_list,
                                         selectmode=tk.MULTIPLE,
                                         activestyle='none')
        self.selection_list.grid(row=2, column=0, columnspan=3, sticky=tk.W+tk.E,
                                 padx=1, pady=3)

        # New frame for Data Labels
        self.data_labels_frame = tk.Frame(self.plotsFrame, bg=BG_BLUE)
        self.data_labels_frame.grid(row=0, column=1)

        # Input EntryBox for Data Label
        self.label = tk.Label(self.data_labels_frame, text='Data Label:', bg=BG_BLUE,
                              font=('Courier New', '10', 'bold'))
        self.label.grid(row=0, column=2, columnspan=2, padx=5)
        self.data_label = tk.Entry(self.data_labels_frame, textvariable=self.dat_lab,
                                   width='50')
        self.data_label.grid(row=0, column=4, columnspan=2, padx=5)
        # Input EntryBox for the Fill data Label
        self.label = tk.Label(self.data_labels_frame, text='Fill Label:', bg=BG_BLUE,
                              font=('Courier New', '10', 'bold'))
        self.label.grid(row=0, column=6, columnspan=2, padx=5)
        self.data_label = tk.Entry(self.data_labels_frame, textvariable=self.dat_lab2,
                                   width='50')
        self.data_label.grid(row=0, column=8, columnspan=2, padx=5)
        #************************************************************#
        #************************************************************#
        self.plot_options_frame = tk.Frame(self.plotsFrame, bg=BG_BLUE)
        self.plot_options_frame.grid(row=1, column=1)

        # Window Frame for the Errorbar Data
        self.ebar_dat = tk.LabelFrame(self.plot_options_frame, text='Error Bar',
                                      labelanchor='n', bg=BG_BLUE,
                                      font=('Courier New', '11', 'bold'),
                                      height=200, width=160)
        self.ebar_dat.grid(row=0, column=0, columnspan=2, padx=1)
        self.ebar_dat.grid_propagate(0)
        # CheckBox for whether to show errobars
        self.label = tk.Label(self.ebar_dat, text='Error Bar?:', bg=BG_BLUE,
                              font=('Courier New', '10', 'bold'))
        self.label.grid(row=0, column=0, padx=5, pady=2)
        self.ebar_exist_check = tk.Checkbutton(self.ebar_dat,
                                               variable=self.ebar_exist,
                                               bg=BG_BLUE,
                                               activebackground=BG_BLUE,
                                               command=self.other_plot_select)
        self.ebar_exist_check.grid(row=0, column=1, padx=5, pady=2)
        # Errorbar color selection
        self.label = tk.Label(self.ebar_dat, text='Color:', bg=BG_BLUE,
                              font=('Courier New', '10', 'bold'))
        self.label.grid(row=1, column=0, padx=5, pady=2)
        self.eb_col = tk.Button(self.ebar_dat, text='',
                                bg=self.ebar_color.get(),
                                activebackground=self.ebar_color.get(),
                                font=('Courier New', '10', 'bold'),
                                command=self.ebar_col_h)
        self.eb_col.grid(row=1, column=1, padx=5, pady=2, sticky=tk.W+tk.E)
        # Errorbar linewidth
        self.label = tk.Label(self.ebar_dat, text='Width:', bg=BG_BLUE,
                              font=('Courier New', '10', 'bold'))
        self.label.grid(row=2, column=0, padx=5, pady=2)
        self.eb_lw = tk.Spinbox(self.ebar_dat, textvariable=self.ebar_linew,
                                width='5', from_=1, to=100, increment=1)
        self.eb_lw.grid(row=2, column=1, padx=5, pady=2)

        self.label = tk.Label(self.ebar_dat, text='Error Bar Cap:', bg=BG_BLUE,
                              font=('Courier New', '10', 'underline'))
        self.label.grid(row=3, column=0, columnspan=2, padx=5, pady=2)

        # Errorbar Cap Size
        self.label = tk.Label(self.ebar_dat, text='Size:', bg=BG_BLUE,
                              font=('Courier New', '10', 'bold'))
        self.label.grid(row=4, column=0, padx=5, pady=2)
        self.eb_cs = tk.Spinbox(self.ebar_dat, textvariable=self.ebar_caps,
                                width='5', from_=1, to=100, increment=1)
        self.eb_cs.grid(row=4, column=1, padx=5, pady=2)
        # Errorbar Cap Thickness
        self.label = tk.Label(self.ebar_dat, text='Thickness:', bg=BG_BLUE,
                              font=('Courier New', '10', 'bold'))
        self.label.grid(row=5, column=0, padx=5, pady=2)
        self.eb_ct = tk.Spinbox(self.ebar_dat, textvariable=self.ebar_capt,
                                width='5', from_=1, to=100, increment=1)
        self.eb_ct.grid(row=5, column=1, padx=5, pady=2)
        #************************************************************#
        #************************************************************#

        self.line_dat = tk.LabelFrame(self.plot_options_frame, text='Line',
                                      labelanchor='n', bg=BG_BLUE,
                                      font=('Courier New', '11', 'bold'),
                                      height=200, width=135)
        self.line_dat.grid(row=0, column=2, columnspan=2, padx=1)
        self.line_dat.grid_propagate(0)

        self.label = tk.Label(self.line_dat, text='Line?:', bg=BG_BLUE,
                              font=('Courier New', '10', 'bold'))
        self.label.grid(row=0, column=0, padx=5, pady=2)

        self.line_exist_check = tk.Checkbutton(self.line_dat,
                                               variable=self.line_exist,
                                               bg=BG_BLUE,
                                               activebackground=BG_BLUE,
                                               command=self.other_plot_select)
        self.line_exist_check.grid(row=0, column=1, padx=5, pady=2)

        self.label = tk.Label(self.line_dat, text='Color:', bg=BG_BLUE,
                              font=('Courier New', '10', 'bold'))
        self.label.grid(row=1, column=0, padx=5, pady=2)
        self.l_col = tk.Button(self.line_dat, text='',
                               bg=self.line_color.get(),
                               activebackground=self.line_color.get(),
                               font=('Courier New', '10', 'bold'),
                               command=self.line_col_h)
        self.l_col.grid(row=1, column=1, padx=5, pady=2, sticky=tk.W+tk.E)

        self.label = tk.Label(self.line_dat, text='Style:', bg=BG_BLUE,
                              font=('Courier New', '10', 'bold'))
        self.label.grid(row=2, column=0, padx=5, pady=2)
        self.l_sty = tk.OptionMenu(self.line_dat, self.line_style,
                                   *self.styles)
        self.l_sty['bg'] = BG_BLUE
        self.l_sty['activebackground'] = BG_BLUE
        self.l_sty['width'] = '3'
        self.l_sty['height'] = '1'
        self.l_sty['borderwidth'] = '1'
        self.l_sty['pady'] = '1'
        self.l_sty['padx'] = '2'
        self.l_sty['relief'] = tk.RAISED
        self.l_sty['anchor'] = tk.W
        self.l_sty['highlightthickness'] = '0'
        self.l_sty.grid(row=2, column=1, padx=5, pady=2)

        self.label = tk.Label(self.line_dat, text='Width:', bg=BG_BLUE,
                              font=('Courier New', '10', 'bold'))
        self.label.grid(row=3, column=0, padx=5, pady=2)
        self.l_wid = tk.Spinbox(self.line_dat, textvariable=self.line_width,
                                width='5', from_=1, to=100, increment=1)
        self.l_wid.grid(row=3, column=1, padx=5, pady=2)
        
        self.label = tk.Label(self.line_dat, text='Alpha:', bg=BG_BLUE,
                              font=('Courier New', '10', 'bold'))
        self.label.grid(row=4, column=0)

        self.l_alpha_choice = tk.Spinbox(self.line_dat, textvariable=self.line_alpha,
                                     width='4', from_=0, to=1, increment=0.01)
        self.l_alpha_choice.grid(row=4, column=1, padx=2, pady=1)



        #************************************************************#
        #************************************************************#
        self.marker_dat = tk.LabelFrame(self.plot_options_frame, text='Marker',
                                        labelanchor='n', bg=BG_BLUE,
                                        font=('Courier New', '11', 'bold'),
                                        height=200, width=160)
        self.marker_dat.grid(row=0, column=4, columnspan=2, padx=1)
        self.marker_dat.grid_propagate(0)

        self.label = tk.Label(self.marker_dat, text='Marker?:', bg=BG_BLUE,
                              font=('Courier New', '10', 'bold'))
        self.label.grid(row=0, column=0, padx=5, pady=2)

        self.mark_exist_check = tk.Checkbutton(self.marker_dat,
                                               variable=self.mark_exist,
                                               bg=BG_BLUE,
                                               activebackground=BG_BLUE,
                                               command=self.other_plot_select)
        self.mark_exist_check.grid(row=0, column=1, padx=5, pady=2)

        self.label = tk.Label(self.marker_dat, text='Type:', bg=BG_BLUE,
                              font=('Courier New', '10', 'bold'))
        self.label.grid(row=1, column=0)
        self.m_type = tk.OptionMenu(self.marker_dat, self.mark_type,
                                    *self.marker_types)
        self.m_type['bg'] = BG_BLUE
        self.m_type['activebackground'] = BG_BLUE
        self.m_type['width'] = '3'
        self.m_type['height'] = '1'
        self.m_type['borderwidth'] = '1'
        self.m_type['pady'] = '1'
        self.m_type['padx'] = '2'
        self.m_type['relief'] = tk.RAISED
        self.m_type['anchor'] = tk.W
        self.m_type['highlightthickness'] = '0'
        self.m_type.grid(row=1, column=1, padx=5, pady=2)


        self.label = tk.Label(self.marker_dat, text='Edge Color:', bg=BG_BLUE,
                              font=('Courier New', '10', 'bold'))
        self.label.grid(row=2, column=0)
        self.m_ecol = tk.Button(self.marker_dat, text='',
                                bg=self.mark_ec.get(),
                                activebackground=self.mark_ec.get(),
                                font=('Courier New', '10', 'bold'),
                                command=self.me_col_h)
        self.m_ecol.grid(row=2, column=1, padx=5, pady=2, sticky=tk.W+tk.E)

        self.label = tk.Label(self.marker_dat, text='Edge Width:', bg=BG_BLUE,
                              font=('Courier New', '10', 'bold'))
        self.label.grid(row=3, column=0)
        self.m_ewid = tk.Spinbox(self.marker_dat, textvariable=self.mark_ew,
                                 width='5', from_=1, to=100, increment=1)
        self.m_ewid.grid(row=3, column=1, padx=5, pady=2)

        self.label = tk.Label(self.marker_dat, text='Face Color:', bg=BG_BLUE,
                              font=('Courier New', '10', 'bold'))
        self.label.grid(row=4, column=0)
        self.m_fcol = tk.Button(self.marker_dat, text='',
                                bg=self.mark_fc.get(),
                                activebackground=self.mark_fc.get(),
                                font=('Courier New', '10', 'bold'),
                                command=self.mf_col_h)
        self.m_fcol.grid(row=4, column=1, padx=5, pady=2, sticky=tk.W+tk.E)

        self.label = tk.Label(self.marker_dat, text='Size:', bg=BG_BLUE,
                              font=('Courier New', '10', 'bold'))
        self.label.grid(row=5, column=0)
        self.m_sz = tk.Spinbox(self.marker_dat, textvariable=self.mark_sz,
                               width='5', from_=1, to=1000, increment=1)
        self.m_sz.grid(row=5, column=1, padx=5, pady=2)


        #************************************************************#
        #************************************************************#
        self.fill_dat = tk.LabelFrame(self.plot_options_frame, text='Fill',
                                      labelanchor='n', bg=BG_BLUE,
                                      font=('Courier New', '11', 'bold'),
                                      height=200, width=160)
        self.fill_dat.grid(row=0, column=6, columnspan=2, padx=1)
        self.fill_dat.grid_propagate(0)

        self.label = tk.Label(self.fill_dat, text='Fill?:', bg=BG_BLUE,
                              font=('Courier New', '10', 'bold'))
        self.label.grid(row=0, column=0)
        self.fill_exist_check = tk.Checkbutton(self.fill_dat,
                                               variable=self.fill_exist,
                                               bg=BG_BLUE,
                                               activebackground=BG_BLUE,
                                               command=self.other_plot_select)
        self.fill_exist_check.grid(row=0, column=1, padx=5, pady=2)

        self.label = tk.Label(self.fill_dat, text='Alpha:', bg=BG_BLUE,
                              font=('Courier New', '10', 'bold'))
        self.label.grid(row=1, column=0)
        self.f_alpha = tk.Spinbox(self.fill_dat, textvariable=self.fill_alpha,
                                  width='5', from_=0, to=1, increment=0.01)
        self.f_alpha.grid(row=1, column=1, padx=5, pady=2)

        self.label = tk.Label(self.fill_dat, text='Face Color:', bg=BG_BLUE,
                              font=('Courier New', '10', 'bold'))
        self.label.grid(row=2, column=0)
        self.f_fcol = tk.Button(self.fill_dat, text='', bg=self.fill_fc.get(),
                                activebackground=self.fill_fc.get(),
                                font=('Courier New', '10', 'bold'),
                                command=self.ff_col_h)
        self.f_fcol.grid(row=2, column=1, padx=5, pady=2, sticky=tk.W+tk.E)

        self.label = tk.Label(self.fill_dat, text='Edge Color:', bg=BG_BLUE,
                              font=('Courier New', '10', 'bold'))
        self.label.grid(row=3, column=0)
        self.f_ecol = tk.Button(self.fill_dat, text='', bg=self.fill_ec.get(),
                                activebackground=self.fill_ec.get(),
                                font=('Courier New', '10', 'bold'),
                                command=self.fe_col_h)
        self.f_ecol.grid(row=3, column=1, padx=5, pady=2, sticky=tk.W+tk.E)


        self.label = tk.Label(self.fill_dat, text='Edge Width:', bg=BG_BLUE,
                              font=('Courier New', '10', 'bold'))
        self.label.grid(row=4, column=0)
        self.f_linew = tk.Spinbox(self.fill_dat, textvariable=self.fill_linew,
                                  width='5', from_=0, to=100, increment=1)
        self.f_linew.grid(row=4, column=1, padx=5, pady=2)

        self.label = tk.Label(self.fill_dat, text='Edge Style:', bg=BG_BLUE,
                              font=('Courier New', '10', 'bold'))
        self.label.grid(row=5, column=0)
        self.f_ls = tk.OptionMenu(self.fill_dat, self.fill_lines, *self.styles)
        self.f_ls['bg'] = BG_BLUE
        self.f_ls['activebackground'] = BG_BLUE
        self.f_ls['width'] = '3'
        self.f_ls['height'] = '1'
        self.f_ls['borderwidth'] = '1'
        self.f_ls['pady'] = '1'
        self.f_ls['padx'] = '2'
        self.f_ls['relief'] = tk.RAISED
        self.f_ls['anchor'] = tk.W
        self.f_ls['highlightthickness'] = '0'
        self.f_ls.grid(row=5, column=1, padx=5, pady=2)

        #************************************************************#
        #************************************************************#
        # Create a frame to hold the scatter information
        self.scatter_dat = tk.LabelFrame(self.plot_options_frame, text='Scatter Plot',
                                         labelanchor='n', bg=BG_BLUE,
                                         font=('Courier New', '11', 'bold'),
                                         height=200, width=240)
        self.scatter_dat.grid(row=0, column=8, columnspan=2, padx=1)
        self.scatter_dat.grid_propagate(0)
        self.label = tk.Label(self.scatter_dat, text='Scatter?:', bg=BG_BLUE,
                              font=('Courier New', '10', 'bold'))
        self.label.grid(row=0, column=0)
        self.scat_exist_check = tk.Checkbutton(self.scatter_dat,
                                               variable=self.scat_exist,
                                               bg=BG_BLUE,
                                               activebackground=BG_BLUE,
                                               command=self.scatter_select)
        self.scat_exist_check.grid(row=0, column=1, padx=5, pady=2)

        self.label = tk.Label(self.scatter_dat, text='Marker:', bg=BG_BLUE,
                              font=('Courier New', '10', 'bold'))
        self.label.grid(row=1, column=0)

        self.scatter_type = tk.OptionMenu(self.scatter_dat, self.scat_type,
                                          *self.marker_types)
        self.scatter_type['bg'] = BG_BLUE
        self.scatter_type['activebackground'] = BG_BLUE
        self.scatter_type['width'] = '3'
        self.scatter_type['height'] = '1'
        self.scatter_type['borderwidth'] = '1'
        self.scatter_type['pady'] = '1'
        self.scatter_type['padx'] = '2'
        self.scatter_type['relief'] = tk.RAISED
        self.scatter_type['anchor'] = tk.W
        self.scatter_type['highlightthickness'] = '0'
        self.scatter_type.grid(row=1, column=1, padx=5, pady=2)

        self.scatter_edge = tk.OptionMenu(self.scatter_dat, self.scat_edge,
                                          *self.scat_faces)
        self.scatter_edge['bg'] = BG_BLUE
        self.scatter_edge['activebackground'] = BG_BLUE
        self.scatter_edge['width'] = '5'
        self.scatter_edge['height'] = '1'
        self.scatter_edge['borderwidth'] = '1'
        self.scatter_edge['pady'] = '1'
        self.scatter_edge['padx'] = '2'
        self.scatter_edge['relief'] = tk.RAISED
        self.scatter_edge['anchor'] = tk.W
        self.scatter_edge['highlightthickness'] = '0'
        self.scatter_edge.grid(row=1, column=2, padx=5, pady=2)

        self.label = tk.Label(self.scatter_dat, text='Alpha:', bg=BG_BLUE,
                              font=('Courier New', '10', 'bold'))
        self.label.grid(row=2, column=0)

        self.scat_alpha_choice = tk.Spinbox(self.scatter_dat, textvariable=self.scat_alpha,
                                     width='4', from_=0, to=1, increment=0.01)
        self.scat_alpha_choice.grid(row=2, column=1, padx=2, pady=1)

        self.label = tk.Label(self.scatter_dat, text='Color:', bg=BG_BLUE,
                              font=('Courier New', '10', 'bold'))
        self.label.grid(row=3, column=0)

        self.scatter_color = tk.OptionMenu(self.scatter_dat, self.scat_color,
                                           *self.scat_color_list)
        self.scatter_color['bg'] = BG_BLUE
        self.scatter_color['activebackground'] = BG_BLUE
        self.scatter_color['width'] = '17'
        self.scatter_color['height'] = '1'
        self.scatter_color['borderwidth'] = '1'
        self.scatter_color['pady'] = '1'
        self.scatter_color['padx'] = '2'
        self.scatter_color['relief'] = tk.RAISED
        self.scatter_color['anchor'] = tk.W
        self.scatter_color['highlightthickness'] = '0'
        self.scatter_color.grid(row=3, column=1, columnspan=2, padx=5, pady=2)

        self.label = tk.Label(self.scatter_dat, text='Size:', bg=BG_BLUE,
                              font=('Courier New', '10', 'bold'))
        self.label.grid(row=4, column=0)

        self.scatter_size = tk.OptionMenu(self.scatter_dat, self.scat_size,
                                          *self.scat_size_list)
        self.scatter_size['bg'] = BG_BLUE
        self.scatter_size['activebackground'] = BG_BLUE
        self.scatter_size['width'] = '17'
        self.scatter_size['height'] = '1'
        self.scatter_size['borderwidth'] = '1'
        self.scatter_size['pady'] = '1'
        self.scatter_size['padx'] = '2'
        self.scatter_size['relief'] = tk.RAISED
        self.scatter_size['anchor'] = tk.W
        self.scatter_size['highlightthickness'] = '0'
        self.scatter_size.grid(row=4, column=1, columnspan=2, padx=5, pady=2)

        self.label = tk.Label(self.scatter_dat, text='Color Bar?:', bg=BG_BLUE,
                              font=('Courier New', '10', 'bold'))
        self.label.grid(row=5, column=0)
        self.cb_exist_check = tk.Checkbutton(self.scatter_dat,
                                             variable=self.cb_exist,
                                             bg=BG_BLUE,
                                             activebackground=BG_BLUE)
        self.cb_exist_check.grid(row=5, column=1, padx=5, pady=2)

        self.label = tk.Label(self.scatter_dat, text='Color Map:', bg=BG_BLUE,
                              font=('Courier New', '10', 'bold'))
        self.label.grid(row=6, column=0)

        self.color_map = tk.OptionMenu(self.scatter_dat, self.cmap_pick,
                                          *self.cmap_list)
        self.color_map['bg'] = BG_BLUE
        self.color_map['activebackground'] = BG_BLUE
        self.color_map['width'] = '17'
        self.color_map['height'] = '1'
        self.color_map['borderwidth'] = '1'
        self.color_map['pady'] = '1'
        self.color_map['padx'] = '2'
        self.color_map['relief'] = tk.RAISED
        self.color_map['anchor'] = tk.W
        self.color_map['highlightthickness'] = '0'
        self.color_map.grid(row=6, column=1, columnspan=2, padx=5, pady=2)

        #************************************************************#
        #************************************************************#
        # Create a frame to hold the axis details information
        self.axisFrame = tk.LabelFrame(self, text='Axis Details',
                                       labelanchor='nw', height='100',
                                       width='400', bg=BG_BLUE,
                                       font=('Courier New', '12', 'bold'))
        self.axisFrame.grid(row=2, column=0, columnspan=3, rowspan=2,
                            padx=10, pady=4)


        #************************************************************#
        #************************************************************#
        # Create the frame to specify the grid size
        self.gridFrame = tk.LabelFrame(self.axisFrame, text='Grid Size',
                                       labelanchor='n',
                                       font=('Courier New', '12', 'bold'),
                                       bg=BG_BLUE)
        self.gridFrame.grid(row=0, column=0, columnspan=2, padx=5, pady=5,
                            sticky=tk.W+tk.E)
        self.label = tk.Label(self.gridFrame, text='Rows:',
                              font=('Courier New', '10'), bg=BG_BLUE)
        self.label.grid(row=0, column=0, padx=2, pady=1)
        self.gridrEntry = tk.Spinbox(self.gridFrame, textvariable=self.gridrow,
                                     width='4', from_=1, to=100, increment=1)
        self.gridrEntry.grid(row=0, column=1, padx=2, pady=1)
        self.label = tk.Label(self.gridFrame, text='Columns:',
                              font=('Courier New', '10'), bg=BG_BLUE)
        self.label.grid(row=0, column=2, padx=2, pady=1)
        self.gridcEntry = tk.Spinbox(self.gridFrame, textvariable=self.gridcol,
                                     width='4', from_=1, to=100, increment=1)
        self.gridcEntry.grid(row=0, column=3, padx=2, pady=1)
        self.label = tk.Label(self.gridFrame, text='Share x:',
                              font=('Courier New', '10'), bg=BG_BLUE)
        self.label.grid(row=1, column=0, padx=2, pady=1)
        self.sharex_check = tk.Checkbutton(self.gridFrame,
                                           variable=self.sharex, bg=BG_BLUE,
                                           activebackground=BG_BLUE)
        self.sharex_check.grid(row=1, column=1, padx=5, pady=2)
        self.label = tk.Label(self.gridFrame, text='Share y:',
                              font=('Courier New', '10'), bg=BG_BLUE)
        self.label.grid(row=1, column=2, padx=2, pady=1)
        self.sharey_check = tk.Checkbutton(self.gridFrame,
                                           variable=self.sharey,
                                           bg=BG_BLUE,
                                           activebackground=BG_BLUE)
        self.sharey_check.grid(row=1, column=3, padx=5, pady=2)

        #************************************************************#
        #************************************************************#
        # Create button for adding a new axis to the plot
        self.createFrame = tk.LabelFrame(self.axisFrame,
                                         text='Create or Delete Axes',
                                         labelanchor='n',
                                         font=('Courier New', '12', 'bold'),
                                         bg=BG_BLUE)
        self.createFrame.grid(row=0, column=2, columnspan=2, padx=5, pady=5,
                              sticky=tk.W+tk.E)

        self.addnewAxis = tk.Button(self.createFrame, text='Add Axis',
                                    font=('Courier New', '10', 'bold'),
                                    bg=BG_GREEN, activebackground=BG_GREEN,
                                    command=self.add_new_axis)
        self.addnewAxis.grid(row=0, column=0, sticky=tk.W+tk.E, padx=5, pady=5)

        self.axis_select = tk.OptionMenu(self.createFrame, self.current_axis,
                                         *self.axis_list,
                                         command=self.axis_changed)
        self.axis_select['bg'] = BG_BLUE
        self.axis_select['activebackground'] = BG_BLUE
        self.axis_select['width'] = '10'
        self.axis_select['height'] = '2'
        self.axis_select['borderwidth'] = '1'
        self.axis_select['pady'] = '1'
        self.axis_select['padx'] = '2'
        self.axis_select['relief'] = tk.RAISED
        self.axis_select['anchor'] = tk.W
        self.axis_select['highlightthickness'] = '0'
        self.axis_select.grid(row=0, column=1, sticky=tk.W+tk.E)

        self.delAxis = tk.Button(self.createFrame, text='Delete Axis',
                                 font=('Courier New', '10', 'bold'), bg=BG_RED,
                                 activebackground=BG_RED,
                                 command=self.del_curr_axis)
        self.delAxis.grid(row=0, column=2, sticky=tk.W+tk.E, padx=8, pady=6)

        #************************************************************#
        #************************************************************#
        # Create Frame for data selection for the axis
        self.selDataFrame = tk.LabelFrame(self.axisFrame,
                                          text='Data Selection',
                                          labelanchor='n',
                                          font=('Courier New', '12', 'bold'),
                                          bg=BG_BLUE, width=500, height=100)
        self.selDataFrame.grid(row=0, column=4, columnspan=2, padx=5, pady=5,
                               sticky=tk.W+tk.E)

        self.label = tk.Label(self.selDataFrame, text='All Data', bg=BG_BLUE,
                              font=('Courier New', '10', 'bold'))
        self.label.grid(row=0, column=0, sticky=tk.W+tk.E)

        self.label = tk.Label(self.selDataFrame, text='Selected Data',
                              bg=BG_BLUE, font=('Courier New', '10', 'bold'))
        self.label.grid(row=0, column=2, sticky=tk.W+tk.E)

        self.alldat = tk.OptionMenu(self.selDataFrame, self.alldat_selected,
                                    *self.data_list)
        self.alldat['bg'] = BG_BLUE
        self.alldat['activebackground'] = BG_BLUE
        self.alldat['width'] = '10'
        self.alldat['height'] = '1'
        self.alldat['borderwidth'] = '1'
        self.alldat['pady'] = '1'
        self.alldat['padx'] = '2'
        self.alldat['relief'] = tk.RAISED
        self.alldat['anchor'] = tk.W
        self.alldat['highlightthickness'] = '0'
        self.alldat.grid(row=1, column=0, padx=5)

        self.add_dat = tk.Button(self.selDataFrame, text='>', bg=BG_GREEN,
                                 activebackground=BG_GREEN,
                                 command=self.add_plot_to_axis)
        self.add_dat.grid(row=1, column=1)

        self.rem_dat = tk.Button(self.selDataFrame, text='<', bg=BG_RED,
                                 activebackground=BG_RED,
                                 command=self.remove_plot_from_axis)
        self.rem_dat.grid(row=1, column=3)

        self.seldat = tk.OptionMenu(self.selDataFrame, self.seldat_selected,
                                    *self.selected_axis_data)
        self.seldat['bg'] = BG_BLUE
        self.seldat['activebackground'] = BG_BLUE
        self.seldat['width'] = '10'
        self.seldat['height'] = '1'
        self.seldat['borderwidth'] = '1'
        self.seldat['pady'] = '1'
        self.seldat['padx'] = '2'
        self.seldat['relief'] = tk.RAISED
        self.seldat['anchor'] = tk.W
        self.seldat['highlightthickness'] = '0'
        self.seldat.grid(row=1, column=2, padx=5)


        #************************************************************#
        #************************************************************#
        # Create Frame for data position for the axis
        self.axPosFrame = tk.LabelFrame(self.axisFrame, text='Axis Position',
                                        labelanchor='n',
                                        font=('Courier New', '12', 'bold'), bg=BG_BLUE,
                                        width=500, height=100)
        self.axPosFrame.grid(row=0, column=6, columnspan=2, padx=5, pady=5,
                             sticky=tk.W+tk.E)

        self.label = tk.Label(self.axPosFrame, text='Row:',
                              font=('Courier New', '10', 'bold'), bg=BG_BLUE)
        self.label.grid(row=0, column=0)
        self.axrow_sb = tk.Spinbox(self.axPosFrame, textvariable=self.axrow,
                                   width='4', from_=0, to=100, increment=1)
        self.axrow_sb.grid(row=0, column=1, padx=2, pady=1)
        self.label = tk.Label(self.axPosFrame, text='Row Span:',
                              font=('Courier New', '10', 'bold'), bg=BG_BLUE)
        self.label.grid(row=0, column=2)
        self.axrowspan_sb = tk.Spinbox(self.axPosFrame,
                                       textvariable=self.axrowspan, width='4',
                                       from_=1, to=100, increment=1)
        self.axrowspan_sb.grid(row=0, column=3, padx=2, pady=1)

        self.label = tk.Label(self.axPosFrame, text='Column:',
                              font=('Courier New', '10', 'bold'), bg=BG_BLUE)
        self.label.grid(row=1, column=0)
        self.axcol_sb = tk.Spinbox(self.axPosFrame, textvariable=self.axcol,
                                   width='4', from_=0, to=100, increment=1)
        self.axcol_sb.grid(row=1, column=1, padx=2, pady=1)
        self.label = tk.Label(self.axPosFrame, text='Column Span:',
                              font=('Courier New', '10', 'bold'), bg=BG_BLUE)
        self.label.grid(row=1, column=2)
        self.axcolspan_sb = tk.Spinbox(self.axPosFrame,
                                       textvariable=self.axcolspan, width='4',
                                       from_=1, to=100, increment=1)
        self.axcolspan_sb.grid(row=1, column=3, padx=2, pady=1)

        #************************************************************#
        #************************************************************#
        # create the frame that will hold the information for the axis labels
        self.axlabFrame = tk.LabelFrame(self.axisFrame, text='Axis Labels',
                                        labelanchor='n', height='100',
                                        width='200', bg=BG_BLUE,
                                        font=('Courier New', '12', 'bold'))
        self.axlabFrame.grid(row=1, column=0, columnspan=4, rowspan=3, padx=5,
                             pady=5, sticky=tk.W+tk.E)

        # Create a text field for the x-axis title
        self.label = tk.Label(self.axlabFrame, text='X-Axis: Label:',
                              font=('Courier New', '10'), bg=BG_BLUE)
        self.label.grid(row=0, column=0, padx=2, pady=1)
        self.xlabEntry = tk.Entry(self.axlabFrame, textvariable=self.xlab,
                                  width='71')
        self.xlabEntry.grid(row=0, column=1, columnspan=7, padx=2, pady=1)
        # Create a text field for entering the lower x_limit
        self.label = tk.Label(self.axlabFrame, text='Lower Limit:',
                              font=('Courier New', '10'), bg=BG_BLUE)
        self.label.grid(row=1, column=0, padx=2, pady=1)
        self.xlimloEntry = tk.Entry(self.axlabFrame, textvariable=self.xlimlow,
                                    width='5')
        self.xlimloEntry.grid(row=1, column=1, padx=2, pady=1)
        # Create a text field for entering the upper x_limit
        self.label = tk.Label(self.axlabFrame, text='Upper Limit:',
                              font=('Courier New', '10'), bg=BG_BLUE)
        self.label.grid(row=1, column=2, padx=2, pady=1)
        self.xlimhiEntry = tk.Entry(self.axlabFrame, textvariable=self.xlimhi,
                                    width='5')
        self.xlimhiEntry.grid(row=1, column=3, padx=2, pady=1)
        # Create checkbox for axis ticks
        self.label = tk.Label(self.axlabFrame, text='Show ticks:',
                              font=('Courier New', '10'), bg=BG_BLUE)
        self.label.grid(row=1, column=4, padx=2, pady=1)
        self.xtickcheck = tk.Checkbutton(self.axlabFrame, variable=self.xticks,
                                         bg=BG_BLUE, activebackground=BG_BLUE)
        self.xtickcheck.grid(row=1, column=5, padx=2, pady=1)

        # Create checkbox for log scale
        self.label = tk.Label(self.axlabFrame, text='Log Scale:',
                              font=('Courier New', '10'), bg=BG_BLUE)
        self.label.grid(row=1, column=6, padx=2, pady=1)
        self.xlogscale = tk.Checkbutton(self.axlabFrame, variable=self.xlog,
                                        bg=BG_BLUE, activebackground=BG_BLUE)
        self.xlogscale.grid(row=1, column=7, padx=2, pady=1)

        # Create Textbox for the y-Axis label
        self.label = tk.Label(self.axlabFrame, text='Y-Axis: Label:',
                              font=('Courier New', '10'), bg=BG_BLUE)
        self.label.grid(row=2, column=0, padx=2, pady=1)
        self.ylabEntry = tk.Entry(self.axlabFrame, textvariable=self.ylab,
                                  width='71')
        self.ylabEntry.grid(row=2, column=1, columnspan=7, padx=2, pady=1)
        # Create entry for lower y-Limit
        self.label = tk.Label(self.axlabFrame, text='Lower Limit:',
                              font=('Courier New', '10'), bg=BG_BLUE)
        self.label.grid(row=3, column=0, padx=2, pady=1)
        self.ylimloEntry = tk.Entry(self.axlabFrame, textvariable=self.ylimlow,
                                    width='5')
        self.ylimloEntry.grid(row=3, column=1, padx=2, pady=1)
        # Create entry for upper y_limit
        self.label = tk.Label(self.axlabFrame, text='Upper Limit:',
                              font=('Courier New', '10'), bg=BG_BLUE)
        self.label.grid(row=3, column=2, padx=2, pady=1)
        self.ylimhiEntry = tk.Entry(self.axlabFrame, textvariable=self.ylimhi,
                                    width='5')
        self.ylimhiEntry.grid(row=3, column=3, padx=2, pady=1)
        # Create checkbox for axis ticks
        self.label = tk.Label(self.axlabFrame, text='Show ticks:',
                              font=('Courier New', '10'), bg=BG_BLUE)
        self.label.grid(row=3, column=4, padx=2, pady=1)
        self.xtickcheck = tk.Checkbutton(self.axlabFrame, variable=self.yticks,
                                         bg=BG_BLUE, activebackground=BG_BLUE)
        self.xtickcheck.grid(row=3, column=5, padx=2, pady=1)
        # Create checkbox for log scale
        self.label = tk.Label(self.axlabFrame, text='Log Scale:',
                              font=('Courier New', '10'), bg=BG_BLUE)
        self.label.grid(row=3, column=6, padx=2, pady=1)
        self.ylogscale = tk.Checkbutton(self.axlabFrame, variable=self.ylog,
                                        bg=BG_BLUE, activebackground=BG_BLUE)
        self.ylogscale.grid(row=3, column=7, padx=2, pady=1)

        # Create a Spinbox for the text size
        self.label = tk.Label(self.axlabFrame, text='Font Size:',
                              font=('Courier New', '10'), bg=BG_BLUE)
        self.label.grid(row=4, column=0, padx=2, pady=1)
        self.xlabSize = tk.Spinbox(self.axlabFrame, textvariable=self.axsize,
                                   width='4', from_=1, to=30, increment=0.5)
        self.xlabSize.grid(row=4, column=1)
        # Create a checkbutton for bold font
        self.label = tk.Label(self.axlabFrame, text='Bold:',
                              font=('Courier New', '10'), bg=BG_BLUE)
        self.label.grid(row=4, column=2, padx=2, pady=1)
        self.xboldselect = tk.Checkbutton(self.axlabFrame,
                                          variable=self.axbold, bg=BG_BLUE,
                                          activebackground=BG_BLUE)
        self.xboldselect.grid(row=4, column=3, padx=2, pady=1)
        # Create a checkbutton for italic font
        self.label = tk.Label(self.axlabFrame, text='Italic:',
                              font=('Courier New', '10'), bg=BG_BLUE)
        self.label.grid(row=4, column=4, padx=2, pady=1)
        self.xboldselect = tk.Checkbutton(self.axlabFrame,
                                          variable=self.axitalic, bg=BG_BLUE,
                                          activebackground=BG_BLUE)
        self.xboldselect.grid(row=4, column=5, padx=2, pady=1)

        #************************************************************#
        #************************************************************#
        # Create frame for the plot title information
        self.titFrame = tk.LabelFrame(self.axisFrame, text='Plot Title',
                                      labelanchor='n', height='100',
                                      width='200', bg=BG_BLUE,
                                      font=('Courier New', '12', 'bold'))
        self.titFrame.grid(row=1, column=4, columnspan=4, padx=5, pady=0,
                           sticky=tk.W+tk.E)

        # Create entry box for title
        self.label = tk.Label(self.titFrame, text='Label:',
                              font=('Courier New', '10'), bg=BG_BLUE)
        self.label.grid(row=0, column=0, padx=2, pady=1)
        self.titleEntry = tk.Entry(self.titFrame, textvariable=self.title,
                                   width='70')
        self.titleEntry.grid(row=0, column=1, padx=2, pady=1, columnspan=7)
        # Create spinbox for title size
        self.label = tk.Label(self.titFrame, text='Font Size:',
                              font=('Courier New', '10'), bg=BG_BLUE)
        self.label.grid(row=1, column=0, padx=2, pady=1)
        self.titleSize = tk.Spinbox(self.titFrame, textvariable=self.tsize,
                                    width=4, from_=1, to=30, increment=0.5)
        self.titleSize.grid(row=1, column=1)
        # Create select box for bold font
        self.label = tk.Label(self.titFrame, text='Bold:',
                              font=('Courier New', '10'), bg=BG_BLUE)
        self.label.grid(row=1, column=2, padx=2, pady=1)
        self.yboldselect = tk.Checkbutton(self.titFrame, variable=self.tbold,
                                          bg=BG_BLUE, activebackground=BG_BLUE)
        self.yboldselect.grid(row=1, column=3, padx=2, pady=1)
        # Create select box for italic font
        self.label = tk.Label(self.titFrame, text='Italic:',
                              font=('Courier New', '10'), bg=BG_BLUE)
        self.label.grid(row=1, column=4, padx=2, pady=1)
        self.yboldselect = tk.Checkbutton(self.titFrame, variable=self.titalic,
                                          bg=BG_BLUE, activebackground=BG_BLUE)
        self.yboldselect.grid(row=1, column=5, padx=2, pady=1)

        #************************************************************#
        #************************************************************#
        # Create frame for the legend position information
        self.legFrame = tk.LabelFrame(self.axisFrame, text='Legend',
                                      labelanchor='n', height='100',
                                      width='200', bg=BG_BLUE,
                                      font=('Courier New', '12', 'bold'))
        self.legFrame.grid(row=2, column=4, rowspan=2, columnspan=2, padx=5, pady=5,
                           sticky=tk.W+tk.E)

        self.label = tk.Label(self.legFrame, text='Position:',
                              font=('Courier New', '10', 'bold'), bg=BG_BLUE)
        self.label.grid(row=0, column=0, padx=2, pady=1, sticky=tk.W+tk.E)
        self.leg_pos = tk.OptionMenu(self.legFrame, self.legend,
                                     *self.legend_pos_list)
        self.leg_pos['bg'] = BG_BLUE
        self.leg_pos['activebackground'] = BG_BLUE
        self.leg_pos['width'] = '10'
        self.leg_pos['height'] = '1'
        self.leg_pos['borderwidth'] = '1'
        self.leg_pos['pady'] = '1'
        self.leg_pos['padx'] = '2'
        self.leg_pos['relief'] = tk.RAISED
        self.leg_pos['anchor'] = tk.W
        self.leg_pos['highlightthickness'] = '0'
        self.leg_pos.grid(row=1, column=0, padx=20, pady=5, sticky=tk.W+tk.E)

        self.label = tk.Label(self.legFrame, text='Font Size:',
                              font=('Courier New', '10', 'bold'), bg=BG_BLUE)
        self.label.grid(row=0, column=1, padx=2, pady=1, sticky=tk.W+tk.E)
        self.legSize = tk.Spinbox(self.legFrame, textvariable=self.lgSize,
                                  width=4, from_=1, to=30, increment=0.5)
        self.legSize.grid(row=1, column=1)


        #************************************************************#
        #************************************************************#
        # Create a button for showing the plot
        self.show_plot = tk.Button(self.axisFrame, text='---SHOW PLOT---',
                                   bg=BG_GREEN, activebackground=BG_GREEN,
                                   command=self.gen_plot)
        self.show_plot.grid(row=2, column=6, columnspan=2,
                            sticky=tk.W+tk.E+tk.N+tk.S, padx=30, pady=1)

        # Create a button for saving the plot
        self.save_plot_btn = tk.Button(self.axisFrame, text='---SAVE PLOT---',
                                       bg='#4E51B5', activebackground='#4E51B5',
                                       command=self.save_plot)
        self.save_plot_btn.grid(row=3, column=6, columnspan=2,
                                sticky=tk.W+tk.E+tk.N+tk.S, padx=30, pady=1)

    def populate_variables(self):
        self.data_list = list(self.data_dict.keys())
        self.add_first_axis()
        self.axis_list = list(self.axis_dict.keys())
        self.dat_lab.set(self.data_dict[self.data_list[0]]['label'])
        self.current_data.set(self.data_list[0])
        self.selected_data_value = self.current_data.get()
        self.selected_axis_value = 'axis1'

        self.ebar_exist.set(self.data_dict[self.data_list[0]]['ebar']['exist'])
        self.ebar_color.set(self.data_dict[self.data_list[0]]['ebar']['color'])
        self.ebar_linew.set(self.data_dict[self.data_list[0]]['ebar']['linew'])
        self.ebar_caps.set(self.data_dict[self.data_list[0]]['ebar']['capsize'])
        self.ebar_capt.set(self.data_dict[self.data_list[0]]['ebar']['capthick'])

        self.line_exist.set(self.data_dict[self.data_list[0]]['line']['exist'])
        self.line_color.set(self.data_dict[self.data_list[0]]['line']['color'])
        self.line_style.set(self.data_dict[self.data_list[0]]['line']['style'])
        self.line_width.set(self.data_dict[self.data_list[0]]['line']['width'])
        self.line_alpha.set(self.data_dict[self.data_list[0]]['line']['alpha'])

        self.mark_exist.set(self.data_dict[self.data_list[0]]['marker']['exist'])
        self.mark_type.set(self.data_dict[self.data_list[0]]['marker']['type'])
        self.mark_ec.set(self.data_dict[self.data_list[0]]['marker']['edge_col'])
        self.mark_ew .set(self.data_dict[self.data_list[0]]['marker']['edge_wid'])
        self.mark_fc.set(self.data_dict[self.data_list[0]]['marker']['face_col'])
        self.mark_sz.set(self.data_dict[self.data_list[0]]['marker']['size'])

        self.fill_exist.set(self.data_dict[self.data_list[0]]['fill']['exist'])
        self.fill_alpha.set(self.data_dict[self.data_list[0]]['fill']['alpha'])
        self.fill_ec.set(self.data_dict[self.data_list[0]]['fill']['edge_col'])
        self.fill_fc.set(self.data_dict[self.data_list[0]]['fill']['face_col'])
        self.fill_linew.set(self.data_dict[self.data_list[0]]['fill']['line_wid'])
        self.fill_lines.set(self.data_dict[self.data_list[0]]['fill']['line_sty'])

        self.scat_exist.set(self.data_dict[self.data_list[0]]['scatter']['exist'])
        self.scat_type.set(self.data_dict[self.data_list[0]]['scatter']['type'])
        self.scat_size_list = list(self.data_dict[self.data_list[0]]['scatter']['size_vector_names'])
        self.scat_size.set(self.scat_size_list[0])
        self.scat_color_list = list(self.data_dict[self.data_list[0]]['scatter']['color_vector_names'])
        self.scat_color.set(self.scat_color_list[0])
        self.cmap_pick.set('viridis')
        self.scat_edge.set('none')
        self.scat_alpha.set(0.5)
        self.cb_exist.set(1)

        self.gridrow.set(1)
        self.gridcol.set(1)
        self.sharex.set(0)
        self.sharey.set(0)

        self.alldat_selected.set(self.data_list[0])
        self.seldat_selected.set(self.axis_dict['axis1']['plots'][0])
        self.selected_axis_data = self.axis_dict['axis1']['plots']

        self.current_axis.set('axis1')

        self.axrow.set(self.axis_dict['axis1']['position'][0])
        self.axcol.set(self.axis_dict['axis1']['position'][1])
        self.axrowspan.set(self.axis_dict['axis1']['position'][2])
        self.axcolspan.set(self.axis_dict['axis1']['position'][3])

        self.xlab.set(self.axis_dict['axis1']['x_label'])
        self.ylab.set(self.axis_dict['axis1']['y_label'])

        self.axsize.set(self.axis_dict['axis1']['axis_text']['size'])

        self.xlimlow.set(self.axis_dict['axis1']['x_lim'][0])
        self.xlimhi.set(self.axis_dict['axis1']['x_lim'][1])
        self.ylimlow.set(self.axis_dict['axis1']['y_lim'][0])
        self.ylimhi.set(self.axis_dict['axis1']['y_lim'][1])
        self.xticks.set(self.axis_dict['axis1']['xticks'])
        self.yticks.set(self.axis_dict['axis1']['yticks'])
        self.xlog.set(self.axis_dict['axis1']['xscale'])
        self.ylog.set(self.axis_dict['axis1']['yscale'])

        self.axbold.set(self.axis_dict['axis1']['axis_text']['Bold'])
        self.axitalic.set(self.axis_dict['axis1']['axis_text']['Italic'])

        self.title.set(self.axis_dict['axis1']['title'])
        self.tsize.set(self.axis_dict['axis1']['title_text']['size'])
        self.tbold.set(self.axis_dict['axis1']['title_text']['Bold'])
        self.titalic.set(self.axis_dict['axis1']['title_text']['Italic'])

        self.legend.set(self.axis_dict['axis1']['legend'])
        self.lgSize.set(self.axis_dict['axis1']['legendFontSize'])

    def ebar_col_h(self):
        col = askcolor(self.ebar_color.get())[1]
        self.ebar_color.set(col)
        self.eb_col['bg'] = col
        self.eb_col['activebackground'] = col

    def line_col_h(self):
        col = askcolor(self.line_color.get())[1]
        if col != None:
            self.line_color.set(col)
            self.l_col['bg'] = col
            self.l_col['activebackground'] = col

    def me_col_h(self):
        col = askcolor(self.mark_ec.get())[1]
        if col != None:
            self.mark_ec.set(col)
            self.m_ecol['bg'] = col
            self.m_ecol['activebackground'] = col

    def mf_col_h(self):
        col = askcolor(self.mark_fc.get())[1]
        if col != None:
            self.mark_fc.set(col)
            self.m_fcol['bg'] = col
            self.m_fcol['activebackground'] = col

    def fe_col_h(self):
        col = askcolor(self.fill_ec.get())[1]
        if col != None:
            self.fill_ec.set(col)
            self.f_ecol['bg'] = col
            self.f_ecol['activebackground'] = col

    def ff_col_h(self):
        col = askcolor(self.fill_fc.get())[1]
        if col != None:
            self.fill_fc.set(col)
            self.f_fcol['bg'] = col
            self.f_fcol['activebackground'] = col

    def clear_multi_choice(self):
        selected = self.selection_list.curselection()
        all_val = self.multi_list.get()[1:-1].split(', ')
        new_list = ''
        for i in range(len(all_val)):
            if i != 0:
                new_list += ' '
            if i not in selected:
                new_list += all_val[i][1:-1]
        self.multi_list.set(new_list)

    def multi_select_finish(self):
        if self.multi_select.get() == 0:
            if self.multi_list.get() == '':
                return
            options = self.multi_list.get()[1:-1].split(', ')
            multi_list = []
            for i in range(len(options)):
                multi_list.append(options[i][1:-1])

            for item in multi_list:
                self.data_dict[item]['ebar']['exist'] = self.ebar_exist.get()
                self.data_dict[item]['ebar']['color'] = self.ebar_color.get()
                self.data_dict[item]['ebar']['linew'] = self.ebar_linew.get()
                self.data_dict[item]['ebar']['capsize'] = self.ebar_caps.get()
                self.data_dict[item]['ebar']['capthick'] = self.ebar_capt.get()

                self.data_dict[item]['line']['exist'] = self.line_exist.get()
                self.data_dict[item]['line']['color'] = self.line_color.get()
                self.data_dict[item]['line']['style'] = self.line_style.get()
                self.data_dict[item]['line']['width'] = self.line_width.get()
                self.data_dict[item]['line']['alpha'] = self.line_alpha.get()

                self.data_dict[item]['marker']['exist'] = self.mark_exist.get()
                self.data_dict[item]['marker']['type'] = self.mark_type.get()
                self.data_dict[item]['marker']['edge_col'] = self.mark_ec.get()
                self.data_dict[item]['marker']['edge_wid'] = self.mark_ew .get()
                self.data_dict[item]['marker']['face_col'] = self.mark_fc.get()
                self.data_dict[item]['marker']['size'] = self.mark_sz.get()

                self.data_dict[item]['fill']['exist'] = self.fill_exist.get()
                self.data_dict[item]['fill']['alpha'] = self.fill_alpha.get()
                self.data_dict[item]['fill']['edge_col'] = self.fill_ec.get()
                self.data_dict[item]['fill']['face_col'] = self.fill_fc.get()
                self.data_dict[item]['fill']['line_wid'] = self.fill_linew.get()
                self.data_dict[item]['fill']['line_sty'] = self.fill_lines.get()

                self.data_dict[item]['scatter']['exist'] = self.scat_exist.get()
                self.data_dict[item]['scatter']['type'] = self.scat_type.get()
                self.data_dict[item]['scatter']['current_size'] = self.scat_size.get()
                self.data_dict[item]['scatter']['current_color'] = self.scat_color.get()
                self.data_dict[item]['scatter']['cmap'] = self.cmap_pick.get()
                self.data_dict[item]['scatter']['alpha'] = float(self.scat_alpha.get())
                self.data_dict[item]['scatter']['edge'] = self.scat_edge.get()
                self.data_dict[item]['colorbar'] = self.cb_exist.get()
            self.multi_list.set('')
            event = self.current_data.get()
            self.dat_lab.set(self.data_dict[event]['label'])
            self.dat_lab2.set(self.data_dict[event]['fill-label'])
            self.current_data.set(event)
            self.selected_data_value = self.current_data.get()

            self.ebar_exist.set(self.data_dict[event]['ebar']['exist'])
            self.ebar_color.set(self.data_dict[event]['ebar']['color'])
            self.eb_col['bg'] = self.data_dict[event]['ebar']['color']
            self.eb_col['activebackground'] = self.data_dict[event]['ebar']['color']
            self.ebar_linew.set(self.data_dict[event]['ebar']['linew'])
            self.ebar_caps.set(self.data_dict[event]['ebar']['capsize'])
            self.ebar_capt.set(self.data_dict[event]['ebar']['capthick'])

            self.line_exist.set(self.data_dict[event]['line']['exist'])
            self.line_color.set(self.data_dict[event]['line']['color'])
            self.l_col['bg'] = self.data_dict[event]['line']['color']
            self.l_col['activebackground'] = self.data_dict[event]['line']['color']
            self.line_style.set(self.data_dict[event]['line']['style'])
            self.line_width.set(self.data_dict[event]['line']['width'])
            self.line_alpha.set(self.data_dict[event]['line']['alpha'])

            self.mark_exist.set(self.data_dict[event]['marker']['exist'])
            self.mark_type.set(self.data_dict[event]['marker']['type'])
            self.mark_ec.set(self.data_dict[event]['marker']['edge_col'])
            self.m_ecol['bg'] = self.data_dict[event]['marker']['edge_col']
            self.m_ecol['activebackground'] = self.data_dict[event]['marker']['edge_col']
            self.mark_ew .set(self.data_dict[event]['marker']['edge_wid'])
            self.mark_fc.set(self.data_dict[event]['marker']['face_col'])
            self.m_fcol['bg'] = self.data_dict[event]['marker']['face_col']
            self.m_fcol['activebackground'] = self.data_dict[event]['marker']['face_col']
            self.mark_sz.set(self.data_dict[event]['marker']['size'])

            self.fill_exist.set(self.data_dict[event]['fill']['exist'])
            self.fill_alpha.set(self.data_dict[event]['fill']['alpha'])
            self.fill_ec.set(self.data_dict[event]['fill']['edge_col'])
            self.f_ecol['bg'] = self.data_dict[event]['fill']['edge_col']
            self.f_ecol['activebackground'] = self.data_dict[event]['fill']['edge_col']
            self.fill_fc.set(self.data_dict[event]['fill']['face_col'])
            self.f_fcol['bg'] = self.data_dict[event]['fill']['face_col']
            self.f_fcol['activebackground'] = self.data_dict[event]['fill']['face_col']
            self.fill_linew.set(self.data_dict[event]['fill']['line_wid'])
            self.fill_lines.set(self.data_dict[event]['fill']['line_sty'])

            self.scat_exist.set(self.data_dict[event]['scatter']['exist'])
            self.scat_type.set(self.data_dict[event]['scatter']['type'])
            self.cmap_pick.set(self.data_dict[event]['scatter']['cmap'])
            self.scat_alpha.set(self.data_dict[self.selected_data_value]['scatter']['alpha'])
            self.scat_edge.set(self.data_dict[self.selected_data_value]['scatter']['edge'])
            self.cb_exist.set(self.data_dict[self.selected_data_value]['colorbar'])
            self.scat_size_list = list(self.data_dict[event]['scatter']['size_vector_names'])
            self.scat_color_list = list(self.data_dict[event]['scatter']['color_vector_names'])
            menu1 = self.scatter_size["menu"]
            menu1.delete(0, "end")
            for string in self.scat_size_list:
                menu1.add_command(label=string)
            menu2 = self.scatter_color["menu"]
            menu2.delete(0, "end")
            for string in self.scat_color_list:
                menu2.add_command(label=string)
            self.scat_size.set(self.data_dict[event]['scatter']['current_size'])
            self.scat_color.set(self.data_dict[event]['scatter']['current_color'])

    def scatter_select(self):
        if self.scat_exist.get() == 1:
            self.line_exist.set(0)
            self.mark_exist.set(0)
            self.ebar_exist.set(0)
            self.fill_exist.set(0)
        else:
            self.line_exist.set(1)

    def other_plot_select(self):
        if self.line_exist.get() == 1 or self.mark_exist.get() == 1 \
            or self.ebar_exist.get() == 1 or self.fill_exist.get() == 1:
            self.scat_exist.set(0)

    def axis_changed(self, event):
        # print(self.axis_dict)

        if event == self.selected_axis_value:
            return
        else:
            self.axis_dict[self.selected_axis_value]['plots'][0] = self.seldat_selected.get()
            self.axis_dict[self.selected_axis_value]['plots'] = self.selected_axis_data

            self.axis_dict[self.selected_axis_value]['position'][0] = self.axrow.get()
            self.axis_dict[self.selected_axis_value]['position'][1] = self.axcol.get()
            self.axis_dict[self.selected_axis_value]['position'][2] = self.axrowspan.get()
            self.axis_dict[self.selected_axis_value]['position'][3] = self.axcolspan.get()

            self.axis_dict[self.selected_axis_value]['x_label'] = self.xlab.get()
            self.axis_dict[self.selected_axis_value]['y_label'] = self.ylab.get()

            self.axis_dict[self.selected_axis_value]['axis_text']['size'] = self.axsize.get()

            self.axis_dict[self.selected_axis_value]['x_lim'][0] = self.xlimlow.get()
            self.axis_dict[self.selected_axis_value]['x_lim'][1] = self.xlimhi.get()
            self.axis_dict[self.selected_axis_value]['y_lim'][0] = self.ylimlow.get()
            self.axis_dict[self.selected_axis_value]['y_lim'][1] = self.ylimhi.get()
            self.axis_dict[self.selected_axis_value]['xticks'] = self.xticks.get()
            self.axis_dict[self.selected_axis_value]['yticks'] = self.yticks.get()
            self.axis_dict[self.selected_axis_value]['xscale'] = self.xlog.get()
            self.axis_dict[self.selected_axis_value]['yscale'] = self.ylog.get()

            self.axis_dict[self.selected_axis_value]['axis_text']['Bold'] = self.axbold.get()
            self.axis_dict[self.selected_axis_value]['axis_text']['Italic'] = self.axitalic.get()

            self.axis_dict[self.selected_axis_value]['title'] = self.title.get()
            self.axis_dict[self.selected_axis_value]['title_text']['size'] = self.tsize.get()
            self.axis_dict[self.selected_axis_value]['title_text']['Bold'] = self.tbold.get()
            self.axis_dict[self.selected_axis_value]['title_text']['Italic'] = self.titalic.get()

            self.axis_dict[self.selected_axis_value]['legend'] = self.legend.get()
            self.axis_dict[self.selected_axis_value]['legendFontSize'] = self.lgSize.get()

            self.selected_axis_value = event

            self.seldat_selected.set(self.axis_dict[event]['plots'][0])
            self.selected_axis_data = self.axis_dict[event]['plots']
            # print(self.selected_axis_data)

            menu = self.seldat["menu"]
            menu.delete(0, "end")
            for string in self.selected_axis_data:
                menu.add_command(label=string)

            self.current_axis.set(event)

            self.axrow.set(self.axis_dict[event]['position'][0])
            self.axcol.set(self.axis_dict[event]['position'][1])
            self.axrowspan.set(self.axis_dict[event]['position'][2])
            self.axcolspan.set(self.axis_dict[event]['position'][3])

            self.xlab.set(self.axis_dict[event]['x_label'])
            self.ylab.set(self.axis_dict[event]['y_label'])

            self.axsize.set(self.axis_dict[event]['axis_text']['size'])

            self.xlimlow.set(self.axis_dict[event]['x_lim'][0])
            self.xlimhi.set(self.axis_dict[event]['x_lim'][1])
            self.ylimlow.set(self.axis_dict[event]['y_lim'][0])
            self.ylimhi.set(self.axis_dict[event]['y_lim'][1])
            self.xticks.set(self.axis_dict[event]['xticks'])
            self.yticks.set(self.axis_dict[event]['yticks'])
            self.xlog.set(self.axis_dict[event]['xscale'])
            self.ylog.set(self.axis_dict[event]['yscale'])

            self.axbold.set(self.axis_dict[event]['axis_text']['Bold'])
            self.axitalic.set(self.axis_dict[event]['axis_text']['Italic'])

            self.title.set(self.axis_dict[event]['title'])
            self.tsize.set(self.axis_dict[event]['title_text']['size'])
            self.tbold.set(self.axis_dict[event]['title_text']['Bold'])
            self.titalic.set(self.axis_dict[event]['title_text']['Italic'])

            self.legend.set(self.axis_dict[self.selected_axis_value]['legend'])
            self.lgSize.set(self.axis_dict[self.selected_axis_value]['legendFontSize'])

    def plot_changed(self, event):
        if event == self.selected_data_value:
            return
        elif self.multi_select.get() == 1:
            import re
            split_line = re.compile(r',\s*')
            if self.multi_list.get() != '()':
                options = split_line.split(self.multi_list.get()[1:-1])
            else:
                options = []
            multi_list = []
            for i in range(len(options)):
                if i != '':
                    multi_list.append(options[i][1:-1])
            if event not in multi_list:
                multi_list.append(event)
            new_list = ''
            for item in multi_list:
                new_list += '{} '.format(item)
            self.multi_list.set(new_list[:-1])
            self.selected_data_value = event
        else:
            self.data_dict[self.selected_data_value]['label'] = self.dat_lab.get()
            self.data_dict[self.selected_data_value]['fill-label'] = self.dat_lab2.get()

            self.data_dict[self.selected_data_value]['ebar']['exist'] = self.ebar_exist.get()
            self.data_dict[self.selected_data_value]['ebar']['color'] = self.ebar_color.get()
            self.data_dict[self.selected_data_value]['ebar']['linew'] = self.ebar_linew.get()
            self.data_dict[self.selected_data_value]['ebar']['capsize'] = self.ebar_caps.get()
            self.data_dict[self.selected_data_value]['ebar']['capthick'] = self.ebar_capt.get()

            self.data_dict[self.selected_data_value]['line']['exist'] = self.line_exist.get()
            self.data_dict[self.selected_data_value]['line']['color'] = self.line_color.get()
            self.data_dict[self.selected_data_value]['line']['style'] = self.line_style.get()
            self.data_dict[self.selected_data_value]['line']['width'] = self.line_width.get()
            self.data_dict[self.selected_data_value]['line']['alpha'] = self.line_alpha.get()

            self.data_dict[self.selected_data_value]['marker']['exist'] = self.mark_exist.get()
            self.data_dict[self.selected_data_value]['marker']['type'] = self.mark_type.get()
            self.data_dict[self.selected_data_value]['marker']['edge_col'] = self.mark_ec.get()
            self.data_dict[self.selected_data_value]['marker']['edge_wid'] = self.mark_ew .get()
            self.data_dict[self.selected_data_value]['marker']['face_col'] = self.mark_fc.get()
            self.data_dict[self.selected_data_value]['marker']['size'] = self.mark_sz.get()

            self.data_dict[self.selected_data_value]['fill']['exist'] = self.fill_exist.get()
            self.data_dict[self.selected_data_value]['fill']['alpha'] = self.fill_alpha.get()
            self.data_dict[self.selected_data_value]['fill']['edge_col'] = self.fill_ec.get()
            self.data_dict[self.selected_data_value]['fill']['face_col'] = self.fill_fc.get()
            self.data_dict[self.selected_data_value]['fill']['line_wid'] = self.fill_linew.get()
            self.data_dict[self.selected_data_value]['fill']['line_sty'] = self.fill_lines.get()

            self.data_dict[self.selected_data_value]['scatter']['exist'] = self.scat_exist.get()
            self.data_dict[self.selected_data_value]['scatter']['type'] = self.scat_type.get()
            self.data_dict[self.selected_data_value]['scatter']['current_size'] = self.scat_size.get()
            self.data_dict[self.selected_data_value]['scatter']['current_color'] = self.scat_color.get()
            self.data_dict[self.selected_data_value]['scatter']['cmap'] = self.cmap_pick.get()
            self.data_dict[self.selected_data_value]['scatter']['alpha'] = float(self.scat_alpha.get())
            self.data_dict[self.selected_data_value]['scatter']['edge'] = self.scat_edge.get()
            self.data_dict[self.selected_data_value]['colorbar'] = self.cb_exist.get()

            self.selected_data_value = event
            self.dat_lab.set(self.data_dict[event]['label'])
            self.dat_lab2.set(self.data_dict[event]['fill-label'])
            self.current_data.set(event)
            self.selected_data_value = self.current_data.get()

            self.ebar_exist.set(self.data_dict[event]['ebar']['exist'])
            self.ebar_color.set(self.data_dict[event]['ebar']['color'])
            self.eb_col['bg'] = self.data_dict[event]['ebar']['color']
            self.eb_col['activebackground'] = self.data_dict[event]['ebar']['color']
            self.ebar_linew.set(self.data_dict[event]['ebar']['linew'])
            self.ebar_caps.set(self.data_dict[event]['ebar']['capsize'])
            self.ebar_capt.set(self.data_dict[event]['ebar']['capthick'])

            self.line_exist.set(self.data_dict[event]['line']['exist'])
            self.line_color.set(self.data_dict[event]['line']['color'])
            self.l_col['bg'] = self.data_dict[event]['line']['color']
            self.l_col['activebackground'] = self.data_dict[event]['line']['color']
            self.line_style.set(self.data_dict[event]['line']['style'])
            self.line_width.set(self.data_dict[event]['line']['width'])
            self.line_alpha.set(self.data_dict[event]['line']['alpha'])

            self.mark_exist.set(self.data_dict[event]['marker']['exist'])
            self.mark_type.set(self.data_dict[event]['marker']['type'])
            self.mark_ec.set(self.data_dict[event]['marker']['edge_col'])
            self.m_ecol['bg'] = self.data_dict[event]['marker']['edge_col']
            self.m_ecol['activebackground'] = self.data_dict[event]['marker']['edge_col']
            self.mark_ew .set(self.data_dict[event]['marker']['edge_wid'])
            self.mark_fc.set(self.data_dict[event]['marker']['face_col'])
            self.m_fcol['bg'] = self.data_dict[event]['marker']['face_col']
            self.m_fcol['activebackground'] = self.data_dict[event]['marker']['face_col']
            self.mark_sz.set(self.data_dict[event]['marker']['size'])

            self.fill_exist.set(self.data_dict[event]['fill']['exist'])
            self.fill_alpha.set(self.data_dict[event]['fill']['alpha'])
            self.fill_ec.set(self.data_dict[event]['fill']['edge_col'])
            self.f_ecol['bg'] = self.data_dict[event]['fill']['edge_col']
            self.f_ecol['activebackground'] = self.data_dict[event]['fill']['edge_col']
            self.fill_fc.set(self.data_dict[event]['fill']['face_col'])
            self.f_fcol['bg'] = self.data_dict[event]['fill']['face_col']
            self.f_fcol['activebackground'] = self.data_dict[event]['fill']['face_col']
            self.fill_linew.set(self.data_dict[event]['fill']['line_wid'])
            self.fill_lines.set(self.data_dict[event]['fill']['line_sty'])

            self.scat_exist.set(self.data_dict[event]['scatter']['exist'])
            self.scat_type.set(self.data_dict[event]['scatter']['type'])
            self.cmap_pick.set(self.data_dict[event]['scatter']['cmap'])
            self.scat_alpha.set(self.data_dict[event]['scatter']['alpha'])
            self.scat_edge.set(self.data_dict[event]['scatter']['edge'])
            self.cb_exist.set(self.data_dict[event]['colorbar'])
            menu = self.scatter_size["menu"]
            menu.delete(0, "end")
            for string in list(self.data_dict[event]['scatter']['size_vector_names']):
                menu.add_command(label=string,
                                 command=lambda value=string: self.scat_size.set(value))
            menu = self.scatter_color["menu"]
            menu.delete(0, "end")
            for string in list(self.data_dict[event]['scatter']['color_vector_names']):
                menu.add_command(label=string,
                                 command=lambda value=string: self.scat_color.set(value))
            self.scat_size.set(self.data_dict[event]['scatter']['current_size'])
            self.scat_color.set(self.data_dict[event]['scatter']['current_color'])

    def add_first_axis(self):
        self.axis_dict['axis1'] = {'plots':[],
                                   'plots_data':[],
                                   'x_lim':[],
                                   'y_lim':[],
                                   'x_label':'x',
                                   'y_label':'y',
                                   'title':'Plot',
                                   'axis_text':{'size':12, 'Bold':0,
                                                'Italic':0, 'Underline':0},
                                   'title_text':{'size':12, 'Bold':1,
                                                 'Italic':0, 'Underline':0},
                                   'position':[0, 0, 1, 1],
                                   'legend':'best',
                                   'legendFontSize':8,
                                   'xticks': 1, 'yticks':1,
                                   'xscale':0, 'yscale':0}
        max_x = -1e16
        min_x = 1e16
        max_y = -1e16
        min_y = 1e16
        for i in range(len(self.data_list)):
            self.axis_dict['axis1']['plots_data'].append(self.data_dict[self.data_list[i]])
            self.axis_dict['axis1']['plots'].append(self.data_list[i])
            if max(self.data_dict[self.data_list[i]]['x']) > max_x:
                max_x = max(self.data_dict[self.data_list[i]]['x'])
            if max(self.data_dict[self.data_list[i]]['y']) > max_y:
                max_y = max(self.data_dict[self.data_list[i]]['y'])
            if min(self.data_dict[self.data_list[i]]['x']) < min_x:
                min_x = min(self.data_dict[self.data_list[i]]['x'])
            if min(self.data_dict[self.data_list[i]]['y']) < min_y:
                min_y = min(self.data_dict[self.data_list[i]]['y'])
        self.axis_dict['axis1']['x_lim'] = [min_x, max_x]
        self.axis_dict['axis1']['y_lim'] = [min_y, max_y]

    def add_new_axis(self):
        self.axis_dict['axis{}'.format(self.axis_count+1)] = {
            'plots':[''],
            'plots_data':[''],
            'x_lim':[0, 1],
            'y_lim':[0, 1],
            'x_label':'x',
            'y_label':'y',
            'title':'Plot',
            'axis_text':{'size':12, 'Bold':0,
                         'Italic':0, 'Underline':0},
            'title_text':{'size':12, 'Bold':1,
                          'Italic':0, 'Underline':0},
            'position':[0, 0, 1, 1],
            'legend':'best',
            'legendFontSize':8,
            'xticks': 1, 'yticks':1,
            'xscale':0, 'yscale':0}
        self.axis_list.append('axis{}'.format(self.axis_count+1))
        menu = self.axis_select["menu"]
        menu.delete(0, "end")
        for string in self.axis_list:
            menu.add_command(label=string,
                             command=lambda value=string: self.axis_changed(value))
        self.axis_count += 1

    def del_curr_axis(self):
        if self.axis_list[0] == self.current_axis.get():
            messagebox.showerror("Delete Axis", "Axis 1 cannot be deleted!")
            return
        temp_axis_list = []
        temp_axis_dict = {}
        menu = self.axis_select["menu"]
        menu.delete(0, "end")
        for string in self.axis_list:
            if string != self.current_axis.get():
                temp_axis_list.append(string)
                temp_axis_dict[string] = self.axis_dict[string]
                menu.add_command(label=string,
                                 command=lambda value=string: self.axis_changed(value))
        self.axis_dict = temp_axis_dict
        self.axis_list = temp_axis_list

        event = self.axis_list[0]

        self.selected_axis_value = event

        self.seldat_selected.set(self.axis_dict[event]['plots'][0])
        self.selected_axis_data = self.axis_dict[event]['plots']
        # print(self.selected_axis_data)

        menu = self.seldat["menu"]
        menu.delete(0, "end")
        for string in self.selected_axis_data:
            menu.add_command(label=string)

        self.current_axis.set(event)

        self.axrow.set(self.axis_dict[event]['position'][0])
        self.axcol.set(self.axis_dict[event]['position'][1])
        self.axrowspan.set(self.axis_dict[event]['position'][2])
        self.axcolspan.set(self.axis_dict[event]['position'][3])

        self.xlab.set(self.axis_dict[event]['x_label'])
        self.ylab.set(self.axis_dict[event]['y_label'])

        self.axsize.set(self.axis_dict[event]['axis_text']['size'])

        self.xlimlow.set(self.axis_dict[event]['x_lim'][0])
        self.xlimhi.set(self.axis_dict[event]['x_lim'][1])
        self.ylimlow.set(self.axis_dict[event]['y_lim'][0])
        self.ylimhi.set(self.axis_dict[event]['y_lim'][1])
        self.xticks.set(self.axis_dict[event]['xticks'])
        self.yticks.set(self.axis_dict[event]['yticks'])
        self.xlog.set(self.axis_dict[event]['xscale'])
        self.ylog.set(self.axis_dict[event]['yscale'])

        self.axbold.set(self.axis_dict[event]['axis_text']['Bold'])
        self.axitalic.set(self.axis_dict[event]['axis_text']['Italic'])

        self.title.set(self.axis_dict[event]['title'])
        self.tsize.set(self.axis_dict[event]['title_text']['size'])
        self.tbold.set(self.axis_dict[event]['title_text']['Bold'])
        self.titalic.set(self.axis_dict[event]['title_text']['Italic'])

        self.legend.set(self.axis_dict[self.selected_axis_value]['legend'])
        self.lgSize.set(self.axis_dict[self.selected_axis_value]['legendFontSize'])

    def add_plot_to_axis(self):
        plot_name = self.alldat_selected.get()
        if plot_name not in self.axis_dict[self.current_axis.get()]['plots']:
            if self.axis_dict[self.current_axis.get()]['plots'][0] == '':
                self.axis_dict[self.current_axis.get()]['plots'] = []
                self.axis_dict[self.current_axis.get()]['plots_data'] = []
                max_x = -1e16
                min_x = 1e16
                max_y = -1e16
                min_y = 1e16
            else:
                max_x = self.axis_dict[self.current_axis.get()]['x_lim'][1]
                min_x = self.axis_dict[self.current_axis.get()]['x_lim'][0]
                max_y = self.axis_dict[self.current_axis.get()]['y_lim'][1]
                min_y = self.axis_dict[self.current_axis.get()]['y_lim'][0]
            self.axis_dict[self.current_axis.get()]['plots'].append(plot_name)
            self.axis_dict[self.current_axis.get()]['plots_data'].append(self.data_dict[plot_name])

            if np.max(self.data_dict[plot_name]['x']) > max_x:
                max_x = np.max(self.data_dict[plot_name]['x'])
            if np.max(self.data_dict[plot_name]['y']) > max_y:
                max_y = np.max(self.data_dict[plot_name]['y'])
            if np.min(self.data_dict[plot_name]['x']) < min_x:
                min_x = np.min(self.data_dict[plot_name]['x'])
            if np.min(self.data_dict[plot_name]['y']) < min_y:
                min_y = np.min(self.data_dict[plot_name]['y'])
            self.axis_dict[self.current_axis.get()]['x_lim'] = [min_x, max_x]
            self.axis_dict[self.current_axis.get()]['y_lim'] = [min_y, max_y]

            self.xlimlow.set(min_x)
            self.xlimhi.set(max_x)
            self.ylimlow.set(min_y)
            self.ylimhi.set(max_y)

            self.seldat_selected.set(self.axis_dict[self.current_axis.get()]['plots'][0])
            self.selected_axis_data = self.axis_dict[self.current_axis.get()]['plots']

            menu = self.seldat["menu"]
            menu.delete(0, "end")
            for string in self.axis_dict[self.current_axis.get()]['plots']:
                menu.add_command(label=string,
                                 command=lambda value=string: self.seldat_selected.set(value))
            self.seldat_selected.set(self.axis_dict[self.current_axis.get()]['plots'][0])

    def remove_plot_from_axis(self):
        plot_name = self.seldat_selected.get()
        temp_plots = []
        temp_plots_data = []
        max_x = -1e16
        min_x = 1e16
        max_y = -1e16
        min_y = 1e16

        for i in range(len(self.axis_dict[self.current_axis.get()]['plots'])):
            if self.axis_dict[self.current_axis.get()]['plots'][i] != plot_name:
                plot_name_temp = self.axis_dict[self.current_axis.get()]['plots'][i]
                temp_plots.append(self.axis_dict[self.current_axis.get()]['plots'][i])
                temp_plots_data.append(self.data_dict[self.axis_dict[self.current_axis.get()]['plots'][i]])
                if np.max(self.data_dict[plot_name_temp]['x']) > max_x:
                    max_x = np.max(self.data_dict[plot_name_temp]['x'])
                if np.max(self.data_dict[plot_name_temp]['y']) > max_y:
                    max_y = np.max(self.data_dict[plot_name_temp]['y'])
                if np.min(self.data_dict[plot_name_temp]['x']) < min_x:
                    min_x = np.min(self.data_dict[plot_name_temp]['x'])
                if np.min(self.data_dict[plot_name_temp]['y']) < min_y:
                    min_y = np.min(self.data_dict[plot_name_temp]['y'])

        if temp_plots == []:
            self.axis_dict[self.current_axis.get()]['plots'] = ['']
            self.axis_dict[self.current_axis.get()]['plots_data'] = ['']
            max_x = 1
            min_x = 0
            max_y = 1
            min_y = 0
        else:
            self.axis_dict[self.current_axis.get()]['plots'] = temp_plots
            self.axis_dict[self.current_axis.get()]['plots_data'] = temp_plots_data

        self.axis_dict[self.current_axis.get()]['x_lim'] = [min_x, max_x]
        self.axis_dict[self.current_axis.get()]['y_lim'] = [min_y, max_y]

        self.xlimlow.set(min_x)
        self.xlimhi.set(max_x)
        self.ylimlow.set(min_y)
        self.ylimhi.set(max_y)

        self.seldat_selected.set(self.axis_dict[self.current_axis.get()]['plots'][0])
        self.selected_axis_data = self.axis_dict[self.current_axis.get()]['plots']

        menu = self.seldat["menu"]
        menu.delete(0, "end")
        for string in self.axis_dict[self.current_axis.get()]['plots']:
            menu.add_command(label=string,
                             command=lambda value=string: self.seldat_selected.set(value))
        self.seldat_selected.set(self.axis_dict[self.current_axis.get()]['plots'][0])

    def gen_plot(self):
        plt.close(1)
        self.collect_current_data()
        test_grid = np.zeros((self.gridrow.get(), self.gridcol.get()))

        plot_dict = {}
        plot_dict['axes'] = list(self.axis_dict.keys())
        plot_dict['axis data'] = self.axis_dict
        plot_dict['fig_size'] = [2+2*self.gridrow.get(), 2.5+2.5*self.gridcol.get()]
        plot_dict['gsr'] = self.gridrow.get()
        plot_dict['gsc'] = self.gridcol.get()
        plot_dict['sharex'] = self.sharex.get()
        plot_dict['sharey'] = self.sharey.get()
        plot_obj = plot_class(plot_dict, '')

        try:
            for axis in plot_dict['axes']:
                data = plot_dict['axis data'][axis]
                for i in range(data['position'][2]):
                    for j in range(data['position'][3]):
                        test_grid[data['position'][0]+i, data['position'][1]+j] = 1
            if np.sum(test_grid) != plot_dict['gsr']*plot_dict['gsc']:
                messagebox.showerror(title='Grid Error',
                                     message="All Grid Spaces must be filled!")
                return
        except IndexError:
            messagebox.showerror(title='Grid Error',
                                 message="Grid index of plot exceeds Grid Bounds!")
            return


        if (self.sharex.get() == 0) and (self.sharey.get() == 0):
            plot_obj.show_plot()
        else:
            plot_obj.show_plot2()

    def save_plot(self):
        plt.close(1)
        self.collect_current_data()
        file = filedialog.asksaveasfile(defaultextension='.png',
                                        title='Save Matplotlib Figure',
                                        filetypes=[('png files (*.png)',
                                                    '*.png')])
        if file != None:
            test_grid = np.zeros((self.gridrow.get(), self.gridcol.get()))
            plot_dict = {}
            plot_dict['axes'] = list(self.axis_dict.keys())
            plot_dict['axis data'] = self.axis_dict
            plot_dict['fig_size'] = [3+3*self.gridrow.get(),
                                     3.5+3.5*self.gridcol.get()]
            plot_dict['gsr'] = self.gridrow.get()
            plot_dict['gsc'] = self.gridcol.get()
            plot_dict['sharex'] = self.sharex.get()
            plot_dict['sharey'] = self.sharey.get()
            plot_obj = plot_class(plot_dict, file.name)

            try:
                for axis in plot_dict['axes']:
                    data = plot_dict['axis data'][axis]
                    for i in range(data['position'][2]):
                        for j in range(data['position'][3]):
                            test_grid[data['position'][0]+i,
                                      data['position'][1]+j] = 1
                if np.sum(test_grid) != plot_dict['gsr']*plot_dict['gsc']:
                    messagebox.showerror(title='Grid Error',
                                         message="All Grid Spaces must be filled!")
                    return
            except IndexError:
                messagebox.showerror(title='Grid Error',
                                     message="Grid index of plot exceeds Grid Bounds!")
                return

            if (self.sharex.get() == 0) and (self.sharey.get() == 0):
                plot_obj.save_plot()
            else:
                plot_obj.save_plot2()

    def collect_current_data(self):
        self.data_dict[self.selected_data_value]['label'] = self.dat_lab.get()
        self.data_dict[self.selected_data_value]['fill-label'] = self.dat_lab2.get()

        self.data_dict[self.selected_data_value]['ebar']['exist'] = self.ebar_exist.get()
        self.data_dict[self.selected_data_value]['ebar']['color'] = self.ebar_color.get()
        self.data_dict[self.selected_data_value]['ebar']['linew'] = self.ebar_linew.get()
        self.data_dict[self.selected_data_value]['ebar']['capsize'] = self.ebar_caps.get()
        self.data_dict[self.selected_data_value]['ebar']['capthick'] = self.ebar_capt.get()

        self.data_dict[self.selected_data_value]['line']['exist'] = self.line_exist.get()
        self.data_dict[self.selected_data_value]['line']['color'] = self.line_color.get()
        self.data_dict[self.selected_data_value]['line']['style'] = self.line_style.get()
        self.data_dict[self.selected_data_value]['line']['width'] = self.line_width.get()
        self.data_dict[self.selected_data_value]['line']['alpha'] = self.line_alpha.get()

        self.data_dict[self.selected_data_value]['marker']['exist'] = self.mark_exist.get()
        self.data_dict[self.selected_data_value]['marker']['type'] = self.mark_type.get()
        self.data_dict[self.selected_data_value]['marker']['edge_col'] = self.mark_ec.get()
        self.data_dict[self.selected_data_value]['marker']['edge_wid'] = self.mark_ew .get()
        self.data_dict[self.selected_data_value]['marker']['face_col'] = self.mark_fc.get()
        self.data_dict[self.selected_data_value]['marker']['size'] = self.mark_sz.get()

        self.data_dict[self.selected_data_value]['fill']['exist'] = self.fill_exist.get()
        self.data_dict[self.selected_data_value]['fill']['alpha'] = self.fill_alpha.get()
        self.data_dict[self.selected_data_value]['fill']['edge_col'] = self.fill_ec.get()
        self.data_dict[self.selected_data_value]['fill']['face_col'] = self.fill_fc.get()
        self.data_dict[self.selected_data_value]['fill']['line_wid'] = self.fill_linew.get()
        self.data_dict[self.selected_data_value]['fill']['line_sty'] = self.fill_lines.get()
        self.axis_dict[self.selected_axis_value]['plots'][0] = self.seldat_selected.get()
        self.axis_dict[self.selected_axis_value]['plots'] = self.selected_axis_data

        self.data_dict[self.selected_data_value]['scatter']['exist'] = self.scat_exist.get()
        self.data_dict[self.selected_data_value]['scatter']['type'] = self.scat_type.get()
        self.data_dict[self.selected_data_value]['scatter']['edge'] = self.scat_edge.get()
        self.data_dict[self.selected_data_value]['scatter']['current_size'] = self.scat_size.get()
        self.data_dict[self.selected_data_value]['scatter']['current_color'] = self.scat_color.get()
        self.data_dict[self.selected_data_value]['scatter']['cmap'] = self.cmap_pick.get()
        self.data_dict[self.selected_data_value]['scatter']['alpha'] = float(self.scat_alpha.get())
        self.data_dict[self.selected_data_value]['colorbar'] = self.cb_exist.get()

        self.axis_dict[self.selected_axis_value]['position'][0] = self.axrow.get()
        self.axis_dict[self.selected_axis_value]['position'][1] = self.axcol.get()
        self.axis_dict[self.selected_axis_value]['position'][2] = self.axrowspan.get()
        self.axis_dict[self.selected_axis_value]['position'][3] = self.axcolspan.get()

        self.axis_dict[self.selected_axis_value]['x_label'] = self.xlab.get()
        self.axis_dict[self.selected_axis_value]['y_label'] = self.ylab.get()

        self.axis_dict[self.selected_axis_value]['axis_text']['size'] = self.axsize.get()

        self.axis_dict[self.selected_axis_value]['x_lim'][0] = self.xlimlow.get()
        self.axis_dict[self.selected_axis_value]['x_lim'][1] = self.xlimhi.get()
        self.axis_dict[self.selected_axis_value]['y_lim'][0] = self.ylimlow.get()
        self.axis_dict[self.selected_axis_value]['y_lim'][1] = self.ylimhi.get()
        self.axis_dict[self.selected_axis_value]['xticks'] = self.xticks.get()
        self.axis_dict[self.selected_axis_value]['yticks'] = self.yticks.get()
        self.axis_dict[self.selected_axis_value]['xscale'] = self.xlog.get()
        self.axis_dict[self.selected_axis_value]['yscale'] = self.ylog.get()

        self.axis_dict[self.selected_axis_value]['axis_text']['Bold'] = self.axbold.get()
        self.axis_dict[self.selected_axis_value]['axis_text']['Italic'] = self.axitalic.get()

        self.axis_dict[self.selected_axis_value]['title'] = self.title.get()
        self.axis_dict[self.selected_axis_value]['title_text']['size'] = self.tsize.get()
        self.axis_dict[self.selected_axis_value]['title_text']['Bold'] = self.tbold.get()
        self.axis_dict[self.selected_axis_value]['title_text']['Italic'] = self.titalic.get()

        self.axis_dict[self.selected_axis_value]['legend'] = self.legend.get()
        self.axis_dict[self.selected_axis_value]['legendFontSize'] = self.lgSize.get()




class plot_class():
    def __init__(self, axis_dict, fname):
        self.axis_dict = axis_dict
        self.axis_list = axis_dict['axes']
        self.axis_data = axis_dict['axis data']
        self.fig = plt.figure(num=1, constrained_layout=True,
                              figsize=(axis_dict['fig_size'][1],
                                       axis_dict['fig_size'][0]))
        self.rows = axis_dict['gsr']
        self.cols = axis_dict['gsc']
        self.gs = GridSpec(self.rows, self.cols, figure=self.fig)
        self.save_fname = fname
        self.axis_names = []
        self.axes = []
        self.sharex = axis_dict['sharex']
        self.sharey = axis_dict['sharey']
        for i in range(axis_dict['gsr']):
            self.axes.append([])
            self.axis_names.append([])
            for j in range(axis_dict['gsc']):
                self.axes[i].append('')
                self.axis_names[i].append('')


    def show_plot(self):
        label_length = ''
        cbar_map = []
        cbar_axis = []
        ax = []
        colorbar = 0
        count = 0
        for axis in self.axis_list:
            data = self.axis_data[axis]
            ax.append(self.fig.add_subplot(
                self.gs[data['position'][0]:data['position'][0]+data['position'][2],
                        data['position'][1]:data['position'][1]+data['position'][3]]))
            
            for plot_num in range(len(data['plots'])):
                plot = data['plots_data'][plot_num]

                if plot['fill']['exist'] == 1 and len(plot['dif_top']) > 0:
                    ax[count].fill_between(
                        np.array(plot['x']),
                        np.array(plot['y'])+np.array(plot['dif_top']),
                        np.array(plot['y'])-np.array(plot['dif_bot']),
                        alpha=plot['fill']['alpha'],
                        edgecolor=plot['fill']['edge_col'],
                        facecolor=plot['fill']['face_col'],
                        linewidth=plot['fill']['line_wid'],
                        linestyle=plot['fill']['line_sty'],
                        label=plot['fill-label'])
                    label_length += 'label'

                no_err_data = (plot['y_err'].size == 0 and plot['x_err'].size == 0)
                if plot['scatter']['exist'] == 1:
                    if plot['colorbar'] == 1:
                        colorbar = 1
                    else:
                        colorbar = 0
                    # set cmap
                    color_map = plt.get_cmap(plot['scatter']['cmap'])
                    # check for color vector
                    if plot['scatter']['current_color'] == 'None':
                        color = plot['marker']['face_col']
                        colorbar = 0
                    else:
                        col_index = plot['scatter']['color_vector_names'].index(plot['scatter']['current_color'])
                        color = np.array(plot['scatter']['color_vectors'][col_index])

                    # check for size vector
                    if plot['scatter']['current_size'] == 'None':
                        size = plot['marker']['size']**2
                    else:
                        sz_index = plot['scatter']['size_vector_names'].index(plot['scatter']['current_size'])
                        size = np.array(plot['scatter']['size_vectors'][sz_index])
                        size = ((size-size.min())/(size.max()-size.min()))*20*plot['marker']['size']
                    cset = ax[count].scatter(
                        x=plot['x'], y=plot['y'],
                        s=size, c=color, marker=plot['scatter']['type'],
                        alpha=plot['scatter']['alpha'], edgecolors=plot['scatter']['edge'],
                        linewidths=plot['marker']['edge_wid'], cmap=color_map)
                    if colorbar == 1:
                        cbar_map.append(cset)
                        cbar_axis.append(ax[count])
                else:
                    if plot['ebar']['exist'] == 1 and not no_err_data:
                        if len(plot['y_err']) == 0:
                            if plot['line']['exist'] == 1:
                                linestyle = plot['line']['style']
                            else: 
                                linestyle = ''
                            if plot['marker']['exist'] == 1:
                                marker_type = plot['marker']['type']
                            else: 
                                marker_type = 'None'
                            ax[count].errorbar(
                                x=plot['x'], y=plot['y'],
                                xerr=plot['x_err'],
                                ecolor=plot['ebar']['color'],
                                elinewidth=plot['ebar']['linew'],
                                capsize=plot['ebar']['capsize'],
                                capthick=plot['ebar']['capthick'],
                                color=plot['line']['color'],
                                linestyle=linestyle,
                                linewidth=plot['line']['width'],
                                marker=marker_type,
                                markeredgecolor=plot['marker']['edge_col'],
                                markeredgewidth=plot['marker']['edge_wid'],
                                markerfacecolor=plot['marker']['face_col'],
                                markersize=plot['marker']['size'],
                                label=plot['label'],
                                alpha=plot['line']['alpha'])
                        if len(plot['x_err']) == 0:
                            if plot['line']['exist'] == 1:
                                linestyle = plot['line']['style']
                            else: 
                                linestyle = ''
                            if plot['marker']['exist'] == 1:
                                marker_type = plot['marker']['type']
                            else: 
                                marker_type = 'None'
                            ax[count].errorbar(
                                x=plot['x'], y=plot['y'],
                                yerr=plot['y_err'],
                                ecolor=plot['ebar']['color'],
                                elinewidth=plot['ebar']['linew'],
                                capsize=plot['ebar']['capsize'],
                                capthick=plot['ebar']['capthick'],
                                color=plot['line']['color'],
                                linestyle=linestyle,
                                linewidth=plot['line']['width'],
                                marker=marker_type,
                                markeredgecolor=plot['marker']['edge_col'],
                                markeredgewidth=plot['marker']['edge_wid'],
                                markerfacecolor=plot['marker']['face_col'],
                                markersize=plot['marker']['size'],
                                label=plot['label'],
                                alpha=plot['line']['alpha'])
                        if (len(plot['x_err']) != 0) and (len(plot['y_err']) != 0):
                            if plot['line']['exist'] == 1:
                                linestyle = plot['line']['style']
                            else: 
                                linestyle = ''
                            if plot['marker']['exist'] == 1:
                                marker_type = plot['marker']['type']
                            else: 
                                marker_type = 'None'
                            ax[count].errorbar(
                                x=plot['x'], y=plot['y'],
                                yerr=plot['y_err'], xerr=plot['x_err'],
                                ecolor=plot['ebar']['color'],
                                elinewidth=plot['ebar']['linew'],
                                capsize=plot['ebar']['capsize'],
                                capthick=plot['ebar']['capthick'],
                                color=plot['line']['color'],
                                linestyle=linestyle,
                                linewidth=plot['line']['width'],
                                marker=marker_type,
                                markeredgecolor=plot['marker']['edge_col'],
                                markeredgewidth=plot['marker']['edge_wid'],
                                markerfacecolor=plot['marker']['face_col'],
                                markersize=plot['marker']['size'],
                                label=plot['label'],
                                alpha=plot['line']['alpha'])
                        label_length += 'label'
                    else:
                        if plot['line']['exist'] == 1:
                            linestyle = plot['line']['style']
                        else: 
                            linestyle = ''
                        if plot['marker']['exist'] == 1:
                            marker_type = plot['marker']['type']
                        else: 
                            marker_type = 'None'
                        ax[count].plot(
                            plot['x'], plot['y'],
                            color=plot['line']['color'],
                            linestyle=linestyle,
                            linewidth=plot['line']['width'],
                            marker=marker_type,
                            markeredgecolor=plot['marker']['edge_col'],
                            markeredgewidth=plot['marker']['edge_wid'],
                            markerfacecolor=plot['marker']['face_col'],
                            markersize=plot['marker']['size'],
                            label=plot['label'],
                            alpha=plot['line']['alpha'])
                        label_length += 'label'

            style = ['normal', 'italic']
            weight = ['normal', 'bold']
            scale = ['linear', 'log']
            # if colorbar == 1:
                # cbar_map.append(cm.ScalarMappable(norm=color, cmap=color_map))
                # cbar_axis.append(ax[count])
            ax[count].set_xlim(data['x_lim'])
            ax[count].set_ylim(data['y_lim'])
            ax[count].set_xscale(scale[data['xscale']])
            ax[count].set_yscale(scale[data['yscale']])
            ax[count].tick_params(labelsize=data['axis_text']['size']-3)
            if data['xticks'] == 0:
                ax[count].set_xticks([], [])
            if data['yticks'] == 0:
                ax[count].set_yticks([], [])
            ax[count].set_xlabel(
                data['x_label'], fontsize=data['axis_text']['size'],
                fontstyle=style[data['axis_text']['Italic']],
                fontweight=weight[data['axis_text']['Bold']])
            ax[count].set_ylabel(
                data['y_label'], fontsize=data['axis_text']['size'],
                fontstyle=style[data['axis_text']['Italic']],
                fontweight=weight[data['axis_text']['Bold']])
            ax[count].set_title(
                data['title'], fontsize=data['title_text']['size'],
                fontstyle=style[data['title_text']['Italic']],
                fontweight=weight[data['title_text']['Bold']])
            if label_length != '':
                if data['legend'] != 'None':
                    ax[count].legend(loc=data['legend'],
                                     fontsize=data['legendFontSize'])
            count += 1
        if len(cbar_map) > 0:
            for i in range(len(cbar_map)):
                self.fig.colorbar(cbar_map[i], ax=cbar_axis[i])
        self.fig.set_dpi(150)
        self.fig.show()

    def show_plot2(self):
        label_length = ''
        cbar_map = []
        cbar_axis = []
        colorbar = 0
        for axis in self.axis_list:
            data = self.axis_data[axis]
            self.axis_names[data['position'][0]][data['position'][1]] = axis

        last_row = self.axis_names[len(self.axis_names)-1]
        first_col = []

        for i in range(self.rows):
            first_col.append(self.axis_names[i][0])

        for i in range(self.rows):
            for j in range(self.cols):
                if self.axis_names[i][j] != '':
                    label_length = ''
                    data = self.axis_data[self.axis_names[i][j]]
                    try:
                        if self.sharex == 1:
                            if self.sharey == 1:
                                if self.axis_names[i][j] in last_row:
                                    if self.axis_names[i][j] in first_col:
                                        y_label = self.axis_data[self.axis_names[i][j]]['y_label']
                                        x_label = self.axis_data[self.axis_names[i][j]]['x_label']
                                        x_lim = self.axis_data[self.axis_names[i][j]]['x_lim']
                                        y_lim = self.axis_data[self.axis_names[i][j]]['y_lim']
                                        x_scale = self.axis_data[self.axis_names[i][j]]['xscale']
                                        y_scale = self.axis_data[self.axis_names[i][j]]['yscale']
                                    else:
                                        y_label = ''
                                        y_lim = self.axis_data[self.axis_names[i][0]]['y_lim']
                                        x_label = self.axis_data[self.axis_names[i][j]]['x_label']
                                        x_lim = self.axis_data[self.axis_names[i][j]]['x_lim']
                                        x_scale = self.axis_data[self.axis_names[i][j]]['xscale']
                                        y_scale = self.axis_data[self.axis_names[i][0]]['yscale']

                                else:
                                    if self.axis_names[i][j] in first_col:
                                        y_label = self.axis_data[self.axis_names[i][j]]['y_label']
                                        y_lim = self.axis_data[self.axis_names[i][j]]['y_lim']
                                        x_label = ''
                                        x_lim = self.axis_data[self.axis_names[len(self.axis_names)-1][j]]['x_lim']
                                        x_scale = self.axis_data[self.axis_names[len(self.axis_names)-1][j]]['xscale']
                                        y_scale = self.axis_data[self.axis_names[i][j]]['yscale']
                                    else:
                                        y_label = ''
                                        y_lim = self.axis_data[self.axis_names[i][0]]['y_lim']
                                        x_label = ''
                                        x_lim = self.axis_data[self.axis_names[len(self.axis_names)-1][j]]['x_lim']
                                        x_scale = self.axis_data[self.axis_names[len(self.axis_names)-1][j]]['xscale']
                                        y_scale = self.axis_data[self.axis_names[i][0]]['yscale']
                            else:
                                if self.axis_names[i][j] in last_row:
                                    y_label = self.axis_data[self.axis_names[i][j]]['y_label']
                                    x_label = self.axis_data[self.axis_names[i][j]]['x_label']
                                    x_lim = self.axis_data[self.axis_names[i][j]]['x_lim']
                                    y_lim = self.axis_data[self.axis_names[i][j]]['y_lim']
                                    x_scale = self.axis_data[self.axis_names[i][j]]['xscale']
                                    y_scale = self.axis_data[self.axis_names[i][j]]['yscale']
                                else:
                                    y_label = self.axis_data[self.axis_names[i][j]]['y_label']
                                    y_lim = self.axis_data[self.axis_names[i][j]]['y_lim']
                                    x_label = ''
                                    x_lim = self.axis_data[self.axis_names[len(self.axis_names)-1][j]]['x_lim']
                                    x_scale = self.axis_data[self.axis_names[len(self.axis_names)-1][j]]['xscale']
                                    y_scale = self.axis_data[self.axis_names[i][j]]['yscale']
                        else:
                            if self.sharey == 1:
                                if self.axis_names[i][j] in first_col:
                                    y_label = self.axis_data[self.axis_names[i][j]]['y_label']
                                    x_label = self.axis_data[self.axis_names[i][j]]['x_label']
                                    x_lim = self.axis_data[self.axis_names[i][j]]['x_lim']
                                    y_lim = self.axis_data[self.axis_names[i][j]]['y_lim']
                                    x_scale = self.axis_data[self.axis_names[i][j]]['xscale']
                                    y_scale = self.axis_data[self.axis_names[i][j]]['yscale']
                                else:
                                    y_label = ''
                                    y_lim = self.axis_data[self.axis_names[i][0]]['y_lim']
                                    x_label = self.axis_data[self.axis_names[i][j]]['x_label']
                                    x_lim = self.axis_data[self.axis_names[i][j]]['x_lim']
                                    x_scale = self.axis_data[self.axis_names[i][j]]['xscale']
                                    y_scale = self.axis_data[self.axis_names[i][0]]['yscale']
                            else:
                                y_label = self.axis_data[self.axis_names[i][j]]['y_label']
                                x_label = self.axis_data[self.axis_names[i][j]]['x_label']
                                x_lim = self.axis_data[self.axis_names[i][j]]['x_lim']
                                y_lim = self.axis_data[self.axis_names[i][j]]['y_lim']
                                x_scale = self.axis_data[self.axis_names[i][j]]['xscale']
                                y_scale = self.axis_data[self.axis_names[i][j]]['yscale']
                    except:
                        # print(e.args)
                        messagebox.showerror(title='Plot error',
                                             message='Error encountered plotting figure. Ensure plots with shared x or shared y have matching columns or rows.')
                        return

                    self.axes[i][j] = self.fig.add_subplot(
                        self.gs[data['position'][0]:data['position'][0]+data['position'][2],
                                data['position'][1]:data['position'][1]+data['position'][3]])
                    for plot_num in range(len(data['plots'])):
                        plot = data['plots_data'][plot_num]

                        if plot['fill']['exist'] == 1 and len(plot['dif_top']) > 0:
                            self.axes[i][j].fill_between(np.array(plot['x']),
                                                         np.array(plot['y'])+np.array(plot['dif_top']),
                                                         np.array(plot['y'])-np.array(plot['dif_bot']),
                                                         alpha=plot['fill']['alpha'],
                                                         edgecolor=plot['fill']['edge_col'],
                                                         facecolor=plot['fill']['face_col'],
                                                         linewidth=plot['fill']['line_wid'],
                                                         linestyle=plot['fill']['line_sty'],
                                                         label=plot['fill-label'])
                            label_length += 'label'

                        no_err_data = (plot['y_err'].size == 0 and plot['x_err'].size == 0)
                        if plot['scatter']['exist'] == 1:
                            if plot['colorbar'] == 1:
                                colorbar = 1
                            else:
                                colorbar = 0
                            # set cmap
                            color_map = plt.get_cmap(plot['scatter']['cmap'])
                            # check for color vector
                            if plot['scatter']['current_color'] == 'None':
                                color = plot['marker']['face_col']
                                colorbar = 0
                            else:
                                col_index = plot['scatter']['color_vector_names'].index(plot['scatter']['current_color'])
                                color = np.array(plot['scatter']['color_vectors'][col_index])

                            # check for size vector
                            if plot['scatter']['current_size'] == 'None':
                                size = plot['marker']['size']**2
                            else:
                                sz_index = plot['scatter']['size_vector_names'].index(plot['scatter']['current_size'])
                                size = np.array(plot['scatter']['size_vectors'][sz_index])
                                size = ((size-size.min())/(size.max()-size.min()))*20*plot['marker']['size']
                            cset = self.axes[i][j].scatter(x=plot['x'], y=plot['y'],
                                                           s=size,
                                                           c=color,
                                                           marker=plot['scatter']['type'],
                                                           alpha=plot['scatter']['alpha'],
                                                           edgecolors=plot['scatter']['edge'],
                                                           linewidths=plot['marker']['edge_wid'],
                                                           cmap=color_map)
                            if colorbar == 1:
                                cbar_map.append(cset)
                                cbar_axis.append(self.axes[i][j])

                        else:
                            if plot['ebar']['exist'] == 1 and not no_err_data:
                                if plot['line']['exist'] == 1:
                                    linestyle = plot['line']['style']
                                else: 
                                    linestyle = ''
                                if plot['marker']['exist'] == 1:
                                    marker_type = plot['marker']['type']
                                else: 
                                    marker_type = 'None'
                                if len(plot['y_err']) == 0:
                                    #plot['y_err'] = np.zeros_like(np.array(plot['y']))
                                    self.axes[i][j].errorbar(
                                        x=plot['x'], y=plot['y'],
                                        xerr=plot['x_err'],
                                        ecolor=plot['ebar']['color'],
                                        elinewidth=plot['ebar']['linew'],
                                        capsize=plot['ebar']['capsize'],
                                        capthick=plot['ebar']['capthick'],
                                        color=plot['line']['color'],
                                        linestyle=linestyle,
                                        linewidth=plot['line']['width'],
                                        marker=marker_type,
                                        markeredgecolor=plot['marker']['edge_col'],
                                        markeredgewidth=plot['marker']['edge_wid'],
                                        markerfacecolor=plot['marker']['face_col'],
                                        markersize=plot['marker']['size'],
                                        label=plot['label'],
                                        alpha=plot['line']['alpha'])
                                if len(plot['x_err']) == 0:
                                    #plot['x_err'] = np.zeros_like(np.array(plot['x']))
                                    self.axes[i][j].errorbar(
                                        x=plot['x'], y=plot['y'],
                                        yerr=plot['y_err'],
                                        ecolor=plot['ebar']['color'],
                                        elinewidth=plot['ebar']['linew'],
                                        capsize=plot['ebar']['capsize'],
                                        capthick=plot['ebar']['capthick'],
                                        color=plot['line']['color'],
                                        linestyle=linestyle,
                                        linewidth=plot['line']['width'],
                                        marker=marker_type,
                                        markeredgecolor=plot['marker']['edge_col'],
                                        markeredgewidth=plot['marker']['edge_wid'],
                                        markerfacecolor=plot['marker']['face_col'],
                                        markersize=plot['marker']['size'],
                                        label=plot['label'],
                                        alpha=plot['line']['alpha'])
                                if (len(plot['x_err']) != 0) and (len(plot['y_err']) != 0):
                                    self.axes[i][j].errorbar(
                                        x=plot['x'], y=plot['y'],
                                        yerr=plot['y_err'], xerr=plot['x_err'],
                                        ecolor=plot['ebar']['color'],
                                        elinewidth=plot['ebar']['linew'],
                                        capsize=plot['ebar']['capsize'],
                                        capthick=plot['ebar']['capthick'],
                                        color=plot['line']['color'],
                                        linestyle=linestyle,
                                        linewidth=plot['line']['width'],
                                        marker=marker_type,
                                        markeredgecolor=plot['marker']['edge_col'],
                                        markeredgewidth=plot['marker']['edge_wid'],
                                        markerfacecolor=plot['marker']['face_col'],
                                        markersize=plot['marker']['size'],
                                        label=plot['label'],
                                        alpha=plot['line']['alpha'])
                                label_length += 'label'
                            else:
                                if plot['line']['exist'] == 1:
                                    linestyle = plot['line']['style']
                                else: 
                                    linestyle = ''
                                if plot['marker']['exist'] == 1:
                                    marker_type = plot['marker']['type']
                                else: 
                                    marker_type = 'None'
                                self.axes[i][j].plot(
                                    plot['x'], plot['y'],
                                    color=plot['line']['color'],
                                    linestyle=linestyle,
                                    linewidth=plot['line']['width'],
                                    marker=marker_type,
                                    markeredgecolor=plot['marker']['edge_col'],
                                    markeredgewidth=plot['marker']['edge_wid'],
                                    markerfacecolor=plot['marker']['face_col'],
                                    markersize=plot['marker']['size'],
                                    label=plot['label'],
                                    alpha=plot['line']['alpha'])
                                label_length += 'label'

                    style = ['normal', 'italic']
                    weight = ['normal', 'bold']
                    scale = ['linear', 'log']
                    self.axes[i][j].set_xlim(x_lim)
                    self.axes[i][j].set_ylim(y_lim)
                    self.axes[i][j].set_xscale(scale[x_scale])
                    self.axes[i][j].set_yscale(scale[y_scale])
                    self.axes[i][j].tick_params(labelsize=data['axis_text']['size']-3)
                    if data['xticks'] == 0:
                        self.axes[i][j].set_xticks([], [])
                    if data['yticks'] == 0:
                        self.axes[i][j].set_yticks([], [])
                    self.axes[i][j].set_xlabel(
                        x_label,
                        fontsize=data['axis_text']['size'],
                        fontstyle=style[data['axis_text']['Italic']],
                        fontweight=weight[data['axis_text']['Bold']])
                    self.axes[i][j].set_ylabel(
                        y_label,
                        fontsize=data['axis_text']['size'],
                        fontstyle=style[data['axis_text']['Italic']],
                        fontweight=weight[data['axis_text']['Bold']])
                    self.axes[i][j].set_title(
                        data['title'],
                        fontsize=data['title_text']['size'],
                        fontstyle=style[data['title_text']['Italic']],
                        fontweight=weight[data['title_text']['Bold']])
                    if label_length != '':
                        if data['legend'] != 'None':
                            self.axes[i][j].legend(loc=data['legend'],
                                                   fontsize=data['legendFontSize'])
        if len(cbar_map) > 0:
            for i in range(len(cbar_map)):
                self.fig.colorbar(cbar_map[i], ax=cbar_axis[i])
        self.fig.set_dpi(150)
        self.fig.show()


    def save_plot(self):
        label_length = ''
        cbar_map = []
        cbar_axis = []
        ax = []
        count = 0
        for axis in self.axis_list:
            data = self.axis_data[axis]
            ax.append(self.fig.add_subplot(
                self.gs[data['position'][0]:data['position'][0]+data['position'][2],
                        data['position'][1]:data['position'][1]+data['position'][3]]))
            colorbar = 0
            for plot_num in range(len(data['plots'])):
                plot = data['plots_data'][plot_num]

                if plot['fill']['exist'] == 1 and len(plot['dif_top']) > 0:
                    ax[count].fill_between(
                        np.array(plot['x']),
                        np.array(plot['y'])+np.array(plot['dif_top']),
                        np.array(plot['y'])-np.array(plot['dif_bot']),
                        alpha=plot['fill']['alpha'],
                        edgecolor=plot['fill']['edge_col'],
                        facecolor=plot['fill']['face_col'],
                        linewidth=plot['fill']['line_wid'],
                        linestyle=plot['fill']['line_sty'],
                        label=plot['fill-label'])
                    label_length += 'label'

                no_err_data = (plot['y_err'].size == 0 and plot['x_err'].size == 0)
                if plot['scatter']['exist'] == 1:
                    if plot['colorbar'] == 1:
                        colorbar = 1
                    else:
                        colorbar = 0
                    # set cmap
                    color_map = plt.get_cmap(plot['scatter']['cmap'])
                    # check for color vector
                    if plot['scatter']['current_color'] == 'None':
                        color = plot['marker']['face_col']
                        colorbar = 0
                    else:
                        col_index = plot['scatter']['color_vector_names'].index(plot['scatter']['current_color'])
                        color = np.array(plot['scatter']['color_vectors'][col_index])

                    # check for size vector
                    if plot['scatter']['current_size'] == 'None':
                        size = plot['marker']['size']**2
                    else:
                        sz_index = plot['scatter']['size_vector_names'].index(plot['scatter']['current_size'])
                        size = np.array(plot['scatter']['size_vectors'][sz_index])
                        size = ((size-size.min())/(size.max()-size.min()))*20*plot['marker']['size']

                    cset = ax[count].scatter(x=plot['x'], y=plot['y'],
                                             s=size,
                                             c=color,
                                             marker=plot['scatter']['type'],
                                             alpha=plot['scatter']['alpha'],
                                             edgecolors=plot['scatter']['edge'],
                                             linewidths=plot['marker']['edge_wid'],
                                             cmap=color_map)
                    if colorbar == 1:
                        cbar_map.append(cset)
                        cbar_axis.append(ax[count])
                else:
                    if plot['ebar']['exist'] == 1 and not no_err_data:
                        if plot['line']['exist'] == 1:
                            linestyle = plot['line']['style']
                        else: 
                            linestyle = ''
                        if plot['marker']['exist'] == 1:
                            marker_type = plot['marker']['type']
                        else: 
                            marker_type = 'None'
                        if len(plot['y_err']) == 0:
                            #plot['y_err'] = np.zeros_like(np.array(plot['y']))
                            ax[count].errorbar(
                                x=plot['x'], y=plot['y'],
                                xerr=plot['x_err'],
                                ecolor=plot['ebar']['color'],
                                elinewidth=plot['ebar']['linew'],
                                capsize=plot['ebar']['capsize'],
                                capthick=plot['ebar']['capthick'],
                                color=plot['line']['color'],
                                linestyle=linestyle,
                                linewidth=plot['line']['width'],
                                marker=marker_type,
                                markeredgecolor=plot['marker']['edge_col'],
                                markeredgewidth=plot['marker']['edge_wid'],
                                markerfacecolor=plot['marker']['face_col'],
                                markersize=plot['marker']['size'],
                                label=plot['label'],
                                alpha=plot['line']['alpha'])
                        if len(plot['x_err']) == 0:
                            #plot['x_err'] = np.zeros_like(np.array(plot['x']))
                            ax[count].errorbar(
                                x=plot['x'], y=plot['y'],
                                yerr=plot['y_err'],
                                ecolor=plot['ebar']['color'],
                                elinewidth=plot['ebar']['linew'],
                                capsize=plot['ebar']['capsize'],
                                capthick=plot['ebar']['capthick'],
                                color=plot['line']['color'],
                                linestyle=linestyle,
                                linewidth=plot['line']['width'],
                                marker=marker_type,
                                markeredgecolor=plot['marker']['edge_col'],
                                markeredgewidth=plot['marker']['edge_wid'],
                                markerfacecolor=plot['marker']['face_col'],
                                markersize=plot['marker']['size'],
                                label=plot['label'],
                                alpha=plot['line']['alpha'])
                        if (len(plot['x_err']) != 0) and (len(plot['y_err']) != 0):
                            ax[count].errorbar(
                                x=plot['x'], y=plot['y'],
                                yerr=plot['y_err'], xerr=plot['x_err'],
                                ecolor=plot['ebar']['color'],
                                elinewidth=plot['ebar']['linew'],
                                capsize=plot['ebar']['capsize'],
                                capthick=plot['ebar']['capthick'],
                                color=plot['line']['color'],
                                linestyle=linestyle,
                                linewidth=plot['line']['width'],
                                marker=marker_type,
                                markeredgecolor=plot['marker']['edge_col'],
                                markeredgewidth=plot['marker']['edge_wid'],
                                markerfacecolor=plot['marker']['face_col'],
                                markersize=plot['marker']['size'],
                                label=plot['label'],
                                alpha=plot['line']['alpha'])
                        label_length += 'label'
                    else:
                        if plot['line']['exist'] == 1:
                            linestyle = plot['line']['style']
                        else: 
                            linestyle = ''
                        if plot['marker']['exist'] == 1:
                            marker_type = plot['marker']['type']
                        else: 
                            marker_type = 'None'
                        ax[count].plot(
                            plot['x'], plot['y'],
                            color=plot['line']['color'],
                            linestyle=linestyle,
                            linewidth=plot['line']['width'],
                            marker=marker_type,
                            markeredgecolor=plot['marker']['edge_col'],
                            markeredgewidth=plot['marker']['edge_wid'],
                            markerfacecolor=plot['marker']['face_col'],
                            markersize=plot['marker']['size'],
                            label=plot['label'],
                            alpha=plot['line']['alpha'])
                        label_length += 'label'

            style = ['normal', 'italic']
            weight = ['normal', 'bold']
            scale = ['linear', 'log']
            # if colorbar == 1:
                # cbar_map.append(cm.ScalarMappable(norm=color, cmap=color_map))
                # cbar_axis.append(ax[count])
            ax[count].set_xlim(data['x_lim'])
            ax[count].set_ylim(data['y_lim'])
            ax[count].set_xscale(scale[data['xscale']])
            ax[count].set_yscale(scale[data['yscale']])
            ax[count].tick_params(labelsize=data['axis_text']['size']-3)
            if data['xticks'] == 0:
                ax[count].set_xticks([], [])
            if data['yticks'] == 0:
                ax[count].set_yticks([], [])
            ax[count].set_xlabel(
                data['x_label'], fontsize=data['axis_text']['size'],
                fontstyle=style[data['axis_text']['Italic']],
                fontweight=weight[data['axis_text']['Bold']])
            ax[count].set_ylabel(
                data['y_label'], fontsize=data['axis_text']['size'],
                fontstyle=style[data['axis_text']['Italic']],
                fontweight=weight[data['axis_text']['Bold']])
            ax[count].set_title(
                data['title'], fontsize=data['title_text']['size'],
                fontstyle=style[data['title_text']['Italic']],
                fontweight=weight[data['title_text']['Bold']])
            if label_length != '':
                if data['legend'] != 'None':
                    ax[count].legend(loc=data['legend'],
                                     fontsize=data['legendFontSize'])
            count += 1
        if len(cbar_map) > 0:
            for i in range(len(cbar_map)):
                self.fig.colorbar(cbar_map[i], ax=cbar_axis[i])
        self.fig.set_dpi(600)
        self.fig.savefig(self.save_fname)
        save_dir_list = self.save_fname.split('/')
        save_dir = ''
        for i in range(len(save_dir_list)-1):
            save_dir += save_dir_list[i] + '/'
        np.save("{}plot_data.npy".format(save_dir), self.axis_dict)
        write_code_file(save_dir, 'save_plot')

    def save_plot2(self):
        label_length = ''
        cbar_map = []
        cbar_axis = []
        for axis in self.axis_list:
            data = self.axis_data[axis]
            self.axis_names[data['position'][0]][data['position'][1]] = axis

        last_row = self.axis_names[len(self.axis_names)-1]
        first_col = []

        for i in range(self.rows):
            first_col.append(self.axis_names[i][0])

        for i in range(self.rows):
            for j in range(self.cols):
                if self.axis_names[i][j] != '':
                    label_length = ''
                    data = self.axis_data[self.axis_names[i][j]]
                    try:
                        if self.sharex == 1:
                            if self.sharey == 1:
                                if self.axis_names[i][j] in last_row:
                                    if self.axis_names[i][j] in first_col:
                                        y_label = self.axis_data[self.axis_names[i][j]]['y_label']
                                        x_label = self.axis_data[self.axis_names[i][j]]['x_label']
                                        x_lim = self.axis_data[self.axis_names[i][j]]['x_lim']
                                        y_lim = self.axis_data[self.axis_names[i][j]]['y_lim']
                                        x_scale = self.axis_data[self.axis_names[i][j]]['xscale']
                                        y_scale = self.axis_data[self.axis_names[i][j]]['yscale']
                                    else:
                                        y_label = ''
                                        y_lim = self.axis_data[self.axis_names[i][0]]['y_lim']
                                        x_label = self.axis_data[self.axis_names[i][j]]['x_label']
                                        x_lim = self.axis_data[self.axis_names[i][j]]['x_lim']
                                        x_scale = self.axis_data[self.axis_names[i][j]]['xscale']
                                        y_scale = self.axis_data[self.axis_names[i][0]]['yscale']

                                else:
                                    if self.axis_names[i][j] in first_col:
                                        y_label = self.axis_data[self.axis_names[i][j]]['y_label']
                                        y_lim = self.axis_data[self.axis_names[i][j]]['y_lim']
                                        x_label = ''
                                        x_lim = self.axis_data[self.axis_names[len(self.axis_names)-1][j]]['x_lim']
                                        x_scale = self.axis_data[self.axis_names[len(self.axis_names)-1][j]]['xscale']
                                        y_scale = self.axis_data[self.axis_names[i][j]]['yscale']
                                    else:
                                        y_label = ''
                                        y_lim = self.axis_data[self.axis_names[i][0]]['y_lim']
                                        x_label = ''
                                        x_lim = self.axis_data[self.axis_names[len(self.axis_names)-1][j]]['x_lim']
                                        x_scale = self.axis_data[self.axis_names[len(self.axis_names)-1][j]]['xscale']
                                        y_scale = self.axis_data[self.axis_names[i][0]]['yscale']
                            else:
                                if self.axis_names[i][j] in last_row:
                                    y_label = self.axis_data[self.axis_names[i][j]]['y_label']
                                    x_label = self.axis_data[self.axis_names[i][j]]['x_label']
                                    x_lim = self.axis_data[self.axis_names[i][j]]['x_lim']
                                    y_lim = self.axis_data[self.axis_names[i][j]]['y_lim']
                                    x_scale = self.axis_data[self.axis_names[i][j]]['xscale']
                                    y_scale = self.axis_data[self.axis_names[i][j]]['yscale']
                                else:
                                    y_label = self.axis_data[self.axis_names[i][j]]['y_label']
                                    y_lim = self.axis_data[self.axis_names[i][j]]['y_lim']
                                    x_label = ''
                                    x_lim = self.axis_data[self.axis_names[len(self.axis_names)-1][j]]['x_lim']
                                    x_scale = self.axis_data[self.axis_names[len(self.axis_names)-1][j]]['xscale']
                                    y_scale = self.axis_data[self.axis_names[i][j]]['yscale']
                        else:
                            if self.sharey == 1:
                                if self.axis_names[i][j] in first_col:
                                    y_label = self.axis_data[self.axis_names[i][j]]['y_label']
                                    x_label = self.axis_data[self.axis_names[i][j]]['x_label']
                                    x_lim = self.axis_data[self.axis_names[i][j]]['x_lim']
                                    y_lim = self.axis_data[self.axis_names[i][j]]['y_lim']
                                    x_scale = self.axis_data[self.axis_names[i][j]]['xscale']
                                    y_scale = self.axis_data[self.axis_names[i][j]]['yscale']
                                else:
                                    y_label = ''
                                    y_lim = self.axis_data[self.axis_names[i][0]]['y_lim']
                                    x_label = self.axis_data[self.axis_names[i][j]]['x_label']
                                    x_lim = self.axis_data[self.axis_names[i][j]]['x_lim']
                                    x_scale = self.axis_data[self.axis_names[i][j]]['xscale']
                                    y_scale = self.axis_data[self.axis_names[i][0]]['yscale']
                            else:
                                y_label = self.axis_data[self.axis_names[i][j]]['y_label']
                                x_label = self.axis_data[self.axis_names[i][j]]['x_label']
                                x_lim = self.axis_data[self.axis_names[i][j]]['x_lim']
                                y_lim = self.axis_data[self.axis_names[i][j]]['y_lim']
                                x_scale = self.axis_data[self.axis_names[i][j]]['xscale']
                                y_scale = self.axis_data[self.axis_names[i][j]]['yscale']
                    except:
                        # print(e.args)
                        messagebox.showerror(title='Plot error',
                                             message='Error encountered plotting figure. Ensure plots with shared x or shared y have matching columns or rows.')
                        return

                    self.axes[i][j] = self.fig.add_subplot(
                        self.gs[data['position'][0]:data['position'][0]+data['position'][2],
                                data['position'][1]:data['position'][1]+data['position'][3]])
                    for plot_num in range(len(data['plots'])):
                        plot = data['plots_data'][plot_num]

                        if plot['fill']['exist'] == 1 and len(plot['dif_top']) > 0:
                            self.axes[i][j].fill_between(
                                np.array(plot['x']),
                                np.array(plot['y'])+np.array(plot['dif_top']),
                                np.array(plot['y'])-np.array(plot['dif_bot']),
                                alpha=plot['fill']['alpha'],
                                edgecolor=plot['fill']['edge_col'],
                                facecolor=plot['fill']['face_col'],
                                linewidth=plot['fill']['line_wid'],
                                linestyle=plot['fill']['line_sty'],
                                label=plot['fill-label'])
                            label_length += 'label'

                        no_err_data = (plot['y_err'].size == 0 and plot['x_err'].size == 0)
                        if plot['scatter']['exist'] == 1:
                            if plot['colorbar'] == 1:
                                colorbar = 1
                            else:
                                colorbar = 0
                            # set cmap
                            color_map = plt.get_cmap(plot['scatter']['cmap'])
                            # check for color vector
                            if plot['scatter']['current_color'] == 'None':
                                color = plot['marker']['face_col']
                                colorbar = 0
                            else:
                                col_index = plot['scatter']['color_vector_names'].index(plot['scatter']['current_color'])
                                color = np.array(plot['scatter']['color_vectors'][col_index])

                            # check for size vector
                            if plot['scatter']['current_size'] == 'None':
                                size = plot['marker']['size']**2
                            else:
                                sz_index = plot['scatter']['size_vector_names'].index(plot['scatter']['current_size'])
                                size = np.array(plot['scatter']['size_vectors'][sz_index])
                                size = ((size-size.min())/(size.max()-size.min()))*20*plot['marker']['size']
                            cset = self.axes[i][j].scatter(
                                x=plot['x'], y=plot['y'],
                                s=size, c=color,
                                marker=plot['scatter']['type'],
                                alpha=plot['scatter']['alpha'],
                                edgecolors=plot['scatter']['edge'],
                                linewidths=plot['marker']['edge_wid'],
                                cmap=color_map)
                            if colorbar == 1:
                                cbar_map.append(cset)
                                cbar_axis.append(self.axes[i][j])

                        else:
                            if plot['ebar']['exist'] == 1 and not no_err_data:
                                if plot['line']['exist'] == 1:
                                    linestyle = plot['line']['style']
                                else: 
                                    linestyle = ''
                                if plot['marker']['exist'] == 1:
                                    marker_type = plot['marker']['type']
                                else: 
                                    marker_type = 'None'
                                if len(plot['y_err']) == 0:
                                    #plot['y_err'] = np.zeros_like(np.array(plot['y']))
                                    self.axes[i][j].errorbar(
                                        x=plot['x'], y=plot['y'],
                                        xerr=plot['x_err'],
                                        ecolor=plot['ebar']['color'],
                                        elinewidth=plot['ebar']['linew'],
                                        capsize=plot['ebar']['capsize'],
                                        capthick=plot['ebar']['capthick'],
                                        color=plot['line']['color'],
                                        linestyle=linestyle,
                                        linewidth=plot['line']['width'],
                                        marker=marker_type,
                                        markeredgecolor=plot['marker']['edge_col'],
                                        markeredgewidth=plot['marker']['edge_wid'],
                                        markerfacecolor=plot['marker']['face_col'],
                                        markersize=plot['marker']['size'],
                                        label=plot['label'],
                                        alpha=plot['line']['alpha'])
                                if len(plot['x_err']) == 0:
                                    #plot['x_err'] = np.zeros_like(np.array(plot['x']))
                                    self.axes[i][j].errorbar(
                                        x=plot['x'], y=plot['y'],
                                        yerr=plot['y_err'],
                                        ecolor=plot['ebar']['color'],
                                        elinewidth=plot['ebar']['linew'],
                                        capsize=plot['ebar']['capsize'],
                                        capthick=plot['ebar']['capthick'],
                                        color=plot['line']['color'],
                                        linestyle=linestyle,
                                        linewidth=plot['line']['width'],
                                        marker=marker_type,
                                        markeredgecolor=plot['marker']['edge_col'],
                                        markeredgewidth=plot['marker']['edge_wid'],
                                        markerfacecolor=plot['marker']['face_col'],
                                        markersize=plot['marker']['size'],
                                        label=plot['label'],
                                        alpha=plot['line']['alpha'])
                                if (len(plot['x_err']) != 0) and (len(plot['y_err']) != 0):
                                    self.axes[i][j].errorbar(
                                        x=plot['x'], y=plot['y'],
                                        yerr=plot['y_err'], xerr=plot['x_err'],
                                        ecolor=plot['ebar']['color'],
                                        elinewidth=plot['ebar']['linew'],
                                        capsize=plot['ebar']['capsize'],
                                        capthick=plot['ebar']['capthick'],
                                        color=plot['line']['color'],
                                        linestyle=linestyle,
                                        linewidth=plot['line']['width'],
                                        marker=marker_type,
                                        markeredgecolor=plot['marker']['edge_col'],
                                        markeredgewidth=plot['marker']['edge_wid'],
                                        markerfacecolor=plot['marker']['face_col'],
                                        markersize=plot['marker']['size'],
                                        label=plot['label'],
                                        alpha=plot['line']['alpha'])
                                label_length += 'label'
                            else:
                                if plot['line']['exist'] == 1:
                                    linestyle = plot['line']['style']
                                else: 
                                    linestyle = ''
                                if plot['marker']['exist'] == 1:
                                    marker_type = plot['marker']['type']
                                else: 
                                    marker_type = 'None'
                                self.axes[i][j].plot(
                                    plot['x'], plot['y'],
                                    color=plot['line']['color'],
                                    linestyle=linestyle,
                                    linewidth=plot['line']['width'],
                                    marker=marker_type,
                                    markeredgecolor=plot['marker']['edge_col'],
                                    markeredgewidth=plot['marker']['edge_wid'],
                                    markerfacecolor=plot['marker']['face_col'],
                                    markersize=plot['marker']['size'],
                                    label=plot['label'],
                                    alpha=plot['line']['alpha'])
                                label_length += 'label'

                    style = ['normal', 'italic']
                    weight = ['normal', 'bold']
                    scale = ['linear', 'log']
                    self.axes[i][j].set_xlim(x_lim)
                    self.axes[i][j].set_ylim(y_lim)
                    self.axes[i][j].set_xscale(scale[x_scale])
                    self.axes[i][j].set_yscale(scale[y_scale])
                    self.axes[i][j].tick_params(labelsize=data['axis_text']['size']-3)
                    if data['xticks'] == 0:
                        self.axes[i][j].set_xticks([], [])
                    if data['yticks'] == 0:
                        self.axes[i][j].set_yticks([], [])
                    self.axes[i][j].set_xlabel(
                        x_label,
                        fontsize=data['axis_text']['size'],
                        fontstyle=style[data['axis_text']['Italic']],
                        fontweight=weight[data['axis_text']['Bold']])
                    self.axes[i][j].set_ylabel(
                        y_label,
                        fontsize=data['axis_text']['size'],
                        fontstyle=style[data['axis_text']['Italic']],
                        fontweight=weight[data['axis_text']['Bold']])
                    self.axes[i][j].set_title(
                        data['title'],
                        fontsize=data['title_text']['size'],
                        fontstyle=style[data['title_text']['Italic']],
                        fontweight=weight[data['title_text']['Bold']])
                    if label_length != '':
                        if data['legend'] != 'None':
                            self.axes[i][j].legend(loc=data['legend'],
                                                   fontsize=data['legendFontSize'])
        if len(cbar_map) > 0:
            for i in range(len(cbar_map)):
                self.fig.colorbar(cbar_map[i], ax=cbar_axis[i])
        self.fig.set_dpi(600)
        self.fig.savefig(self.save_fname)
        save_dir_list = self.save_fname.split('/')
        save_dir = ''
        for i in range(len(save_dir_list)-1):
            save_dir += save_dir_list[i] + '/'
        np.save("{}plot_data.npy".format(save_dir), self.axis_dict)
        write_code_file(save_dir, 'save_plot2')


class plotEditor():
    def __init__(self, x=[], y=[], x_err=[], y_err=[], fill=[],
                 fill_alt=[], labels=[]):
        self.x = x
        self.y = y
        if x_err == []:
            self.x_err = []
            for i in range(len(x)):
                self.x_err.append([])
        else:
            self.x_err = x_err
        if y_err == []:
            self.y_err = []
            for i in range(len(x)):
                self.y_err.append([])
        else:
            self.y_err = y_err
        if fill == []:
            self.dif_top = []
            for i in range(len(x)):
                self.dif_top.append([])
        else:
            self.dif_top = fill
        if fill_alt == []:
            self.dif_bot = self.dif_top
        else:
            self.dif_bot = fill_alt
        if labels == []:
            self.labels = []
            for i in range(len(x)):
                self.labels.append('')
        else:
            self.labels = []
            for i in range(len(x)):
                self.labels.append(labels[i].replace(' ', '-'))

        self.same_vectors = []
        self.same_vector_names = []

        for i in range(len(x)):
            self.same_vectors.append([[]])
            self.same_vector_names.append(['None'])
            for j in range(len(x)):
                if len(self.x[i]) == len(self.x[j]):
                    self.same_vectors[i].append(self.x[j])
                    self.same_vector_names[i].append("{}-{}".format('x', 
                                                                    self.labels[j][:10]))
                if len(self.x[i]) == len(self.y[j]):
                    self.same_vectors[i].append(self.y[j])
                    self.same_vector_names[i].append("{}-{}".format('y', 
                                                                    self.labels[j][:10]))
                if len(self.x[i]) == len(self.x_err[j]):
                    self.same_vectors[i].append(self.x_err[j])
                    self.same_vector_names[i].append("{}-{}".format('x_err', 
                                                                    self.labels[j][:10]))
                if len(self.x[i]) == len(self.y_err[j]):
                    self.same_vectors[i].append(self.y_err[j])
                    self.same_vector_names[i].append("{}-{}".format('y_err', 
                                                                    self.labels[j][:10]))
                if len(self.x[i]) == len(self.dif_top[j]):
                    self.same_vectors[i].append(self.dif_top[j])
                    self.same_vector_names[i].append("{}-{}".format('fill', 
                                                                    self.labels[j][:10]))
                if len(self.x[i]) == len(self.dif_bot[j]):
                    self.same_vectors[i].append(self.dif_bot[j])
                    self.same_vector_names[i].append("{}-{}".format('fill_alt', 
                                                                    self.labels[j][:10]))


        try:
            self.__check_input()
        except Exception as e:
            root = tk.Tk()
            messagebox.showerror("Startup",
                                 "Failed to Initialize tool:\n{}".format(e))
            root.destroy()
            raise ValueError("Inputs not fully specified")
        self.__initialize_plot()


    def __initialize_plot(self):
        line_col = ['#000000', '#0000FF', '#00FF00', '#FF0000', '#FF00FF',
                    '#FFFF00', '#00FFFF', '#44AAFF', '#AA44FF', '#FFAA44']
        col_count = 0
        plot_data_Dict = {}
        for i in range(len(self.x)):
            if (len(self.x_err[i]) > 0) or (len(self.y_err[i]) > 0):
                ebar = 1
            else:
                ebar = 0
            if len(self.dif_top[i]) > 0:
                fill = 1
            else:
                fill = 0
            plot_data_Dict[self.labels[i]] = {
                'label': self.labels[i].replace('-',' '),
                'fill-label': '{} fill'.format(self.labels[i].replace('-',' ')),
                'x': self.x[i],
                'y': self.y[i],
                'y_err':self.y_err[i],
                'x_err':self.x_err[i],
                'dif_top':self.dif_top[i],
                'dif_bot':self.dif_bot[i],
                'ebar':{'exist':ebar,
                        'color':line_col[col_count],
                        'linew':1,
                        'capsize':1,
                        'capthick':1},
                'line':{'exist':1,
                        'color':line_col[col_count],
                        'style':'-',
                        'width':2,
                        'alpha':1.0},
                'marker':{'exist':1,
                          'type':'.',
                          'edge_col':line_col[col_count],
                          'edge_wid':1,
                          'face_col':line_col[col_count],
                          'size':10},
                'fill':{'exist':fill,
                        'alpha':0.5,
                        'edge_col':line_col[col_count],
                        'face_col':line_col[col_count],
                        'line_sty':'-',
                        'line_wid':1},
                'scatter':{'exist':0,
                           'type':'.',
                           'color_vector_names':self.same_vector_names[i],
                           'color_vectors':self.same_vectors[i],
                           'current_color':self.same_vector_names[i][0],
                           'size_vector_names':self.same_vector_names[i],
                           'size_vectors':self.same_vectors[i],
                           'current_size':self.same_vector_names[i][0],
                           'cmap':'viridis',
                           'edge':'none',
                           'alpha':0.5},
                'colorbar':1}
            col_count += 1
            if col_count == 10:
                col_count = 0
        self.root = tk.Tk()
        self.root.title('Matplotlib Post Processor')
        #root.iconbitmap(bitmap='Main.ico')
        self.root.resizable(0, 0)
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        app = window(plot_data_Dict, master=self.root)
        app['bg'] = BG_BLUE
        app.mainloop()

    def __check_input(self):
        if self.x == []:
            raise ValueError('List of X data must be provided')
        if self.y == []:
            raise ValueError('List of Y data must be provided')

        temp_labels = []
        for ii in range(len(self.x)):
            try:
                temp_labels.append(self.labels[ii])
            except IndexError:
                temp_labels.append('')
            try:
                # Convert all inputs to Numpy arrays, raise an error if this fails
                try:
                    self.x[ii] = np.array(self.x[ii])
                    self.y[ii] = np.array(self.y[ii])
                    self.x_err[ii] = np.array(self.x_err[ii])
                    self.y_err[ii] = np.array(self.y_err[ii])
                    self.dif_top[ii] = np.array(self.dif_top[ii])
                    self.dif_bot[ii] = np.array(self.dif_bot[ii])
                except:
                    raise ValueError('Unable to convert inputs to Numpy Arrays')

                if (len(self.x[ii].shape) != 1) or (len(self.x[ii].shape) != 1) or \
                    (len(self.x[ii].shape) != 1) or (len(self.x[ii].shape) != 1) or \
                    (len(self.x[ii].shape) != 1) or (len(self.x[ii].shape) != 1):
                    raise ValueError('All inputs must be vectors | Index {}'.format(ii))
                # check that all inputs have the same length or are empty if allowed
                if (self.y[ii].shape != self.x[ii].shape) and (self.y[ii].shape[0] != 0):
                    raise ValueError('X and Y vectors must be same shape | Index {}'.format(ii))
                if (self.x_err[ii].shape != self.x[ii].shape) and (self.x_err[ii].shape[0] != 0):
                    raise ValueError('X-Error vector must be empty or same shape as X | Index {}'.format(ii))
                if (self.y_err[ii].shape != self.x[ii].shape) and (self.y_err[ii].shape[0] != 0):
                    raise ValueError('Y-Error vector must be empty or same shape as X | Index {}'.format(ii))
                if (self.dif_top[ii].shape != self.x[ii].shape) and (self.dif_top[ii].shape[0] != 0):
                    raise ValueError('Fill-Top vector must be empty or same shape as X | Index {}'.format(ii))
                if (self.dif_bot[ii].shape != self.x[ii].shape) and (self.dif_bot[ii].shape[0] != 0):
                    raise ValueError('Fill-Bottom vector must be empty or same shape as X | Index {}'.format(ii))
            except IndexError:
                raise IndexError('All input lists must be the same length')
        self.labels = temp_labels

    def callback(self):
        if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
            plt.close(1)
            self.root.destroy()


if __name__ == "__main__":
    """
    Test cases for the code sequentially test each situation that could arise
    For each test, the code generates the post processor window and the user
    should click --SHOW PLOT-- and --SAVE PLOT-- buttons and then close the window
    to continue on to the next test.

    The output in the console from this procedure should be:

    #################################################
    Test Case 1: Full data
    Test Case 1 Successful!
    #################################################
    Test Case 2: leave out error data
    Test Case 2 Successful!
    #################################################
    Test Case 3: leave out fill data
    Test Case 3 Successful!
    #################################################
    Test Case 4: leave out fill_alt data
    Test Case 4 Successful!
    #################################################
    Test Case 5: leave out labels
    No handles with labels found to put in legend.
    Test Case 5 Successful!
    #################################################
    Test Case 6: leave out y
    Test Case 6 Failed: List of Y data must be provided
    #################################################
    Test Case 7: leave out x
    Test Case 7 Failed: List of X data must be provided
    #################################################
    Test Case 8: x[0] has missing data
    Test Case 8 Failed: X and Y vectors must be same shape | Index 0
    #################################################
    Test Case 9: y[0] has missing data
    Test Case 9 Failed: X and Y vectors must be same shape | Index 0
    #################################################
    Test Case 10: x_err[1] has missing data
    Test Case 10 Failed: X-Error vector must be empty or same shape as X | Index 1
    #################################################
    Test Case 11: y_err[1] has missing data
    Test Case 11 Failed: Y-Error vector must be empty or same shape as X | Index 1
    #################################################
    Test Case 12: fill[0] has missing data
    Test Case 12 Failed: Fill-Top vector must be empty or same shape as X | Index 1
    #################################################
    Test Case 13: fill_alt[0] has missing data
    Test Case 13 Failed: Fill-Bottom vector must be empty or same shape as X | Index 1
    #################################################
    Test Case 14: labels has missing data
    Test Case 14 Successful!
    """
    x_data = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    y_data = [[0.00, 0.84, 0.91, 0.14, -0.76, -0.96, -0.28, 0.66, 0.99, 0.41, -0.54],
              [1.00, 0.90, 0.82, 0.74, 0.67, 0.61, 0.55, 0.50, 0.45, 0.41, 0.37]]
    x_err_data = [[], [0.1, 0.1, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.1, 0.1, 0.05]]
    y_err_data = [[], [0.1, 0.1, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.1, 0.1, 0.05]]
    fill_data = [[], [0.1, 0.1, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.1, 0.1, 0.05]]
    fill_alt_data = [[], [0.3, 0.3, 0.6, 0.6, 0.9, 0.9, 0.6, 0.6, 0.3, 0.3, 0.15]]
    labels_data = ['Experimental', 'Computation']
    
    plotEditor(x=x_data, y=y_data, x_err=x_err_data,
               y_err=y_err_data, fill=fill_data,
               fill_alt=fill_alt_data, labels=labels_data)

    # check_run_test = input("Do you wish to run the test cases (Y/N)?   ")

    # x_data = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    # y_data = [[0.00, 0.84, 0.91, 0.14, -0.76, -0.96, -0.28, 0.66, 0.99, 0.41, -0.54],
    #           [1.00, 0.90, 0.82, 0.74, 0.67, 0.61, 0.55, 0.50, 0.45, 0.41, 0.37]]
    # x_err_data = [[], [0.1, 0.1, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.1, 0.1, 0.05]]
    # y_err_data = [[], [0.1, 0.1, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.1, 0.1, 0.05]]
    # fill_data = [[], [0.1, 0.1, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.1, 0.1, 0.05]]
    # fill_alt_data = [[], [0.3, 0.3, 0.6, 0.6, 0.9, 0.9, 0.6, 0.6, 0.3, 0.3, 0.15]]
    # labels_data = ['Experimental', 'Computation']

    # if check_run_test in ['Y', 'y']:
    #     for iii in range(14):
    #         test_case = iii+1

    #         if test_case == 1:
    #             print("#################################################")
    #             print("Test Case 1: Full data")
    #             try:
    #                 plotEditor(x=x_data, y=y_data, x_err=x_err_data,
    #                            y_err=y_err_data, fill=fill_data,
    #                            fill_alt=fill_alt_data, labels=labels_data)
    #                 print("Test Case 1 Successful!")
    #             except Exception as e:
    #                 print("Test Case 1 Failed: {}".format(e))
    #         elif test_case == 2:
    #             print("#################################################")
    #             print("Test Case 2: leave out error data")
    #             try:
    #                 plotEditor(x=x_data, y=y_data, x_err=x_err_data,
    #                            y_err=y_err_data, fill=fill_data,
    #                            fill_alt=fill_alt_data, labels=labels_data)
    #                 print("Test Case 2 Successful!")
    #             except Exception as e:
    #                 print("Test Case 2 Failed: {}".format(e))
    #         elif test_case == 3:
    #             print("#################################################")
    #             print("Test Case 3: leave out fill data")
    #             try:
    #                 plotEditor(x=x_data, y=y_data, x_err=x_err_data,
    #                            y_err=y_err_data, fill=fill_data,
    #                            fill_alt=fill_alt_data, labels=labels_data)
    #                 print("Test Case 3 Successful!")
    #             except Exception as e:
    #                 print("Test Case 3 Failed: {}".format(e))
    #         elif test_case == 4:
    #             print("#################################################")
    #             print("Test Case 4: leave out fill_alt data")
    #             try:
    #                 plotEditor(x=x_data, y=y_data, x_err=x_err_data,
    #                            y_err=y_err_data, fill=fill_data,
    #                            fill_alt=fill_alt_data, labels=labels_data)
    #                 print("Test Case 4 Successful!")
    #             except Exception as e:
    #                 print("Test Case 4 Failed: {}".format(e))
    #         elif test_case == 5:
    #             print("#################################################")
    #             print("Test Case 5: leave out labels")
    #             try:
    #                 plotEditor(x=x_data, y=y_data, x_err=x_err_data,
    #                            y_err=y_err_data, fill=fill_data,
    #                            fill_alt=fill_alt_data, labels=labels_data)
    #                 print("Test Case 5 Successful!")
    #             except Exception as e:
    #                 print("Test Case 5 Failed: {}".format(e))
    #         elif test_case == 6:
    #             print("#################################################")
    #             print("Test Case 6: leave out y")
    #             try:
    #                 plotEditor(x=x_data, y=y_data, x_err=x_err_data,
    #                            y_err=y_err_data, fill=fill_data,
    #                            fill_alt=fill_alt_data, labels=labels_data)
    #                 print("Test Case 6 Successful!")
    #             except Exception as e:
    #                 print("Test Case 6 Failed: {}".format(e))
    #         elif test_case == 7:
    #             print("#################################################")
    #             print("Test Case 7: leave out x")
    #             try:
    #                 plotEditor(x=x_data, y=y_data, x_err=x_err_data,
    #                            y_err=y_err_data, fill=fill_data,
    #                            fill_alt=fill_alt_data, labels=labels_data)
    #                 print("Test Case 7 Successful!")
    #             except Exception as e:
    #                 print("Test Case 7 Failed: {}".format(e))
    #         elif test_case == 8:
    #             print("#################################################")
    #             print("Test Case 8: x[0] has missing data")
    #             try:
    #                 x_data = [[0,1,2,3,4,5,6,7,8], [0,1,2,3,4,5,6,7,8,9,10]]
    #                 y_data = [[0.00,0.84,0.91,0.14,-0.76,-0.96,-0.28,0.66,0.99,0.41,-0.54],[1.00,0.90,0.82,0.74,0.67,0.61,0.55,0.50,0.45,0.41,0.37]]
    #                 x_err_data = [[],[0.1,0.1,0.2,0.2,0.3,0.3,0.2,0.2,0.1,0.1,0.05]]
    #                 y_err_data = [[],[0.1,0.1,0.2,0.2,0.3,0.3,0.2,0.2,0.1,0.1,0.05]]
    #                 fill_data = [[],[0.1,0.1,0.2,0.2,0.3,0.3,0.2,0.2,0.1,0.1,0.05]]
    #                 fill_alt_data = [[],[0.1,0.1,0.2,0.2,0.3,0.3,0.2,0.2,0.1,0.1,0.05]]
    #                 labels_data = ['Experimental','Computation']
    #                 plotEditor(x=x_data, y=y_data, x_err=x_err_data,
    #                             y_err=y_err_data, fill=fill_data,
    #                             fill_alt=fill_alt_data, labels=labels_data)
    #                 print("Test Case 8 Successful!")
    #             except Exception as e:
    #                 print("Test Case 8 Failed: {}".format(e))
    #         elif test_case == 9:
    #             print("#################################################")
    #             print("Test Case 9: y[0] has missing data")
    #             try:
    #                 x_data = [[0,1,2,3,4,5,6,7,8,9,10], [0,1,2,3,4,5,6,7,8,9,10]]
    #                 y_data = [[0.00,0.84,0.91,0.14,-0.76,-0.96,-0.28,0.66,0.99],[1.00,0.90,0.82,0.74,0.67,0.61,0.55,0.50,0.45,0.41,0.37]]
    #                 x_err_data = [[],[0.1,0.1,0.2,0.2,0.3,0.3,0.2,0.2,0.1,0.1,0.05]]
    #                 y_err_data = [[],[0.1,0.1,0.2,0.2,0.3,0.3,0.2,0.2,0.1,0.1,0.05]]
    #                 fill_data = [[],[0.1,0.1,0.2,0.2,0.3,0.3,0.2,0.2,0.1,0.1,0.05]]
    #                 fill_alt_data = [[],[0.1,0.1,0.2,0.2,0.3,0.3,0.2,0.2,0.1,0.1,0.05]]
    #                 labels_data = ['Experimental','Computation']
    #                 plotEditor(x=x_data, y=y_data, x_err=x_err_data,
    #                             y_err=y_err_data, fill=fill_data,
    #                             fill_alt=fill_alt_data, labels=labels_data)
    #                 print("Test Case 9 Successful!")
    #             except Exception as e:
    #                 print("Test Case 9 Failed: {}".format(e))
    #         elif test_case == 10:
    #             print("#################################################")
    #             print("Test Case 10: x_err[1] has missing data")
    #             try:
    #                 x_data = [[0,1,2,3,4,5,6,7,8,9,10], [0,1,2,3,4,5,6,7,8,9,10]]
    #                 y_data = [[0.00,0.84,0.91,0.14,-0.76,-0.96,-0.28,0.66,0.99,0.41,-0.54],[1.00,0.90,0.82,0.74,0.67,0.61,0.55,0.50,0.45,0.41,0.37]]
    #                 x_err_data = [[],[0.1,0.1,0.2,0.2,0.3,0.3,0.2,0.2,0.1]]
    #                 y_err_data = [[],[0.1,0.1,0.2,0.2,0.3,0.3,0.2,0.2,0.1,0.1,0.05]]
    #                 fill_data = [[],[0.1,0.1,0.2,0.2,0.3,0.3,0.2,0.2,0.1,0.1,0.05]]
    #                 fill_alt_data = [[],[0.1,0.1,0.2,0.2,0.3,0.3,0.2,0.2,0.1,0.1,0.05]]
    #                 labels_data = ['Experimental','Computation']
    #                 plotEditor(x=x_data, y=y_data, x_err=x_err_data,
    #                             y_err=y_err_data, fill=fill_data,
    #                             fill_alt=fill_alt_data, labels=labels_data)
    #                 print("Test Case 10 Successful!")
    #             except Exception as e:
    #                 print("Test Case 10 Failed: {}".format(e))
    #         elif test_case == 11:
    #             print("#################################################")
    #             print("Test Case 11: y_err[1] has missing data")
    #             try:
    #                 x_data = [[0,1,2,3,4,5,6,7,8,9,10], [0,1,2,3,4,5,6,7,8,9,10]]
    #                 y_data = [[0.00,0.84,0.91,0.14,-0.76,-0.96,-0.28,0.66,0.99,0.41,-0.54],[1.00,0.90,0.82,0.74,0.67,0.61,0.55,0.50,0.45,0.41,0.37]]
    #                 x_err_data = [[],[0.1,0.1,0.2,0.2,0.3,0.3,0.2,0.2,0.1,0.1,0.05]]
    #                 y_err_data = [[],[0.1,0.1,0.2,0.2,0.3,0.3,0.2,0.2,0.1]]
    #                 fill_data = [[],[0.1,0.1,0.2,0.2,0.3,0.3,0.2,0.2,0.1,0.1,0.05]]
    #                 fill_alt_data = [[],[0.1,0.1,0.2,0.2,0.3,0.3,0.2,0.2,0.1,0.1,0.05]]
    #                 labels_data = ['Experimental','Computation']
    #                 plotEditor(x=x_data, y=y_data, x_err=x_err_data,
    #                             y_err=y_err_data, fill=fill_data,
    #                             fill_alt=fill_alt_data, labels=labels_data)
    #                 print("Test Case 11 Successful!")
    #             except Exception as e:
    #                 print("Test Case 11 Failed: {}".format(e))
    #         elif test_case == 12:
    #             print("#################################################")
    #             print("Test Case 12: fill[0] has missing data")
    #             try:
    #                 x_data = [[0,1,2,3,4,5,6,7,8,9,10], [0,1,2,3,4,5,6,7,8,9,10]]
    #                 y_data = [[0.00,0.84,0.91,0.14,-0.76,-0.96,-0.28,0.66,0.99,0.41,-0.54],[1.00,0.90,0.82,0.74,0.67,0.61,0.55,0.50,0.45,0.41,0.37]]
    #                 x_err_data = [[],[0.1,0.1,0.2,0.2,0.3,0.3,0.2,0.2,0.1,0.1,0.05]]
    #                 y_err_data = [[],[0.1,0.1,0.2,0.2,0.3,0.3,0.2,0.2,0.1,0.1,0.05]]
    #                 fill_data = [[],[0.1,0.1,0.2,0.2,0.3,0.3,0.2,0.2,0.1]]
    #                 fill_alt_data = [[],[0.1,0.1,0.2,0.2,0.3,0.3,0.2,0.2,0.1,0.1,0.05]]
    #                 labels_data = ['Experimental','Computation']
    #                 plotEditor(x=x_data, y=y_data, x_err=x_err_data,
    #                             y_err=y_err_data, fill=fill_data,
    #                             fill_alt=fill_alt_data, labels=labels_data)
    #                 print("Test Case 12 Successful!")
    #             except Exception as e:
    #                 print("Test Case 12 Failed: {}".format(e))
    #         elif test_case == 13:
    #             print("#################################################")
    #             print("Test Case 13: fill_alt[0] has missing data")
    #             try:
    #                 x_data = [[0,1,2,3,4,5,6,7,8,9,10], [0,1,2,3,4,5,6,7,8,9,10]]
    #                 y_data = [[0.00,0.84,0.91,0.14,-0.76,-0.96,-0.28,0.66,0.99,0.41,-0.54],[1.00,0.90,0.82,0.74,0.67,0.61,0.55,0.50,0.45,0.41,0.37]]
    #                 x_err_data = [[],[0.1,0.1,0.2,0.2,0.3,0.3,0.2,0.2,0.1,0.1,0.05]]
    #                 y_err_data = [[],[0.1,0.1,0.2,0.2,0.3,0.3,0.2,0.2,0.1,0.1,0.05]]
    #                 fill_data = [[],[0.1,0.1,0.2,0.2,0.3,0.3,0.2,0.2,0.1,0.1,0.05]]
    #                 fill_alt_data = [[],[0.1,0.1,0.2,0.2,0.3,0.3,0.2,0.2,0.1]]
    #                 labels_data = ['Experimental','Computation']
    #                 plotEditor(x=x_data, y=y_data, x_err=x_err_data,
    #                             y_err=y_err_data, fill=fill_data,
    #                             fill_alt=fill_alt_data, labels=labels_data)
    #                 print("Test Case 13 Successful!")
    #             except Exception as e:
    #                 print("Test Case 13 Failed: {}".format(e))
    #         elif test_case == 14:
    #             print("#################################################")
    #             print("Test Case 14: labels has missing data")
    #             try:
    #                 x_data = [[0,1,2,3,4,5,6,7,8,9,10], [0,1,2,3,4,5,6,7,8,9,10]]
    #                 y_data = [[0.00,0.84,0.91,0.14,-0.76,-0.96,-0.28,0.66,0.99,0.41,-0.54],[1.00,0.90,0.82,0.74,0.67,0.61,0.55,0.50,0.45,0.41,0.37]]
    #                 x_err_data = [[],[0.1,0.1,0.2,0.2,0.3,0.3,0.2,0.2,0.1,0.1,0.05]]
    #                 y_err_data = [[],[0.1,0.1,0.2,0.2,0.3,0.3,0.2,0.2,0.1,0.1,0.05]]
    #                 fill_data = [[],[0.1,0.1,0.2,0.2,0.3,0.3,0.2,0.2,0.1,0.1,0.05]]
    #                 fill_alt_data = [[],[0.1,0.1,0.2,0.2,0.3,0.3,0.2,0.2,0.1,0.1,0.05]]
    #                 labels_data = ['Experimental']
    #                 plotEditor(x=x_data, y=y_data, x_err=x_err_data,
    #                             y_err=y_err_data, fill=fill_data,
    #                             fill_alt=fill_alt_data, labels=labels_data)
    #                 print("Test Case 14 Successful!")
    #             except Exception as e:
    #                 print("Test Case 14 Failed: {}".format(e))
    # else:
        # plotEditor(x=x_data, y=y_data, x_err=x_err_data,
        #                         y_err=y_err_data, fill=fill_data,
        #                         fill_alt=fill_alt_data, labels=labels_data)
