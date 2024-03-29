# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 05:44:53 2020

@author: richardcouperthwaite
"""

from tkinter import messagebox
import numpy as np
import platform
import matplotlib.pyplot as plt
plt.rcParams['mathtext.fontset'] = 'stix'
from matplotlib.gridspec import GridSpec
from matplotlib.ticker import AutoMinorLocator
from matplotlib import get_backend
from copy import deepcopy
try:
    from .plot_code import write_code_file
except ImportError:
    from plot_code import write_code_file


def plot_fillbetween(ax, plot) :
    return ax.fill_between(np.array(plot['x']),
                    np.array(plot['y'])+np.array(plot['dif_top']),
                    np.array(plot['y'])-np.array(plot['dif_bot']),
                    alpha=plot['fill']['alpha'],
                    edgecolor=plot['fill']['edge_col'],
                    facecolor=plot['fill']['face_col'],
                    linewidth=plot['fill']['line_wid'],
                    linestyle=plot['fill']['line_sty'],
                    label=plot['fill-label'])

def plot_errorbar_x(ax, plot):
    if plot['line']['exist'] == 1:
        linestyle = plot['line']['style']
    else:
        linestyle = ''
    if plot['marker']['exist'] == 1:
        marker_type = plot['marker']['type']
    else:
        marker_type = 'None'
    return ax.errorbar(x=plot['x'], y=plot['y'],
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
                alpha=plot['line']['alpha'],
                markevery=plot['marker']['markevery'],
                errorevery=plot['marker']['markevery'])

def plot_errorbar_y(ax, plot):
    if plot['line']['exist'] == 1:
        linestyle = plot['line']['style']
    else:
        linestyle = ''
    if plot['marker']['exist'] == 1:
        marker_type = plot['marker']['type']
    else:
        marker_type = 'None'
    return ax.errorbar(x=plot['x'], y=plot['y'],
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
                alpha=plot['line']['alpha'],
                markevery=plot['marker']['markevery'],
                errorevery=plot['marker']['markevery'])

def plot_errorbar_xy(ax, plot):
    if plot['line']['exist'] == 1:
        linestyle = plot['line']['style']
    else:
        linestyle = ''
    if plot['marker']['exist'] == 1:
        marker_type = plot['marker']['type']
    else:
        marker_type = 'None'
    return ax.errorbar(x=plot['x'], y=plot['y'],
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
                alpha=plot['line']['alpha'],
                markevery=plot['marker']['markevery'],
                errorevery=plot['marker']['markevery'])

def plot_plot(ax, plot):
    if plot['line']['exist'] == 1:
        linestyle = plot['line']['style']
    else:
        linestyle = ''
    if plot['marker']['exist'] == 1:
        marker_type = plot['marker']['type']
    else:
        marker_type = 'None'
    return ax.plot(plot['x'], plot['y'],
            color=plot['line']['color'],
            linestyle=linestyle,
            linewidth=plot['line']['width'],
            marker=marker_type,
            markeredgecolor=plot['marker']['edge_col'],
            markeredgewidth=plot['marker']['edge_wid'],
            markerfacecolor=plot['marker']['face_col'],
            markersize=plot['marker']['size'],
            label=plot['label'],
            alpha=plot['line']['alpha'],
            markevery=plot['marker']['markevery'])

def plot_bar(ax, plot):
    if (plot['barplot']['x-labels'] == []) or (len(plot['barplot']['x-labels']) != plot['x'].shape[0]):
        return ax.bar(plot['x']+plot['barplot']['x-position'], plot['y'],
                width=plot['barplot']['width'],
                bottom=plot['barplot']['y-position'],
                align=plot['barplot']['align'],
                color=plot['barplot']['facecolor'],
                edgecolor=plot['barplot']['edgecolor'],
                linewidth=plot['barplot']['linewidth'],
                alpha=plot['barplot']['alpha'],
                label=plot['label'])
    else:
        return ax.bar(plot['x']+plot['barplot']['x-position'], plot['y'],
                width=plot['barplot']['width'],
                bottom=plot['barplot']['y-position'],
                align=plot['barplot']['align'],
                color=plot['barplot']['facecolor'],
                edgecolor=plot['barplot']['edgecolor'],
                linewidth=plot['barplot']['linewidth'],
                alpha=plot['barplot']['alpha'],
                tick_label=plot['barplot']['x-labels'],
                label=plot['label'])

def plot_scatter(ax, plot):
    if plot['colorbar'] == 1:
        colorbar = 1
    else:
        colorbar = 0
    # set cmap
    color_map = plt.get_cmap(plot['scatter']['cmap'])
    # check for color vector
    if plot['scatter']['current_color'] == 'None':
        color = np.array(plot['scatter']['face_col'])
        color = np.expand_dims(color, axis=0)
        colorbar = 0
    else:
        col_index = plot['scatter']['color_vector_names'].index(plot['scatter']['current_color'])
        color = np.array(plot['scatter']['color_vectors'][col_index])

    # check for size vector
    if plot['scatter']['current_size'] == 'None':
        size = plot['scatter']['size']**2
    else:
        sz_index = plot['scatter']['size_vector_names'].index(plot['scatter']['current_size'])
        size = np.array(plot['scatter']['size_vectors'][sz_index])
        size = ((size-size.min())/(size.max()-size.min()))*20*plot['scatter']['size']
    cset = ax.scatter(x=plot['x'],
                      y=plot['y'],
                      s=size,
                      c=color,
                      marker=plot['scatter']['type'],
                      alpha=plot['scatter']['alpha'],
                      edgecolors=np.expand_dims(np.array(plot['scatter']['edge']), axis=0),
                      linewidths=plot['marker']['edge_wid'],
                      cmap=color_map,
                      label=plot['label'])
    return colorbar, cset



def plot_addlegend_labels(ax, data, label_length, bar_plot):
    style = ['normal', 'italic']
    weight = ['normal', 'bold']
    scale = ['linear', 'log']
    if not bar_plot:
        ax.set_xlim(data['x_lim'])
        ax.set_ylim(data['y_lim'])
        ax.set_xscale(scale[data['xscale']])
        ax.set_yscale(scale[data['yscale']])
        ax.tick_params(labelsize=data['axis_text']['size']-3)
        if data['xticks'] == 0:
            ax.set_xticks([])
        else:
            if scale[data['xscale']] == 'linear':
                ax.xaxis.set_minor_locator(AutoMinorLocator())
                ax.tick_params(which='major', length=7)
                ax.tick_params(which='minor', length=4)
        if data['yticks'] == 0:
            ax.set_yticks([])
        else:
            if scale[data['yscale']] == 'linear':
                ax.yaxis.set_minor_locator(AutoMinorLocator())
                ax.tick_params(which='major', length=7)
                ax.tick_params(which='minor', length=4)
    ax.set_xlabel(
        data['x_label'], fontsize=data['axis_text']['size'],
        fontstyle=style[data['axis_text']['Italic']],
        fontweight=weight[data['axis_text']['Bold']])
    ax.set_ylabel(
        data['y_label'], fontsize=data['axis_text']['size'],
        fontstyle=style[data['axis_text']['Italic']],
        fontweight=weight[data['axis_text']['Bold']])
    ax.set_title(
        data['title'], fontsize=data['title_text']['size'],
        fontstyle=style[data['title_text']['Italic']],
        fontweight=weight[data['title_text']['Bold']],wrap=True)
    if label_length != '':
        if data['legend'] != 'None':
            ax.legend(loc=data['legend'],
                             fontsize=data['legendFontSize'])



def sharexy_axisdata(window, last_row, first_col, i, j):
    if window.sharex == 1:
        if window.sharey == 1:
            if window.axis_names[i][j] in last_row:
                if window.axis_names[i][j] in first_col:
                    pass
                else:
                    window.axis_data[window.axis_names[i][j]]['y_label'] = ''
                    window.axis_data[window.axis_names[i][j]]['yticks'] = False
                    window.axis_data[window.axis_names[i][j]]['y_lim'] = deepcopy(window.axis_data[window.axis_names[i][0]]['y_lim'])
                    window.axis_data[window.axis_names[i][j]]['yscale'] = deepcopy(window.axis_data[window.axis_names[i][0]]['yscale'])
            else:
                if window.axis_names[i][j] in first_col:
                    window.axis_data[window.axis_names[i][j]]['x_label'] = ''
                    window.axis_data[window.axis_names[i][j]]['xticks'] = False
                    window.axis_data[window.axis_names[i][j]]['x_lim'] = deepcopy(window.axis_data[window.axis_names[-1][j]]['x_lim'])
                    window.axis_data[window.axis_names[i][j]]['xscale'] = deepcopy(window.axis_data[window.axis_names[-1][j]]['xscale'])
                else:
                    window.axis_data[window.axis_names[i][j]]['x_label'] = ''
                    window.axis_data[window.axis_names[i][j]]['y_label'] = ''
                    window.axis_data[window.axis_names[i][j]]['xticks'] = False
                    window.axis_data[window.axis_names[i][j]]['yticks'] = False
                    window.axis_data[window.axis_names[i][j]]['x_lim'] = deepcopy(window.axis_data[window.axis_names[-1][j]]['x_lim'])
                    window.axis_data[window.axis_names[i][j]]['xscale'] = deepcopy(window.axis_data[window.axis_names[-1][j]]['xscale'])
                    window.axis_data[window.axis_names[i][j]]['y_lim'] = deepcopy(window.axis_data[window.axis_names[i][0]]['y_lim'])
                    window.axis_data[window.axis_names[i][j]]['yscale'] = deepcopy(window.axis_data[window.axis_names[i][0]]['yscale'])
        else:
            if window.axis_names[i][j] in last_row:
                pass
            else:
                window.axis_data[window.axis_names[i][j]]['x_label'] = ''
                window.axis_data[window.axis_names[i][j]]['xticks'] = False
                window.axis_data[window.axis_names[i][j]]['x_lim'] = deepcopy(window.axis_data[window.axis_names[-1][j]]['x_lim'])
                window.axis_data[window.axis_names[i][j]]['xscale'] = deepcopy(window.axis_data[window.axis_names[-1][j]]['xscale'])
    else:
        if window.sharey == 1:
            if window.axis_names[i][j] in first_col:
                pass
            else:
                window.axis_data[window.axis_names[i][j]]['y_label'] = ''
                window.axis_data[window.axis_names[i][j]]['yticks'] = False
                window.axis_data[window.axis_names[i][j]]['y_lim'] = deepcopy(window.axis_data[window.axis_names[i][0]]['y_lim'])
                window.axis_data[window.axis_names[i][j]]['yscale'] = deepcopy(window.axis_data[window.axis_names[i][0]]['yscale'])
        else:
            pass




class plot_class():
    def __init__(self, axis_dict, fname):
        self.axis_dict = axis_dict
        self.axis_list = axis_dict['axes']
        self.axis_data = axis_dict['axis data']
        if self.axis_dict['Fig_legend']['position'] == 'None':
            const_layout = True
        else:
            const_layout = False
        self.fig = plt.figure(num=1, constrained_layout=const_layout,
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


    def show_plot(self, save, window):
        label_length = ''
        cbar_map = []
        cbar_axis = []
        ax = []
        colorbar = 0
        count = 0

        plots_for_legend = []
        labels_for_legend = []
        axis_font_size = 0
        for axis in self.axis_list:
            data = self.axis_data[axis]
            axis_font_size = data['axis_text']['size']
            ax.append(self.fig.add_subplot(
                self.gs[data['position'][0]:data['position'][0]+data['position'][2],
                        data['position'][1]:data['position'][1]+data['position'][3]]))

            current_axis_labels = []
            bar_plot_on_axis = False
            for plot_num in range(len(data['plots'])):
                plot = data['plots_data'][plot_num]

                if plot['fill']['exist'] == 1 and len(plot['dif_top']) > 0:
                    if (plot['fill-label'] not in current_axis_labels) and (plot['fill-label'] != ''):
                        plots_for_legend.append(plot_fillbetween(ax[count], plot))
                        labels_for_legend.append(plot['fill-label'])
                    else:
                        plot_fillbetween(ax[count], plot)
                    label_length += 'label'

                no_err_data = (plot['y_err'].size == 0 and plot['x_err'].size == 0)
                if plot['scatter']['exist'] == 1:
                    colorbar, cset = plot_scatter(ax[count], plot)
                    plots_for_legend.append(cset)
                    label_length += 'label'
                    if colorbar == 1:
                        cbar_map.append(cset)
                        cbar_axis.append(ax[count])
                else:
                    if plot['barplot']['exist'] == 0:
                        if plot['ebar']['exist'] == 1 and not no_err_data:
                            if len(plot['y_err']) == 0:
                                if (plot['label'] not in current_axis_labels) and (plot['label'] != ''):
                                    plots_for_legend.append(plot_errorbar_y(ax[count], plot)[0])
                                    labels_for_legend.append(plot['label'])
                                else:
                                    plot_errorbar_y(ax[count], plot)
                            if len(plot['x_err']) == 0:
                                if (plot['label'] not in current_axis_labels) and (plot['label'] != ''):
                                    plots_for_legend.append(plot_errorbar_x(ax[count], plot)[0])
                                    labels_for_legend.append(plot['label'])
                                else:
                                    plot_errorbar_x(ax[count], plot)
                            if (len(plot['x_err']) != 0) and (len(plot['y_err']) != 0):
                                if (plot['label'] not in current_axis_labels) and (plot['label'] != ''):
                                    plots_for_legend.append(plot_errorbar_xy(ax[count], plot)[0])
                                    labels_for_legend.append(plot['label'])
                                else:
                                    plot_errorbar_xy(ax[count], plot)
                            label_length += 'label'
                        else:
                            if (plot['label'] not in current_axis_labels) and (plot['label'] != ''):
                                if (plot['label'] not in current_axis_labels) and (plot['label'] != ''):
                                    plots_for_legend.append(plot_plot(ax[count], plot)[0])
                                    labels_for_legend.append(plot['label'])
                                else:
                                    plot_plot(ax[count], plot)
                            label_length += 'label'
                    else:
                        bar_plot_on_axis = True
                        label_length += 'label'
                        if (plot['label'] not in current_axis_labels) and (plot['label'] != ''):
                            if (plot['label'] not in current_axis_labels) and (plot['label'] != ''):
                                plots_for_legend.append(plot_bar(ax[count], plot)[0])
                                # labels_for_legend.append(plot['label'])
                            else:
                                plot_bar(ax[count], plot)


                current_axis_labels.append(plot['fill-label'])
                current_axis_labels.append(plot['label'])

            plot_addlegend_labels(ax[count], data, label_length, bar_plot_on_axis)
            count += 1
        if self.axis_dict['Fig_title']['title'] != '':
            weights = ['normal','bold']
            style = ['normal','italic']
            self.fig.suptitle(self.axis_dict['Fig_title']['title'],
                              fontstyle=style[self.axis_dict['Fig_title']['italic']],
                              fontweight=weights[self.axis_dict['Fig_title']['bold']],
                              fontsize=self.axis_dict['Fig_title']['size'],
                              wrap=True)
        if self.axis_dict['Fig_legend']['position'] != 'None':
            self.fig.legend(handles=plots_for_legend, #labels=labels_for_legend,
                            loc=self.axis_dict['Fig_legend']['position'],
                            ncol=self.axis_dict['Fig_legend']['ncol'],
                            fontsize=self.axis_dict['Fig_legend']['size'])
            plt.subplots_adjust(top=self.axis_dict['Fig_legend']['top'],
                                bottom=self.axis_dict['Fig_legend']['bottom'],
                                left=self.axis_dict['Fig_legend']['left'],
                                right=self.axis_dict['Fig_legend']['right'],
                                wspace=self.axis_dict['Fig_legend']['wspace'],
                                hspace=self.axis_dict['Fig_legend']['hspace'],)
        if len(cbar_map) > 0:
            for i in range(len(cbar_map)):
                cbar = self.fig.colorbar(cbar_map[i], ax=cbar_axis[i])
                cbar.ax.tick_params(labelsize=plot['scatter']['cbarTextSize']-4)
                cbar.set_label(plot['scatter']['cbarTitle'], size=plot['scatter']['cbarTextSize'])
        if save:
            self.fig.set_dpi(600)
            self.fig.savefig(self.save_fname, bbox_inches='tight')
            save_dir_list = self.save_fname.split('/')
            save_dir = ''
            for i in range(len(save_dir_list)-1):
                save_dir += save_dir_list[i] + '/'
            fname = save_dir_list[-1].split(".")[0]
            np.save("{}/{}_plot_data.npy".format(save_dir,fname), self.axis_dict)
            write_code_file(save_dir, fname, 'normal')
        else:
            if platform.system() != "Darwin":
                self.fig.set_dpi(150)
            if window.chbInWindowPlot.isChecked():
                window.addmpl(self.fig)
            else:
                plt.show()

    def show_plot_sharexy(self, save, window):
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

        print(last_row)
        print(first_col)

        for i in range(self.rows):
            for j in range(self.cols):
                if self.axis_names[i][j] != '':
                    bar_plot_on_axis = False
                    label_length = ''
                    data = self.axis_data[self.axis_names[i][j]]
                    try:
                        sharexy_axisdata(self, last_row, first_col, i, j)
                    except KeyError:
                        messagebox.showerror(title='Plot error',
                                             message='Error encountered plotting figure. Ensure plots with shared x or shared y have matching columns or rows.')
                        return

                    self.axes[i][j] = self.fig.add_subplot(
                        self.gs[data['position'][0]:data['position'][0]+data['position'][2],
                                data['position'][1]:data['position'][1]+data['position'][3]])
                    for plot_num in range(len(data['plots'])):
                        plot = data['plots_data'][plot_num]

                        if plot['fill']['exist'] == 1 and len(plot['dif_top']) > 0:
                            plot_fillbetween(self.axes[i][j], plot)
                            label_length += 'label'

                        no_err_data = (plot['y_err'].size == 0 and plot['x_err'].size == 0)
                        if plot['barplot']['exist'] == 0:
                            if plot['scatter']['exist'] == 1:
                                colorbar, cset = plot_scatter(self.axes[i][j], plot)
                                label_length += 'label'
                                if colorbar == 1:
                                    cbar_map.append(cset)
                                    cbar_axis.append(self.axes[i][j])

                            else:
                                if plot['ebar']['exist'] == 1 and not no_err_data:
                                    if len(plot['y_err']) == 0:
                                        plot_errorbar_y(self.axes[i][j], plot)
                                    if len(plot['x_err']) == 0:
                                        plot_errorbar_x(self.axes[i][j], plot)
                                    if (len(plot['x_err']) != 0) and (len(plot['y_err']) != 0):
                                        plot_errorbar_xy(self.axes[i][j], plot)
                                    label_length += 'label'
                                else:
                                    plot_plot(self.axes[i][j], plot)
                                    label_length += 'label'
                        else:
                            plot_bar(self.axes[i][j], plot)
                            bar_plot_on_axis = True

                    plot_addlegend_labels(self.axes[i][j], data, label_length, bar_plot_on_axis)

        if self.axis_dict['Fig_title']['title'] != '':
            weights = ['normal','bold']
            style = ['normal','italic']
            self.fig.suptitle(self.axis_dict['Fig_title']['title'],
                              fontstyle=style[self.axis_dict['Fig_title']['italic']],
                              fontweight=weights[self.axis_dict['Fig_title']['bold']],
                              fontsize=self.axis_dict['Fig_title']['size'],
                              wrap=True)
        if self.axis_dict['Fig_legend']['position'] != 'None':
            self.fig.legend(handles=plots_for_legend, #labels=labels_for_legend,
                            loc=self.axis_dict['Fig_legend']['position'],
                            ncol=self.axis_dict['Fig_legend']['ncol'],
                            fontsize=self.axis_dict['Fig_legend']['size'])
            plt.subplots_adjust(top=self.axis_dict['Fig_legend']['top'],
                                bottom=self.axis_dict['Fig_legend']['bottom'],
                                left=self.axis_dict['Fig_legend']['left'],
                                right=self.axis_dict['Fig_legend']['right'],
                                wspace=self.axis_dict['Fig_legend']['wspace'],
                                hspace=self.axis_dict['Fig_legend']['hspace'],)
        if len(cbar_map) > 0:
            for i in range(len(cbar_map)):
                cbar = self.fig.colorbar(cbar_map[i], ax=cbar_axis[i])
                cbar.ax.tick_params(labelsize=plot['scatter']['cbarTextSize']-4)
                cbar.set_label(plot['scatter']['cbarTitle'], size=plot['scatter']['cbarTextSize'])
        if save:
            self.fig.set_dpi(600)
            self.fig.savefig(self.save_fname)
            save_dir_list = self.save_fname.split('/')
            save_dir = ''
            for i in range(len(save_dir_list)-1):
                save_dir += save_dir_list[i] + '/'
            fname = save_dir_list[-1].split(".")[0]
            np.save("{}/{}_plot_data.npy".format(save_dir,fname), self.axis_dict)
            write_code_file(save_dir, fname, 'share_xy')
        else:
            if platform.system() != "Darwin":
                self.fig.set_dpi(150)
            if platform.system() != "Linux":
                if get_backend() != "module://ipykernel.pylab.backend_inline":
                    if window.chbInWindowPlot.isChecked():
                        window.addmpl(self.fig)
                    else:
                        self.fig.show()
                else:
                    if window.chbInWindowPlot.isChecked():
                        window.addmpl(self.fig)
                    else:
                        plt.show()
            else:
                if window.chbInWindowPlot.isChecked():
                    window.addmpl(self.fig)
                else:
                    plt.show()
