# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 09:42:45 2020

@author: richardcouperthwaite
"""

import tkinter as tk
try:    
    from .util import set_axis_data, set_plot_data
except ImportError:
    from util import set_axis_data, set_plot_data

BG_BLUE = '#409fff'
BG_GREEN = '#6AD535'
BG_RED = '#F22140'

def create_GUI(window):
    window.axis_dict = {}
    window.data_list = ['']
    window.axis_list = ['']
    window.dat_lab = tk.StringVar()
    window.dat_lab2 = tk.StringVar()
    window.current_data = tk.StringVar()
    window.multi_select = tk.IntVar()
    window.multi_list = tk.StringVar()
    window.selected_data_value = ''
    window.selected_axis_value = ''
    window.ebar_exist = tk.IntVar()
    window.ebar_color = tk.StringVar()
    window.ebar_linew = tk.IntVar()
    window.ebar_caps = tk.IntVar()
    window.ebar_capt = tk.IntVar()
    window.line_exist = tk.IntVar()
    window.line_color = tk.StringVar()
    window.line_style = tk.StringVar()
    window.line_width = tk.IntVar()
    window.styles = [':', '-.', '--', '-', '']
    window.line_alpha = tk.DoubleVar()
    window.mark_exist = tk.IntVar()
    window.mark_type = tk.StringVar()
    window.mark_ec = tk.StringVar()
    window.mark_ew = tk.IntVar()
    window.mark_fc = tk.StringVar()
    window.mark_sz = tk.IntVar()
    window.mark_space = tk.IntVar()
    window.marker_types = [".", ",", "o", "v", "^", "<", ">", "1", "2", "3",
                         "4", "8", "s", "p", "P", "*", "h", "H", "+", "x",
                         "X", "D", "d", "|", "_", "None"]
    window.fill_exist = tk.IntVar()
    window.fill_alpha = tk.DoubleVar()
    window.fill_ec = tk.StringVar()
    window.fill_fc = tk.StringVar()
    window.fill_linew = tk.IntVar()
    window.fill_lines = tk.StringVar()
    window.scat_exist = tk.IntVar()
    window.scat_type = tk.StringVar()
    window.scat_color_list = ['']
    window.scat_size_list = ['']
    window.scat_color = tk.StringVar()
    window.scat_size = tk.StringVar()
    window.scat_faces = ['none', 'face', 'blue', 'green',
                       'red', 'cyan', 'magenta', 'yellow',
                       'black', 'white']
    window.scat_edge = tk.StringVar()
    window.scat_alpha = tk.DoubleVar()
    window.cmap_list = ['viridis', 'plasma', 'inferno', 'magma', 'ocean',
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
    window.cb_exist = tk.IntVar()
    window.cmap_pick = tk.StringVar()
    window.cmap_pick.set('viridis')
    window.gridrow = tk.IntVar()
    window.gridcol = tk.IntVar()
    window.sharex = tk.IntVar()
    window.sharey = tk.IntVar()
    window.alldat_selected = tk.StringVar()
    window.seldat_selected = tk.StringVar()
    window.selected_axis_data = ['']
    window.current_axis = tk.StringVar()
    window.axrow = tk.IntVar()
    window.axcol = tk.IntVar()
    window.axrowspan = tk.IntVar()
    window.axcolspan = tk.IntVar()
    window.xlab = tk.StringVar()
    window.ylab = tk.StringVar()
    window.axsize = tk.DoubleVar()
    window.xlimlow = tk.DoubleVar()
    window.xlimhi = tk.DoubleVar()
    window.xticks = tk.IntVar()
    window.xlog = tk.IntVar()
    window.ylimlow = tk.DoubleVar()
    window.ylimhi = tk.DoubleVar()
    window.yticks = tk.IntVar()
    window.ylog = tk.IntVar()
    window.axbold = tk.IntVar()
    window.axitalic = tk.IntVar()
    window.title = tk.StringVar()
    window.tsize = tk.DoubleVar()
    window.tbold = tk.IntVar()
    window.titalic = tk.IntVar()
    window.legend = tk.StringVar()
    window.lgSize = tk.DoubleVar()
    window.legend_pos_list = ['best', 'None', 'upper left', 'upper center',
                            'upper right', 'center left', 'center',
                            'center right', 'lower left', 'lower center',
                            'lower right']
    # Call the function to obtain the initial values for all the variables
    # defined above and set the axis count to 1 since this will create the
    # first axis
    __populate_variables(window)
    window.axis_count = 1
    # Create the Grid object for the layout of the window
    window.grid()
    # populate the window with the widgets
    __create_widgets(window)
    set_plot_data(window, window.data_list[0])

def __create_widgets(window):
    #************************************************************#
    #************************************************************#
    # Create a frame to hold the plot details information
    window.plotsFrame = tk.LabelFrame(window, text='Plot Details',
                                    labelanchor='nw', height='100',
                                    width='300', bg=BG_BLUE,
                                    font=('URW Bookman L', '12', 'bold'))
    window.plotsFrame.grid(row=0, column=0, columnspan=3, rowspan=2,
                         padx=10, pady=4, sticky=tk.W+tk.E)

    #************************************************************#
    #************************************************************#
    window.data_sel_frame = tk.Frame(window.plotsFrame, bg=BG_BLUE)
    window.data_sel_frame.grid(row=0, column=0, rowspan=2)

    # Option menu for selecting the current set of data
    window.data_select = tk.OptionMenu(window.data_sel_frame, window.current_data,
                                     *window.data_list,
                                     command=window.plot_changed)
    window.data_select['bg'] = BG_BLUE
    window.data_select['activebackground'] = BG_BLUE
    window.data_select['width'] = '20'
    window.data_select['height'] = '1'
    window.data_select['borderwidth'] = '1'
    window.data_select['pady'] = '1'
    window.data_select['padx'] = '2'
    window.data_select['relief'] = tk.RAISED
    window.data_select['anchor'] = tk.W
    window.data_select['highlightthickness'] = '0'
    window.data_select.grid(row=0, column=0, columnspan=3, sticky=tk.W+tk.E,
                          padx=0)

    window.label = tk.Label(window.data_sel_frame, text='Multiple:', bg=BG_BLUE,
                          font=('URW Bookman L', '10', 'bold'))
    window.label.grid(row=1, column=0)
    window.multi_select_check = tk.Checkbutton(window.data_sel_frame,
                                             variable=window.multi_select,
                                             bg=BG_BLUE,
                                             activebackground=BG_BLUE,
                                             command=window.multi_select_finish)
    window.multi_select_check.grid(row=1, column=1)
    window.multi_clear = tk.Button(window.data_sel_frame,
                                 bg=BG_BLUE, text='Clear Selection',
                                 activebackground=BG_BLUE,
                                 font=('URW Bookman L', '10', 'bold'),
                                 command=window.clear_multi_choice)
    window.multi_clear.grid(row=1, column=2, pady=3, padx=1)

    window.selection_list = tk.Listbox(window.data_sel_frame,
                                      exportselection=0,
                                      listvariable=window.multi_list,
                                      selectmode=tk.MULTIPLE,
                                      activestyle='none')
    window.selection_list.grid(row=2, column=0, columnspan=3, sticky=tk.W+tk.E,
                              padx=1, pady=3)

    # New frame for Data Labels
    window.data_labels_frame = tk.Frame(window.plotsFrame, bg=BG_BLUE)
    window.data_labels_frame.grid(row=0, column=1)

    # Input EntryBox for Data Label
    window.label = tk.Label(window.data_labels_frame, text='Data Label:', bg=BG_BLUE,
                          font=('URW Bookman L', '10', 'bold'))
    window.label.grid(row=0, column=2, columnspan=2, padx=5)
    window.data_label = tk.Entry(window.data_labels_frame, textvariable=window.dat_lab,
                               width='45')
    window.data_label.grid(row=0, column=4, columnspan=2, padx=5)
    # Input EntryBox for the Fill data Label
    window.label = tk.Label(window.data_labels_frame, text='Fill Label:', bg=BG_BLUE,
                          font=('URW Bookman L', '10', 'bold'))
    window.label.grid(row=0, column=6, columnspan=2, padx=5)
    window.data_label = tk.Entry(window.data_labels_frame, textvariable=window.dat_lab2,
                               width='45')
    window.data_label.grid(row=0, column=8, columnspan=2, padx=5)
    #************************************************************#
    #************************************************************#
    window.plot_options_frame = tk.Frame(window.plotsFrame, bg=BG_BLUE)
    window.plot_options_frame.grid(row=1, column=1)

    # Window Frame for the Errorbar Data
    window.ebar_dat = tk.LabelFrame(window.plot_options_frame, text='Error Bar',
                                  labelanchor='n', bg=BG_BLUE,
                                  font=('URW Bookman L', '11', 'bold'),
                                  height=235, width=165)
    window.ebar_dat.grid(row=0, column=0, columnspan=2, padx=1)
    window.ebar_dat.grid_propagate(0)
    # CheckBox for whether to show errobars
    window.label = tk.Label(window.ebar_dat, text='Error Bar?:', bg=BG_BLUE,
                          font=('URW Bookman L', '10', 'bold'))
    window.label.grid(row=0, column=0, padx=5, pady=2)
    window.ebar_exist_check = tk.Checkbutton(window.ebar_dat,
                                           variable=window.ebar_exist,
                                           bg=BG_BLUE,
                                           activebackground=BG_BLUE,
                                           command=window.other_plot_select)
    window.ebar_exist_check.grid(row=0, column=1, padx=5, pady=2)
    # Errorbar color selection
    window.label = tk.Label(window.ebar_dat, text='Color:', bg=BG_BLUE,
                          font=('URW Bookman L', '10', 'bold'))
    window.label.grid(row=1, column=0, padx=5, pady=2)
    window.eb_col = tk.Button(window.ebar_dat, text='',
                            bg=window.ebar_color.get(),
                            activebackground=window.ebar_color.get(),
                            font=('URW Bookman L', '10', 'bold'),
                            command=window.ebar_col_h)
    window.eb_col.grid(row=1, column=1, padx=5, pady=2, sticky=tk.W+tk.E)
    # Errorbar linewidth
    window.label = tk.Label(window.ebar_dat, text='Width:', bg=BG_BLUE,
                          font=('URW Bookman L', '10', 'bold'))
    window.label.grid(row=2, column=0, padx=5, pady=2)
    window.eb_lw = tk.Spinbox(window.ebar_dat, textvariable=window.ebar_linew,
                            width='5', from_=1, to=100, increment=1)
    window.eb_lw.grid(row=2, column=1, padx=5, pady=2)

    window.label = tk.Label(window.ebar_dat, text='Error Bar Cap:', bg=BG_BLUE,
                          font=('URW Bookman L', '10', 'underline'))
    window.label.grid(row=3, column=0, columnspan=2, padx=5, pady=2)

    # Errorbar Cap Size
    window.label = tk.Label(window.ebar_dat, text='Size:', bg=BG_BLUE,
                          font=('URW Bookman L', '10', 'bold'))
    window.label.grid(row=4, column=0, padx=5, pady=2)
    window.eb_cs = tk.Spinbox(window.ebar_dat, textvariable=window.ebar_caps,
                            width='5', from_=1, to=100, increment=1)
    window.eb_cs.grid(row=4, column=1, padx=5, pady=2)
    # Errorbar Cap Thickness
    window.label = tk.Label(window.ebar_dat, text='Thickness:', bg=BG_BLUE,
                          font=('URW Bookman L', '10', 'bold'))
    window.label.grid(row=5, column=0, padx=5, pady=2)
    window.eb_ct = tk.Spinbox(window.ebar_dat, textvariable=window.ebar_capt,
                            width='5', from_=1, to=100, increment=1)
    window.eb_ct.grid(row=5, column=1, padx=5, pady=2)
    #************************************************************#
    #************************************************************#

    window.line_dat = tk.LabelFrame(window.plot_options_frame, text='Line',
                                  labelanchor='n', bg=BG_BLUE,
                                  font=('URW Bookman L', '11', 'bold'),
                                  height=235, width=140)
    window.line_dat.grid(row=0, column=2, columnspan=2, padx=1)
    window.line_dat.grid_propagate(0)

    window.label = tk.Label(window.line_dat, text='Line?:', bg=BG_BLUE,
                          font=('URW Bookman L', '10', 'bold'))
    window.label.grid(row=0, column=0, padx=5, pady=2)

    window.line_exist_check = tk.Checkbutton(window.line_dat,
                                           variable=window.line_exist,
                                           bg=BG_BLUE,
                                           activebackground=BG_BLUE,
                                           command=window.other_plot_select)
    window.line_exist_check.grid(row=0, column=1, padx=5, pady=2)

    window.label = tk.Label(window.line_dat, text='Color:', bg=BG_BLUE,
                          font=('URW Bookman L', '10', 'bold'))
    window.label.grid(row=1, column=0, padx=5, pady=2)
    window.l_col = tk.Button(window.line_dat, text='',
                           bg=window.line_color.get(),
                           activebackground=window.line_color.get(),
                           font=('URW Bookman L', '10', 'bold'),
                           command=window.line_col_h)
    window.l_col.grid(row=1, column=1, padx=5, pady=2, sticky=tk.W+tk.E)

    window.label = tk.Label(window.line_dat, text='Style:', bg=BG_BLUE,
                          font=('URW Bookman L', '10', 'bold'))
    window.label.grid(row=2, column=0, padx=5, pady=2)
    window.l_sty = tk.OptionMenu(window.line_dat, window.line_style,
                               *window.styles)
    window.l_sty['bg'] = BG_BLUE
    window.l_sty['activebackground'] = BG_BLUE
    window.l_sty['width'] = '3'
    window.l_sty['height'] = '1'
    window.l_sty['borderwidth'] = '1'
    window.l_sty['pady'] = '1'
    window.l_sty['padx'] = '2'
    window.l_sty['relief'] = tk.RAISED
    window.l_sty['anchor'] = tk.W
    window.l_sty['highlightthickness'] = '0'
    window.l_sty.grid(row=2, column=1, padx=5, pady=2)

    window.label = tk.Label(window.line_dat, text='Width:', bg=BG_BLUE,
                          font=('URW Bookman L', '10', 'bold'))
    window.label.grid(row=3, column=0, padx=5, pady=2)
    window.l_wid = tk.Spinbox(window.line_dat, textvariable=window.line_width,
                            width='5', from_=1, to=100, increment=1)
    window.l_wid.grid(row=3, column=1, padx=5, pady=2)
    
    window.label = tk.Label(window.line_dat, text='Alpha:', bg=BG_BLUE,
                          font=('URW Bookman L', '10', 'bold'))
    window.label.grid(row=4, column=0)

    window.l_alpha_choice = tk.Spinbox(window.line_dat, textvariable=window.line_alpha,
                                 width='4', from_=0, to=1, increment=0.01)
    window.l_alpha_choice.grid(row=4, column=1, padx=2, pady=1)



    #************************************************************#
    #************************************************************#
    window.marker_dat = tk.LabelFrame(window.plot_options_frame, text='Marker',
                                    labelanchor='n', bg=BG_BLUE,
                                    font=('URW Bookman L', '11', 'bold'),
                                    height=235, width=165)
    window.marker_dat.grid(row=0, column=4, columnspan=2, padx=1)
    window.marker_dat.grid_propagate(0)

    window.label = tk.Label(window.marker_dat, text='Marker?:', bg=BG_BLUE,
                          font=('URW Bookman L', '10', 'bold'))
    window.label.grid(row=0, column=0, padx=5, pady=2)

    window.mark_exist_check = tk.Checkbutton(window.marker_dat,
                                           variable=window.mark_exist,
                                           bg=BG_BLUE,
                                           activebackground=BG_BLUE,
                                           command=window.other_plot_select)
    window.mark_exist_check.grid(row=0, column=1, padx=5, pady=2)

    window.label = tk.Label(window.marker_dat, text='Type:', bg=BG_BLUE,
                          font=('URW Bookman L', '10', 'bold'))
    window.label.grid(row=1, column=0)
    window.m_type = tk.OptionMenu(window.marker_dat, window.mark_type,
                                *window.marker_types)
    window.m_type['bg'] = BG_BLUE
    window.m_type['activebackground'] = BG_BLUE
    window.m_type['width'] = '3'
    window.m_type['height'] = '1'
    window.m_type['borderwidth'] = '1'
    window.m_type['pady'] = '1'
    window.m_type['padx'] = '2'
    window.m_type['relief'] = tk.RAISED
    window.m_type['anchor'] = tk.W
    window.m_type['highlightthickness'] = '0'
    window.m_type.grid(row=1, column=1, padx=5, pady=2)


    window.label = tk.Label(window.marker_dat, text='Edge Color:', bg=BG_BLUE,
                          font=('URW Bookman L', '10', 'bold'))
    window.label.grid(row=2, column=0)
    window.m_ecol = tk.Button(window.marker_dat, text='',
                            bg=window.mark_ec.get(),
                            activebackground=window.mark_ec.get(),
                            font=('URW Bookman L', '10', 'bold'),
                            command=window.me_col_h)
    window.m_ecol.grid(row=2, column=1, padx=5, pady=2, sticky=tk.W+tk.E)

    window.label = tk.Label(window.marker_dat, text='Edge Width:', bg=BG_BLUE,
                          font=('URW Bookman L', '10', 'bold'))
    window.label.grid(row=3, column=0)
    window.m_ewid = tk.Spinbox(window.marker_dat, textvariable=window.mark_ew,
                             width='5', from_=1, to=100, increment=1)
    window.m_ewid.grid(row=3, column=1, padx=5, pady=2)

    window.label = tk.Label(window.marker_dat, text='Face Color:', bg=BG_BLUE,
                          font=('URW Bookman L', '10', 'bold'))
    window.label.grid(row=4, column=0)
    window.m_fcol = tk.Button(window.marker_dat, text='',
                            bg=window.mark_fc.get(),
                            activebackground=window.mark_fc.get(),
                            font=('URW Bookman L', '10', 'bold'),
                            command=window.mf_col_h)
    window.m_fcol.grid(row=4, column=1, padx=5, pady=2, sticky=tk.W+tk.E)

    window.label = tk.Label(window.marker_dat, text='Size:', bg=BG_BLUE,
                          font=('URW Bookman L', '10', 'bold'))
    window.label.grid(row=5, column=0)
    window.m_sz = tk.Spinbox(window.marker_dat, textvariable=window.mark_sz,
                           width='5', from_=1, to=1000, increment=1)
    window.m_sz.grid(row=5, column=1, padx=5, pady=2)
    
    window.label = tk.Label(window.marker_dat, text='Mark Every:', bg=BG_BLUE,
                          font=('URW Bookman L', '10', 'bold'))
    window.label.grid(row=6, column=0)
    window.m_sz = tk.Spinbox(window.marker_dat, textvariable=window.mark_space,
                           width='5', from_=1, to=1000, increment=1)
    window.m_sz.grid(row=6, column=1, padx=5, pady=2)


    #************************************************************#
    #************************************************************#
    window.fill_dat = tk.LabelFrame(window.plot_options_frame, text='Fill',
                                  labelanchor='n', bg=BG_BLUE,
                                  font=('URW Bookman L', '11', 'bold'),
                                  height=235, width=165)
    window.fill_dat.grid(row=0, column=6, columnspan=2, padx=1)
    window.fill_dat.grid_propagate(0)

    window.label = tk.Label(window.fill_dat, text='Fill?:', bg=BG_BLUE,
                          font=('URW Bookman L', '10', 'bold'))
    window.label.grid(row=0, column=0)
    window.fill_exist_check = tk.Checkbutton(window.fill_dat,
                                           variable=window.fill_exist,
                                           bg=BG_BLUE,
                                           activebackground=BG_BLUE,
                                           command=window.other_plot_select)
    window.fill_exist_check.grid(row=0, column=1, padx=5, pady=2)

    window.label = tk.Label(window.fill_dat, text='Alpha:', bg=BG_BLUE,
                          font=('URW Bookman L', '10', 'bold'))
    window.label.grid(row=1, column=0)
    window.f_alpha = tk.Spinbox(window.fill_dat, textvariable=window.fill_alpha,
                              width='5', from_=0, to=1, increment=0.01)
    window.f_alpha.grid(row=1, column=1, padx=5, pady=2)

    window.label = tk.Label(window.fill_dat, text='Face Color:', bg=BG_BLUE,
                          font=('URW Bookman L', '10', 'bold'))
    window.label.grid(row=2, column=0)
    window.f_fcol = tk.Button(window.fill_dat, text='', bg=window.fill_fc.get(),
                            activebackground=window.fill_fc.get(),
                            font=('URW Bookman L', '10', 'bold'),
                            command=window.ff_col_h)
    window.f_fcol.grid(row=2, column=1, padx=5, pady=2, sticky=tk.W+tk.E)

    window.label = tk.Label(window.fill_dat, text='Edge Color:', bg=BG_BLUE,
                          font=('URW Bookman L', '10', 'bold'))
    window.label.grid(row=3, column=0)
    window.f_ecol = tk.Button(window.fill_dat, text='', bg=window.fill_ec.get(),
                            activebackground=window.fill_ec.get(),
                            font=('URW Bookman L', '10', 'bold'),
                            command=window.fe_col_h)
    window.f_ecol.grid(row=3, column=1, padx=5, pady=2, sticky=tk.W+tk.E)


    window.label = tk.Label(window.fill_dat, text='Edge Width:', bg=BG_BLUE,
                          font=('URW Bookman L', '10', 'bold'))
    window.label.grid(row=4, column=0)
    window.f_linew = tk.Spinbox(window.fill_dat, textvariable=window.fill_linew,
                              width='5', from_=0, to=100, increment=1)
    window.f_linew.grid(row=4, column=1, padx=5, pady=2)

    window.label = tk.Label(window.fill_dat, text='Edge Style:', bg=BG_BLUE,
                          font=('URW Bookman L', '10', 'bold'))
    window.label.grid(row=5, column=0)
    window.f_ls = tk.OptionMenu(window.fill_dat, window.fill_lines, *window.styles)
    window.f_ls['bg'] = BG_BLUE
    window.f_ls['activebackground'] = BG_BLUE
    window.f_ls['width'] = '3'
    window.f_ls['height'] = '1'
    window.f_ls['borderwidth'] = '1'
    window.f_ls['pady'] = '1'
    window.f_ls['padx'] = '2'
    window.f_ls['relief'] = tk.RAISED
    window.f_ls['anchor'] = tk.W
    window.f_ls['highlightthickness'] = '0'
    window.f_ls.grid(row=5, column=1, padx=5, pady=2)

    #************************************************************#
    #************************************************************#
    # Create a frame to hold the scatter information
    window.scatter_dat = tk.LabelFrame(window.plot_options_frame, text='Scatter Plot',
                                     labelanchor='n', bg=BG_BLUE,
                                     font=('URW Bookman L', '11', 'bold'),
                                     height=235, width=270)
    window.scatter_dat.grid(row=0, column=8, columnspan=2, padx=1)
    window.scatter_dat.grid_propagate(0)
    window.label = tk.Label(window.scatter_dat, text='Scatter?:', bg=BG_BLUE,
                          font=('URW Bookman L', '10', 'bold'))
    window.label.grid(row=0, column=0)
    window.scat_exist_check = tk.Checkbutton(window.scatter_dat,
                                           variable=window.scat_exist,
                                           bg=BG_BLUE,
                                           activebackground=BG_BLUE,
                                           command=window.scatter_select)
    window.scat_exist_check.grid(row=0, column=1, padx=5, pady=2)

    window.label = tk.Label(window.scatter_dat, text='Marker:', bg=BG_BLUE,
                          font=('URW Bookman L', '10', 'bold'))
    window.label.grid(row=1, column=0)

    window.scatter_type = tk.OptionMenu(window.scatter_dat, window.scat_type,
                                      *window.marker_types)
    window.scatter_type['bg'] = BG_BLUE
    window.scatter_type['activebackground'] = BG_BLUE
    window.scatter_type['width'] = '3'
    window.scatter_type['height'] = '1'
    window.scatter_type['borderwidth'] = '1'
    window.scatter_type['pady'] = '1'
    window.scatter_type['padx'] = '2'
    window.scatter_type['relief'] = tk.RAISED
    window.scatter_type['anchor'] = tk.W
    window.scatter_type['highlightthickness'] = '0'
    window.scatter_type.grid(row=1, column=1, padx=5, pady=2)

    window.scatter_edge = tk.OptionMenu(window.scatter_dat, window.scat_edge,
                                      *window.scat_faces)
    window.scatter_edge['bg'] = BG_BLUE
    window.scatter_edge['activebackground'] = BG_BLUE
    window.scatter_edge['width'] = '5'
    window.scatter_edge['height'] = '1'
    window.scatter_edge['borderwidth'] = '1'
    window.scatter_edge['pady'] = '1'
    window.scatter_edge['padx'] = '2'
    window.scatter_edge['relief'] = tk.RAISED
    window.scatter_edge['anchor'] = tk.W
    window.scatter_edge['highlightthickness'] = '0'
    window.scatter_edge.grid(row=1, column=2, padx=5, pady=2)

    window.label = tk.Label(window.scatter_dat, text='Alpha:', bg=BG_BLUE,
                          font=('URW Bookman L', '10', 'bold'))
    window.label.grid(row=2, column=0)

    window.scat_alpha_choice = tk.Spinbox(window.scatter_dat, textvariable=window.scat_alpha,
                                 width='4', from_=0, to=1, increment=0.01)
    window.scat_alpha_choice.grid(row=2, column=1, padx=2, pady=1)

    window.label = tk.Label(window.scatter_dat, text='Color:', bg=BG_BLUE,
                          font=('URW Bookman L', '10', 'bold'))
    window.label.grid(row=3, column=0)

    window.scatter_color = tk.OptionMenu(window.scatter_dat, window.scat_color,
                                       *window.scat_color_list)
    window.scatter_color['bg'] = BG_BLUE
    window.scatter_color['activebackground'] = BG_BLUE
    window.scatter_color['width'] = '17'
    window.scatter_color['height'] = '1'
    window.scatter_color['borderwidth'] = '1'
    window.scatter_color['pady'] = '1'
    window.scatter_color['padx'] = '2'
    window.scatter_color['relief'] = tk.RAISED
    window.scatter_color['anchor'] = tk.W
    window.scatter_color['highlightthickness'] = '0'
    window.scatter_color.grid(row=3, column=1, columnspan=2, padx=5, pady=2)

    window.label = tk.Label(window.scatter_dat, text='Size:', bg=BG_BLUE,
                          font=('URW Bookman L', '10', 'bold'))
    window.label.grid(row=4, column=0)

    window.scatter_size = tk.OptionMenu(window.scatter_dat, window.scat_size,
                                      *window.scat_size_list)
    window.scatter_size['bg'] = BG_BLUE
    window.scatter_size['activebackground'] = BG_BLUE
    window.scatter_size['width'] = '17'
    window.scatter_size['height'] = '1'
    window.scatter_size['borderwidth'] = '1'
    window.scatter_size['pady'] = '1'
    window.scatter_size['padx'] = '2'
    window.scatter_size['relief'] = tk.RAISED
    window.scatter_size['anchor'] = tk.W
    window.scatter_size['highlightthickness'] = '0'
    window.scatter_size.grid(row=4, column=1, columnspan=2, padx=5, pady=2)

    window.label = tk.Label(window.scatter_dat, text='Color Bar?:', bg=BG_BLUE,
                          font=('URW Bookman L', '10', 'bold'))
    window.label.grid(row=5, column=0)
    window.cb_exist_check = tk.Checkbutton(window.scatter_dat,
                                         variable=window.cb_exist,
                                         bg=BG_BLUE,
                                         activebackground=BG_BLUE)
    window.cb_exist_check.grid(row=5, column=1, padx=5, pady=2)

    window.label = tk.Label(window.scatter_dat, text='Color Map:', bg=BG_BLUE,
                          font=('URW Bookman L', '10', 'bold'))
    window.label.grid(row=6, column=0)

    window.color_map = tk.OptionMenu(window.scatter_dat, window.cmap_pick,
                                      *window.cmap_list)
    window.color_map['bg'] = BG_BLUE
    window.color_map['activebackground'] = BG_BLUE
    window.color_map['width'] = '17'
    window.color_map['height'] = '1'
    window.color_map['borderwidth'] = '1'
    window.color_map['pady'] = '1'
    window.color_map['padx'] = '2'
    window.color_map['relief'] = tk.RAISED
    window.color_map['anchor'] = tk.W
    window.color_map['highlightthickness'] = '0'
    window.color_map.grid(row=6, column=1, columnspan=2, padx=5, pady=2)

    #************************************************************#
    #************************************************************#
    # Create a frame to hold the axis details information
    window.axisFrame = tk.LabelFrame(window, text='Axis Details',
                                   labelanchor='nw', height='100',
                                   width='400', bg=BG_BLUE,
                                   font=('URW Bookman L', '12', 'bold'))
    window.axisFrame.grid(row=2, column=0, columnspan=3, rowspan=2,
                        padx=10, pady=4)


    #************************************************************#
    #************************************************************#
    # Create the frame to specify the grid size
    window.gridFrame = tk.LabelFrame(window.axisFrame, text='Grid Size',
                                   labelanchor='n',
                                   font=('URW Bookman L', '12', 'bold'),
                                   bg=BG_BLUE)
    window.gridFrame.grid(row=0, column=0, columnspan=2, padx=5, pady=5,
                        sticky=tk.W+tk.E)
    window.label = tk.Label(window.gridFrame, text='Rows:',
                          font=('URW Bookman L', '10'), bg=BG_BLUE)
    window.label.grid(row=0, column=0, padx=2, pady=1)
    window.gridrEntry = tk.Spinbox(window.gridFrame, textvariable=window.gridrow,
                                 width='4', from_=1, to=100, increment=1)
    window.gridrEntry.grid(row=0, column=1, padx=2, pady=1)
    window.label = tk.Label(window.gridFrame, text='Columns:',
                          font=('URW Bookman L', '10'), bg=BG_BLUE)
    window.label.grid(row=0, column=2, padx=2, pady=1)
    window.gridcEntry = tk.Spinbox(window.gridFrame, textvariable=window.gridcol,
                                 width='4', from_=1, to=100, increment=1)
    window.gridcEntry.grid(row=0, column=3, padx=2, pady=1)
    window.label = tk.Label(window.gridFrame, text='Share x:',
                          font=('URW Bookman L', '10'), bg=BG_BLUE)
    window.label.grid(row=1, column=0, padx=2, pady=1)
    window.sharex_check = tk.Checkbutton(window.gridFrame,
                                       variable=window.sharex, bg=BG_BLUE,
                                       activebackground=BG_BLUE)
    window.sharex_check.grid(row=1, column=1, padx=5, pady=2)
    window.label = tk.Label(window.gridFrame, text='Share y:',
                          font=('Verdana', '10'), bg=BG_BLUE)
    window.label.grid(row=1, column=2, padx=2, pady=1)
    window.sharey_check = tk.Checkbutton(window.gridFrame,
                                       variable=window.sharey,
                                       bg=BG_BLUE,
                                       activebackground=BG_BLUE)
    window.sharey_check.grid(row=1, column=3, padx=5, pady=2)

    #************************************************************#
    #************************************************************#
    # Create button for adding a new axis to the plot
    window.createFrame = tk.LabelFrame(window.axisFrame,
                                     text='Create or Delete Axes',
                                     labelanchor='n',
                                     font=('URW Bookman L', '12', 'bold'),
                                     bg=BG_BLUE)
    window.createFrame.grid(row=0, column=2, columnspan=2, padx=5, pady=5,
                          sticky=tk.W+tk.E)

    window.addnewAxis = tk.Button(window.createFrame, text='Add Axis',
                                font=('URW Bookman L', '10', 'bold'),
                                bg=BG_GREEN, activebackground=BG_GREEN,
                                command=window.add_new_axis)
    window.addnewAxis.grid(row=0, column=0, sticky=tk.W+tk.E, padx=3, pady=5)

    window.axis_select = tk.OptionMenu(window.createFrame, window.current_axis,
                                     *window.axis_list,
                                     command=window.axis_changed)
    window.axis_select['bg'] = BG_BLUE
    window.axis_select['activebackground'] = BG_BLUE
    window.axis_select['width'] = '6'
    window.axis_select['height'] = '2'
    window.axis_select['borderwidth'] = '1'
    window.axis_select['pady'] = '1'
    window.axis_select['padx'] = '1'
    window.axis_select['relief'] = tk.RAISED
    window.axis_select['anchor'] = tk.W
    window.axis_select['highlightthickness'] = '0'
    window.axis_select.grid(row=0, column=1, sticky=tk.W+tk.E)

    window.delAxis = tk.Button(window.createFrame, text='Delete Axis',
                             font=('URW Bookman L', '10', 'bold'), bg=BG_RED,
                             activebackground=BG_RED,
                             command=window.del_curr_axis)
    window.delAxis.grid(row=0, column=2, sticky=tk.W+tk.E, padx=3, pady=6)

    #************************************************************#
    #************************************************************#
    # Create Frame for data selection for the axis
    window.selDataFrame = tk.LabelFrame(window.axisFrame,
                                      text='Data Selection',
                                      labelanchor='n',
                                      font=('URW Bookman L', '12', 'bold'),
                                      bg=BG_BLUE, width=500, height=100)
    window.selDataFrame.grid(row=0, column=4, columnspan=2, padx=5, pady=5,
                           sticky=tk.W+tk.E)

    window.label = tk.Label(window.selDataFrame, text='All Data', bg=BG_BLUE,
                          font=('URW Bookman L', '10', 'bold'))
    window.label.grid(row=0, column=0, sticky=tk.W+tk.E)

    window.label = tk.Label(window.selDataFrame, text='Selected Data',
                          bg=BG_BLUE, font=('URW Bookman L', '10', 'bold'))
    window.label.grid(row=0, column=2, sticky=tk.W+tk.E)

    window.alldat = tk.OptionMenu(window.selDataFrame, window.alldat_selected,
                                *window.data_list)
    window.alldat['bg'] = BG_BLUE
    window.alldat['activebackground'] = BG_BLUE
    window.alldat['width'] = '10'
    window.alldat['height'] = '1'
    window.alldat['borderwidth'] = '1'
    window.alldat['pady'] = '1'
    window.alldat['padx'] = '2'
    window.alldat['relief'] = tk.RAISED
    window.alldat['anchor'] = tk.W
    window.alldat['highlightthickness'] = '0'
    window.alldat.grid(row=1, column=0, padx=2)

    window.add_dat = tk.Button(window.selDataFrame, text='>', bg=BG_GREEN,
                             activebackground=BG_GREEN, font=('URW Bookman L', '8'),
                             command=window.add_plot_to_axis)
    window.add_dat.grid(row=1, column=1)

    window.rem_dat = tk.Button(window.selDataFrame, text='<', bg=BG_RED,
                             activebackground=BG_RED, font=('URW Bookman L', '8'),
                             command=window.remove_plot_from_axis)
    window.rem_dat.grid(row=1, column=3)

    window.seldat = tk.OptionMenu(window.selDataFrame, window.seldat_selected,
                                *window.selected_axis_data)
    window.seldat['bg'] = BG_BLUE
    window.seldat['activebackground'] = BG_BLUE
    window.seldat['width'] = '10'
    window.seldat['height'] = '1'
    window.seldat['borderwidth'] = '1'
    window.seldat['pady'] = '1'
    window.seldat['padx'] = '2'
    window.seldat['relief'] = tk.RAISED
    window.seldat['anchor'] = tk.W
    window.seldat['highlightthickness'] = '0'
    window.seldat.grid(row=1, column=2, padx=2)


    #************************************************************#
    #************************************************************#
    # Create Frame for data position for the axis
    window.axPosFrame = tk.LabelFrame(window.axisFrame, text='Axis Position',
                                    labelanchor='n',
                                    font=('URW Bookman L', '12', 'bold'), bg=BG_BLUE,
                                    width=500, height=100)
    window.axPosFrame.grid(row=0, column=6, columnspan=2, padx=5, pady=5,
                         sticky=tk.W+tk.E)

    window.label = tk.Label(window.axPosFrame, text='Row:',
                          font=('URW Bookman L', '10'), bg=BG_BLUE)
    window.label.grid(row=0, column=0)
    window.axrow_sb = tk.Spinbox(window.axPosFrame, textvariable=window.axrow,
                               width='4', from_=0, to=100, increment=1)
    window.axrow_sb.grid(row=0, column=1, padx=2, pady=1)
    window.label = tk.Label(window.axPosFrame, text='Row Span:',
                          font=('URW Bookman L', '10'), bg=BG_BLUE)
    window.label.grid(row=0, column=2)
    window.axrowspan_sb = tk.Spinbox(window.axPosFrame,
                                   textvariable=window.axrowspan, width='4',
                                   from_=1, to=100, increment=1)
    window.axrowspan_sb.grid(row=0, column=3, padx=2, pady=1)

    window.label = tk.Label(window.axPosFrame, text='Column:',
                          font=('URW Bookman L', '10'), bg=BG_BLUE)
    window.label.grid(row=1, column=0)
    window.axcol_sb = tk.Spinbox(window.axPosFrame, textvariable=window.axcol,
                               width='4', from_=0, to=100, increment=1)
    window.axcol_sb.grid(row=1, column=1, padx=2, pady=1)
    window.label = tk.Label(window.axPosFrame, text='Column Span:',
                          font=('URW Bookman L', '10'), bg=BG_BLUE)
    window.label.grid(row=1, column=2)
    window.axcolspan_sb = tk.Spinbox(window.axPosFrame,
                                   textvariable=window.axcolspan, width='4',
                                   from_=1, to=100, increment=1)
    window.axcolspan_sb.grid(row=1, column=3, padx=2, pady=1)

    #************************************************************#
    #************************************************************#
    # create the frame that will hold the information for the axis labels
    window.axlabFrame = tk.LabelFrame(window.axisFrame, text='Axis Labels',
                                    labelanchor='n', height='100',
                                    width='150', bg=BG_BLUE,
                                    font=('URW Bookman L', '12', 'bold'))
    window.axlabFrame.grid(row=1, column=0, columnspan=4, rowspan=3, padx=1,
                         pady=5, sticky=tk.W+tk.E)

    # Create a text field for the x-axis title
    window.label = tk.Label(window.axlabFrame, text='X-Axis: Label:',
                          font=('URW Bookman L', '10'), bg=BG_BLUE)
    window.label.grid(row=0, column=0, padx=1, pady=1)
    window.xlabEntry = tk.Entry(window.axlabFrame, textvariable=window.xlab,
                              width='55')
    window.xlabEntry.grid(row=0, column=1, columnspan=7, padx=2, pady=1)
    # Create a text field for entering the lower x_limit
    window.label = tk.Label(window.axlabFrame, text='Lower Limit:',
                          font=('URW Bookman L', '10'), bg=BG_BLUE)
    window.label.grid(row=1, column=0, padx=1, pady=1)
    window.xlimloEntry = tk.Entry(window.axlabFrame, textvariable=window.xlimlow,
                                width='5')
    window.xlimloEntry.grid(row=1, column=1, padx=1, pady=1)
    # Create a text field for entering the upper x_limit
    window.label = tk.Label(window.axlabFrame, text='Upper Limit:',
                          font=('URW Bookman L', '10'), bg=BG_BLUE)
    window.label.grid(row=1, column=2, padx=1, pady=1)
    window.xlimhiEntry = tk.Entry(window.axlabFrame, textvariable=window.xlimhi,
                                width='5')
    window.xlimhiEntry.grid(row=1, column=3, padx=1, pady=1)
    # Create checkbox for axis ticks
    window.label = tk.Label(window.axlabFrame, text='Show ticks:',
                          font=('URW Bookman L', '10'), bg=BG_BLUE)
    window.label.grid(row=1, column=4, padx=1, pady=1)
    window.xtickcheck = tk.Checkbutton(window.axlabFrame, variable=window.xticks,
                                     bg=BG_BLUE, activebackground=BG_BLUE)
    window.xtickcheck.grid(row=1, column=5, padx=1, pady=1)

    # Create checkbox for log scale
    window.label = tk.Label(window.axlabFrame, text='Log Scale:',
                          font=('URW Bookman L', '10'), bg=BG_BLUE)
    window.label.grid(row=1, column=6, padx=1, pady=1)
    window.xlogscale = tk.Checkbutton(window.axlabFrame, variable=window.xlog,
                                    bg=BG_BLUE, activebackground=BG_BLUE)
    window.xlogscale.grid(row=1, column=7, padx=1, pady=1)

    # Create Textbox for the y-Axis label
    window.label = tk.Label(window.axlabFrame, text='Y-Axis: Label:',
                          font=('URW Bookman L', '10'), bg=BG_BLUE)
    window.label.grid(row=2, column=0, padx=1, pady=1)
    window.ylabEntry = tk.Entry(window.axlabFrame, textvariable=window.ylab,
                              width='55')
    window.ylabEntry.grid(row=2, column=1, columnspan=7, padx=1, pady=1)
    # Create entry for lower y-Limit
    window.label = tk.Label(window.axlabFrame, text='Lower Limit:',
                          font=('URW Bookman L', '10'), bg=BG_BLUE)
    window.label.grid(row=3, column=0, padx=1, pady=1)
    window.ylimloEntry = tk.Entry(window.axlabFrame, textvariable=window.ylimlow,
                                width='5')
    window.ylimloEntry.grid(row=3, column=1, padx=1, pady=1)
    # Create entry for upper y_limit
    window.label = tk.Label(window.axlabFrame, text='Upper Limit:',
                          font=('URW Bookman L', '10'), bg=BG_BLUE)
    window.label.grid(row=3, column=2, padx=0, pady=0)
    window.ylimhiEntry = tk.Entry(window.axlabFrame, textvariable=window.ylimhi,
                                width='5')
    window.ylimhiEntry.grid(row=3, column=3, padx=0, pady=0)
    # Create checkbox for axis ticks
    window.label = tk.Label(window.axlabFrame, text='Show ticks:',
                          font=('URW Bookman L', '10'), bg=BG_BLUE)
    window.label.grid(row=3, column=4, padx=0, pady=0)
    window.xtickcheck = tk.Checkbutton(window.axlabFrame, variable=window.yticks,
                                     bg=BG_BLUE, activebackground=BG_BLUE)
    window.xtickcheck.grid(row=3, column=5, padx=0, pady=0)
    # Create checkbox for log scale
    window.label = tk.Label(window.axlabFrame, text='Log Scale:',
                          font=('URW Bookman L', '10'), bg=BG_BLUE)
    window.label.grid(row=3, column=6, padx=1, pady=1)
    window.ylogscale = tk.Checkbutton(window.axlabFrame, variable=window.ylog,
                                    bg=BG_BLUE, activebackground=BG_BLUE)
    window.ylogscale.grid(row=3, column=7, padx=1, pady=1)

    # Create a Spinbox for the text size
    window.label = tk.Label(window.axlabFrame, text='Font Size:',
                          font=('URW Bookman L', '10'), bg=BG_BLUE)
    window.label.grid(row=4, column=0, padx=1, pady=1)
    window.xlabSize = tk.Spinbox(window.axlabFrame, textvariable=window.axsize,
                               width='4', from_=1, to=30, increment=0.5)
    window.xlabSize.grid(row=4, column=1)
    # Create a checkbutton for bold font
    window.label = tk.Label(window.axlabFrame, text='Bold:',
                          font=('URW Bookman L', '10'), bg=BG_BLUE)
    window.label.grid(row=4, column=2, padx=1, pady=1)
    window.xboldselect = tk.Checkbutton(window.axlabFrame,
                                      variable=window.axbold, bg=BG_BLUE,
                                      activebackground=BG_BLUE)
    window.xboldselect.grid(row=4, column=3, padx=1, pady=1)
    # Create a checkbutton for italic font
    window.label = tk.Label(window.axlabFrame, text='Italic:',
                          font=('URW Bookman L', '10'), bg=BG_BLUE)
    window.label.grid(row=4, column=4, padx=1, pady=1)
    window.xboldselect = tk.Checkbutton(window.axlabFrame,
                                      variable=window.axitalic, bg=BG_BLUE,
                                      activebackground=BG_BLUE)
    window.xboldselect.grid(row=4, column=5, padx=1, pady=1)

    #************************************************************#
    #************************************************************#
    # Create frame for the plot title information
    window.titFrame = tk.LabelFrame(window.axisFrame, text='Plot Title',
                                  labelanchor='n', height='100',
                                  width='200', bg=BG_BLUE,
                                  font=('URW Bookman L', '12', 'bold'))
    window.titFrame.grid(row=1, column=4, columnspan=4, padx=5, pady=0,
                       sticky=tk.W+tk.E)

    # Create entry box for title
    window.label = tk.Label(window.titFrame, text='Label:',
                          font=('URW Bookman L', '10'), bg=BG_BLUE)
    window.label.grid(row=0, column=0, padx=2, pady=1)
    window.titleEntry = tk.Entry(window.titFrame, textvariable=window.title,
                               width='60')
    window.titleEntry.grid(row=0, column=1, padx=2, pady=1, columnspan=7)
    # Create spinbox for title size
    window.label = tk.Label(window.titFrame, text='Font Size:',
                          font=('URW Bookman L', '10'), bg=BG_BLUE)
    window.label.grid(row=1, column=0, padx=2, pady=1)
    window.titleSize = tk.Spinbox(window.titFrame, textvariable=window.tsize,
                                width=4, from_=1, to=30, increment=0.5)
    window.titleSize.grid(row=1, column=1)
    # Create select box for bold font
    window.label = tk.Label(window.titFrame, text='Bold:',
                          font=('URW Bookman L', '10'), bg=BG_BLUE)
    window.label.grid(row=1, column=2, padx=2, pady=1)
    window.yboldselect = tk.Checkbutton(window.titFrame, variable=window.tbold,
                                      bg=BG_BLUE, activebackground=BG_BLUE)
    window.yboldselect.grid(row=1, column=3, padx=2, pady=1)
    # Create select box for italic font
    window.label = tk.Label(window.titFrame, text='Italic:',
                          font=('URW Bookman L', '10'), bg=BG_BLUE)
    window.label.grid(row=1, column=4, padx=2, pady=1)
    window.yboldselect = tk.Checkbutton(window.titFrame, variable=window.titalic,
                                      bg=BG_BLUE, activebackground=BG_BLUE)
    window.yboldselect.grid(row=1, column=5, padx=2, pady=1)

    #************************************************************#
    #************************************************************#
    # Create frame for the legend position information
    window.legFrame = tk.LabelFrame(window.axisFrame, text='Legend',
                                  labelanchor='n', height='100',
                                  width='200', bg=BG_BLUE,
                                  font=('URW Bookman L', '12', 'bold'))
    window.legFrame.grid(row=2, column=4, rowspan=2, columnspan=2, padx=5, pady=5,
                       sticky=tk.W+tk.E)

    window.label = tk.Label(window.legFrame, text='Position:',
                          font=('URW Bookman L', '10'), bg=BG_BLUE)
    window.label.grid(row=0, column=0, padx=2, pady=1, sticky=tk.W+tk.E)
    window.leg_pos = tk.OptionMenu(window.legFrame, window.legend,
                                 *window.legend_pos_list)
    window.leg_pos['bg'] = BG_BLUE
    window.leg_pos['activebackground'] = BG_BLUE
    window.leg_pos['width'] = '10'
    window.leg_pos['height'] = '1'
    window.leg_pos['borderwidth'] = '1'
    window.leg_pos['pady'] = '1'
    window.leg_pos['padx'] = '2'
    window.leg_pos['relief'] = tk.RAISED
    window.leg_pos['anchor'] = tk.W
    window.leg_pos['highlightthickness'] = '0'
    window.leg_pos.grid(row=1, column=0, padx=20, pady=5, sticky=tk.W+tk.E)

    window.label = tk.Label(window.legFrame, text='Font Size:',
                          font=('URW Bookman L', '10'), bg=BG_BLUE)
    window.label.grid(row=0, column=1, padx=2, pady=1, sticky=tk.W+tk.E)
    window.legSize = tk.Spinbox(window.legFrame, textvariable=window.lgSize,
                              width=4, from_=1, to=30, increment=0.5)
    window.legSize.grid(row=1, column=1)


    #************************************************************#
    #************************************************************#
    # Create a button for showing the plot
    window.show_plot = tk.Button(window.axisFrame, text='---SHOW PLOT---',
                               bg=BG_GREEN, activebackground=BG_GREEN,
                               command=window.gen_plot)
    window.show_plot.grid(row=2, column=6, columnspan=2,
                        sticky=tk.W+tk.E+tk.N+tk.S, padx=30, pady=1)

    # Create a button for saving the plot
    window.save_plot_btn = tk.Button(window.axisFrame, text='---SAVE PLOT---',
                                   bg='#4E51B5', activebackground='#4E51B5',
                                   command=window.save_plot)
    window.save_plot_btn.grid(row=3, column=6, columnspan=2,
                            sticky=tk.W+tk.E+tk.N+tk.S, padx=30, pady=1)
    
def __populate_variables(window):
    window.data_list = list(window.data_dict.keys())
    window.add_first_axis()
    window.axis_list = list(window.axis_dict.keys())
    window.selected_axis_value = 'axis1'

    set_plot_data(window, window.data_list[0])
    set_axis_data(window, 'axis1')
