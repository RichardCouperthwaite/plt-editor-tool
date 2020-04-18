# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 09:37:32 2020

@author: richardcouperthwaite
"""

def save_plot_data(window, index):
    window.data_dict[index]['label'] = window.dat_lab.get()
    window.data_dict[index]['fill-label'] = window.dat_lab2.get()

    window.data_dict[index]['ebar']['exist'] = window.ebar_exist.get()
    window.data_dict[index]['ebar']['color'] = window.ebar_color.get()
    window.data_dict[index]['ebar']['linew'] = window.ebar_linew.get()
    window.data_dict[index]['ebar']['capsize'] = window.ebar_caps.get()
    window.data_dict[index]['ebar']['capthick'] = window.ebar_capt.get()

    window.data_dict[index]['line']['exist'] = window.line_exist.get()
    window.data_dict[index]['line']['color'] = window.line_color.get()
    window.data_dict[index]['line']['style'] = window.line_style.get()
    window.data_dict[index]['line']['width'] = window.line_width.get()
    window.data_dict[index]['line']['alpha'] = window.line_alpha.get()

    window.data_dict[index]['marker']['exist'] = window.mark_exist.get()
    window.data_dict[index]['marker']['type'] = window.mark_type.get()
    window.data_dict[index]['marker']['edge_col'] = window.mark_ec.get()
    window.data_dict[index]['marker']['edge_wid'] = window.mark_ew .get()
    window.data_dict[index]['marker']['face_col'] = window.mark_fc.get()
    window.data_dict[index]['marker']['size'] = window.mark_sz.get()
    window.data_dict[index]['marker']['markevery'] = window.mark_space.get()

    window.data_dict[index]['fill']['exist'] = window.fill_exist.get()
    window.data_dict[index]['fill']['alpha'] = window.fill_alpha.get()
    window.data_dict[index]['fill']['edge_col'] = window.fill_ec.get()
    window.data_dict[index]['fill']['face_col'] = window.fill_fc.get()
    window.data_dict[index]['fill']['line_wid'] = window.fill_linew.get()
    window.data_dict[index]['fill']['line_sty'] = window.fill_lines.get()
    # window.axis_dict[index]['plots'][0] = window.seldat_selected.get()
    # window.axis_dict[index]['plots'] = window.selected_axis_data

    window.data_dict[index]['scatter']['exist'] = window.scat_exist.get()
    window.data_dict[index]['scatter']['type'] = window.scat_type.get()
    window.data_dict[index]['scatter']['edge'] = window.scat_edge.get()
    window.data_dict[index]['scatter']['current_size'] = window.scat_size.get()
    window.data_dict[index]['scatter']['current_color'] = window.scat_color.get()
    window.data_dict[index]['scatter']['cmap'] = window.cmap_pick.get()
    window.data_dict[index]['scatter']['alpha'] = float(window.scat_alpha.get())
    window.data_dict[index]['colorbar'] = window.cb_exist.get()

def set_plot_data(window, index):
    window.selected_data_value = index
    window.dat_lab.set(window.data_dict[index]['label'])
    window.dat_lab2.set(window.data_dict[index]['fill-label'])
    window.current_data.set(index)
    window.selected_data_value = window.current_data.get()

    window.ebar_exist.set(window.data_dict[index]['ebar']['exist'])
    window.ebar_color.set(window.data_dict[index]['ebar']['color'])
    try:
        window.eb_col['bg'] = window.data_dict[index]['ebar']['color']
        window.eb_col['activebackground'] = window.data_dict[index]['ebar']['color']
        window.eb_col['fg'] = window.data_dict[index]['ebar']['color']
    except AttributeError:
        pass
    window.ebar_linew.set(window.data_dict[index]['ebar']['linew'])
    window.ebar_caps.set(window.data_dict[index]['ebar']['capsize'])
    window.ebar_capt.set(window.data_dict[index]['ebar']['capthick'])

    window.line_exist.set(window.data_dict[index]['line']['exist'])
    window.line_color.set(window.data_dict[index]['line']['color'])
    try:
        window.l_col['bg'] = window.data_dict[index]['line']['color']
        window.l_col['activebackground'] = window.data_dict[index]['line']['color']
        window.l_col['fg'] = window.data_dict[index]['line']['color']
    except AttributeError:
        pass
    window.line_style.set(window.data_dict[index]['line']['style'])
    window.line_width.set(window.data_dict[index]['line']['width'])
    window.line_alpha.set(window.data_dict[index]['line']['alpha'])

    window.mark_exist.set(window.data_dict[index]['marker']['exist'])
    window.mark_type.set(window.data_dict[index]['marker']['type'])
    window.mark_ec.set(window.data_dict[index]['marker']['edge_col'])
    try:
        window.m_ecol['bg'] = window.data_dict[index]['marker']['edge_col']
        window.m_ecol['activebackground'] = window.data_dict[index]['marker']['edge_col']
        window.m_ecol['fg'] = window.data_dict[index]['marker']['edge_col']
    except AttributeError:
        pass
    window.mark_ew .set(window.data_dict[index]['marker']['edge_wid'])
    window.mark_fc.set(window.data_dict[index]['marker']['face_col'])
    try:
        window.m_fcol['bg'] = window.data_dict[index]['marker']['face_col']
        window.m_fcol['activebackground'] = window.data_dict[index]['marker']['face_col']
        window.m_fcol['fg'] = window.data_dict[index]['marker']['face_col']
    except AttributeError:
        pass
    window.mark_sz.set(window.data_dict[index]['marker']['size'])
    window.mark_space.set(window.data_dict[index]['marker']['markevery'])

    window.fill_exist.set(window.data_dict[index]['fill']['exist'])
    window.fill_alpha.set(window.data_dict[index]['fill']['alpha'])
    window.fill_ec.set(window.data_dict[index]['fill']['edge_col'])
    try:
        window.f_ecol['bg'] = window.data_dict[index]['fill']['edge_col']
        window.f_ecol['activebackground'] = window.data_dict[index]['fill']['edge_col']
        window.f_ecol['fg'] = window.data_dict[index]['fill']['edge_col']
    except AttributeError:
        pass
    window.fill_fc.set(window.data_dict[index]['fill']['face_col'])
    try:
        window.f_fcol['bg'] = window.data_dict[index]['fill']['face_col']
        window.f_fcol['activebackground'] = window.data_dict[index]['fill']['face_col']
        window.f_fcol['fg'] = window.data_dict[index]['fill']['face_col']
    except AttributeError:
        pass
    window.fill_linew.set(window.data_dict[index]['fill']['line_wid'])
    window.fill_lines.set(window.data_dict[index]['fill']['line_sty'])

    window.scat_exist.set(window.data_dict[index]['scatter']['exist'])
    window.scat_type.set(window.data_dict[index]['scatter']['type'])
    window.cmap_pick.set(window.data_dict[index]['scatter']['cmap'])
    window.scat_alpha.set(window.data_dict[index]['scatter']['alpha'])
    window.scat_edge.set(window.data_dict[index]['scatter']['edge'])
    window.cb_exist.set(window.data_dict[index]['colorbar'])
    try:
        menu = window.scatter_size["menu"]
        menu.delete(0, "end")
        for string in list(window.data_dict[index]['scatter']['size_vector_names']):
            menu.add_command(label=string,
                             command=lambda value=string: window.scat_size.set(value))
        menu = window.scatter_color["menu"]
        menu.delete(0, "end")
        for string in list(window.data_dict[index]['scatter']['color_vector_names']):
            menu.add_command(label=string,
                             command=lambda value=string: window.scat_color.set(value))
    except AttributeError:
        pass
    window.scat_size.set(window.data_dict[index]['scatter']['current_size'])
    window.scat_color.set(window.data_dict[index]['scatter']['current_color'])
    
def save_axis_data(window, index):
    window.axis_dict[index]['plots'][0] = window.seldat_selected.get()
    window.axis_dict[index]['plots'] = window.selected_axis_data

    window.axis_dict[index]['position'][0] = window.axrow.get()
    window.axis_dict[index]['position'][1] = window.axcol.get()
    window.axis_dict[index]['position'][2] = window.axrowspan.get()
    window.axis_dict[index]['position'][3] = window.axcolspan.get()

    window.axis_dict[index]['x_label'] = window.xlab.get()
    window.axis_dict[index]['y_label'] = window.ylab.get()

    window.axis_dict[index]['axis_text']['size'] = window.axsize.get()

    window.axis_dict[index]['x_lim'][0] = window.xlimlow.get()
    window.axis_dict[index]['x_lim'][1] = window.xlimhi.get()
    window.axis_dict[index]['y_lim'][0] = window.ylimlow.get()
    window.axis_dict[index]['y_lim'][1] = window.ylimhi.get()
    window.axis_dict[index]['xticks'] = window.xticks.get()
    window.axis_dict[index]['yticks'] = window.yticks.get()
    window.axis_dict[index]['xscale'] = window.xlog.get()
    window.axis_dict[index]['yscale'] = window.ylog.get()

    window.axis_dict[index]['axis_text']['Bold'] = window.axbold.get()
    window.axis_dict[index]['axis_text']['Italic'] = window.axitalic.get()

    window.axis_dict[index]['title'] = window.title.get()
    window.axis_dict[index]['title_text']['size'] = window.tsize.get()
    window.axis_dict[index]['title_text']['Bold'] = window.tbold.get()
    window.axis_dict[index]['title_text']['Italic'] = window.titalic.get()

    window.axis_dict[index]['legend'] = window.legend.get()
    window.axis_dict[index]['legendFontSize'] = window.lgSize.get()
    
def set_axis_data(window, index):
    window.selected_axis_value = index

    window.seldat_selected.set(window.axis_dict[index]['plots'][0])
    window.selected_axis_data = window.axis_dict[index]['plots']
    try:
        menu = window.seldat["menu"]
        menu.delete(0, "end")
        for string in window.selected_axis_data:
            menu.add_command(label=string)
    except AttributeError:
        window.alldat_selected.set(window.data_list[0])
        window.seldat_selected.set(window.axis_dict[index]['plots'][0])
        window.selected_axis_data = window.axis_dict[index]['plots']

    window.current_axis.set(index)

    window.axrow.set(window.axis_dict[index]['position'][0])
    window.axcol.set(window.axis_dict[index]['position'][1])
    window.axrowspan.set(window.axis_dict[index]['position'][2])
    window.axcolspan.set(window.axis_dict[index]['position'][3])

    window.xlab.set(window.axis_dict[index]['x_label'])
    window.ylab.set(window.axis_dict[index]['y_label'])

    window.axsize.set(window.axis_dict[index]['axis_text']['size'])

    window.xlimlow.set(window.axis_dict[index]['x_lim'][0])
    window.xlimhi.set(window.axis_dict[index]['x_lim'][1])
    window.ylimlow.set(window.axis_dict[index]['y_lim'][0])
    window.ylimhi.set(window.axis_dict[index]['y_lim'][1])
    window.xticks.set(window.axis_dict[index]['xticks'])
    window.yticks.set(window.axis_dict[index]['yticks'])
    window.xlog.set(window.axis_dict[index]['xscale'])
    window.ylog.set(window.axis_dict[index]['yscale'])

    window.axbold.set(window.axis_dict[index]['axis_text']['Bold'])
    window.axitalic.set(window.axis_dict[index]['axis_text']['Italic'])

    window.title.set(window.axis_dict[index]['title'])
    window.tsize.set(window.axis_dict[index]['title_text']['size'])
    window.tbold.set(window.axis_dict[index]['title_text']['Bold'])
    window.titalic.set(window.axis_dict[index]['title_text']['Italic'])

    window.legend.set(window.axis_dict[window.selected_axis_value]['legend'])
    window.lgSize.set(window.axis_dict[window.selected_axis_value]['legendFontSize'])
