import tkinter as tk
import platform
from copy import deepcopy
from tkinter import filedialog
from tkinter import messagebox
from tkcolorpicker import askcolor
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import get_backend

PLATFORM = platform.system()

# if get_backend() == "module://ipykernel.pylab.backend_inline":
    # root = tk.Tk()
    # messagebox.showerror(title="Inline Plotting",
                         # message="Plots may not display with inline backend. \nPlots should still be able to be saved. \nPlease consider running code from command line in order to ensure full functionality.")
    # root.destroy()

try:
    from .util import save_axis_data, save_plot_data, set_axis_data, set_plot_data
except ImportError:
    from util import save_axis_data, save_plot_data, set_axis_data, set_plot_data
try:
    from .plot_functions import plot_class
except ImportError:
    from plot_functions import plot_class
try:
    if PLATFORM == "Linux":
        from .tkGUI_linux import create_GUI
        plt.rcParams["font.family"] = 'DeJaVu Serif'
    elif PLATFORM == "Darwin":
        from .tkGUI_Mac import create_GUI
        plt.rcParams["font.family"] = 'DeJaVu Serif'
    else:
        from .tkGUI import create_GUI
        plt.rcParams["font.family"] = "Times New Roman"
except ImportError:
    if PLATFORM == "Linux":
        from tkGUI_linux import create_GUI
        plt.rcParams["font.family"] = 'DeJaVu Serif'
    elif PLATFORM == "Darwin":
        from tkGUI_Mac import create_GUI
        plt.rcParams["font.family"] = 'DeJaVu Serif'
    else:
        from tkGUI import create_GUI
        plt.rcParams["font.family"] = "Times New Roman"

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
        create_GUI(self)
        
    def ebar_col_h(self):
        col = askcolor(self.ebar_color.get())[1]
        if col != None:
            self.ebar_color.set(col)
            if PLATFORM == "Darwin":
                self.eb_col['fg'] = col
            else:
                self.eb_col['bg'] = col
                self.eb_col['activebackground'] = col
            

    def line_col_h(self):
        col = askcolor(self.line_color.get())[1]
        if col != None:
            self.line_color.set(col)
            if PLATFORM == "Darwin":
                self.l_col['fg'] = col
            else:
                self.l_col['bg'] = col
                self.l_col['activebackground'] = col

    def me_col_h(self):
        col = askcolor(self.mark_ec.get())[1]
        if col != None:
            self.mark_ec.set(col)
            if PLATFORM == "Darwin":
                self.m_ecol['fg'] = col
            else:
                self.m_ecol['bg'] = col
                self.m_ecol['activebackground'] = col

    def mf_col_h(self):
        col = askcolor(self.mark_fc.get())[1]
        if col != None:
            self.mark_fc.set(col)
            if PLATFORM == "Darwin":
                self.m_fcol['fg'] = col
            else:
                self.m_fcol['bg'] = col
                self.m_fcol['activebackground'] = col

    def fe_col_h(self):
        col = askcolor(self.fill_ec.get())[1]
        if col != None:
            self.fill_ec.set(col)
            if PLATFORM == "Darwin":
                self.f_ecol['fg'] = col
            else:
                self.f_ecol['bg'] = col
                self.f_ecol['activebackground'] = col
            

    def ff_col_h(self):
        col = askcolor(self.fill_fc.get())[1]
        if col != None:
            self.fill_fc.set(col)
            if PLATFORM == "Darwin":
                self.f_fcol['fg'] = col
            else:
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
                label = deepcopy(self.data_dict[item]['label'])
                fill_label = deepcopy(self.data_dict[item]['fill-label'])
                save_plot_data(self, item)
                self.data_dict[item]['label'] = label
                self.data_dict[item]['fill-label'] = fill_label

            self.multi_list.set('')
            event = self.current_data.get()
            set_plot_data(self, event)

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
        if event != self.selected_axis_value:
            save_axis_data(self, self.selected_axis_value)
            set_axis_data(self, event)
        else:
            return


    def plot_changed(self, event):
        if self.multi_select.get() == 1:
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
        elif event == self.selected_data_value:
            return
        else:
            save_plot_data(self, self.selected_data_value)
            set_plot_data(self, event)

    def add_first_axis(self):
        self.axis_dict['axis1'] = {'plots':[],
                                   'plots_data':[],
                                   'x_lim':[],
                                   'y_lim':[],
                                   'x_label':'x',
                                   'y_label':'y',
                                   'title':'Plot',
                                   'axis_text':{'size':16, 'Bold':0,
                                                'Italic':0, 'Underline':0},
                                   'title_text':{'size':16, 'Bold':1,
                                                 'Italic':0, 'Underline':0},
                                   'position':[0, 0, 1, 1],
                                   'legend':'best',
                                   'legendFontSize':12,
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
            'axis_text':{'size':16, 'Bold':0,
                         'Italic':0, 'Underline':0},
            'title_text':{'size':16, 'Bold':1,
                          'Italic':0, 'Underline':0},
            'position':[0, 0, 1, 1],
            'legend':'best',
            'legendFontSize':12,
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

        set_axis_data(self, self.axis_list[0])

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
            plot_obj.show_plot(False)
        else:
            plot_obj.show_plot_sharexy(False)

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
                plot_obj.show_plot(True)
            else:
                plot_obj.show_plot_sharexy(True)

    def collect_current_data(self):
        save_plot_data(self, self.selected_data_value)
        save_axis_data(self, self.current_axis.get())

class plotEditor():
    def __init__(self, x=[], y=[], x_err=[], y_err=[], fill=[], fill_alt=[], labels=[]):
        if str(type(x)) == "<class 'numpy.ndarray'>":
            try:
                self.__numpy_input(x, y, x_err, y_err, fill, fill_alt, labels)
            except Exception as e:
                root = tk.Tk()
                messagebox.showerror("Startup",
                                     "Failed to Initialize tool:\n{}".format(e))
                root.destroy()
                raise ValueError("Inputs not fully specified")
        elif str(type(x)) == "<class 'pandas.core.frame.DataFrame'>":
            try:
                self.__pandas_input(x, labels)
            except Exception as e:
                root = tk.Tk()
                messagebox.showerror("Startup",
                                     "Failed to Initialize tool:\n{}".format(e))
                root.destroy()
                raise ValueError("Inputs not fully specified")
        else:
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
                    self.labels.append("Dataset-{}".format(i))
            else:
                self.labels = []
                for i in range(len(x)):
                    self.labels.append(labels[i].replace(' ', '-'))


        self.same_vectors = []
        self.same_vector_names = []

        for i in range(len(self.x)):
            self.same_vectors.append([[]])
            self.same_vector_names.append(['None'])
            for j in range(len(self.x)):
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
        
    def __add_input_np(self, var, val, index):
        if str(type(val)) == "<class 'numpy.ndarray'>":
            if val.shape == self.x[index].shape:
                var.append(val)
            else:
                raise ValueError("All inputs must have same shape")
        elif val == []:
            var.append([])
            raise ValueError("Empty Input")
        else:
            try:
                if np.array(val).shape == self.x[index].shape:
                    var.append(np.array(val))
                else:
                    raise ValueError("All inputs must have same shape")
            except:
                raise ValueError("Mismatched inputs. Please ensure all inputs are of same type and size")
    
    def __add_input_str(self, var, val, index):
        if str(type(val)) == "<class 'str'>":
            if val == '':
                var.append("Dataset-{}".format(index))
            else:
                var.append(val.replace(' ','-'))
        else:
            var.append("Dataset-{}".format(index))
    
    def __numpy_input(self, x, y, x_err, y_err, fill, fill_alt, labels):
        self.x = []
        self.y = []
        self.x_err = []
        self.y_err = []
        self.dif_top = []
        self.dif_bot = []
        self.labels = []
        
        if len(x.shape) == 1:
            self.x.append(x)
            self.__add_input_np(self.y, y, 0)
            self.__add_input_np(self.x_err, x_err, 0)
            self.__add_input_np(self.y_err, y_err, 0)
            self.__add_input_np(self.dif_top, fill, 0)
            self.__add_input_np(self.dif_bot, fill_alt, 0)
            self.__add_input_str(self.labels, labels, 0)
        elif len(x.shape) == 2:
            for i in range(x.shape[1]):
                self.x.append(x[:,i])
                try:
                
                    try:
                        self.__add_input_np(self.y, y[:,i], i)
                    except ValueError:
                        raise ValueError("All datasets must have y values")
                    try:
                        try:
                            self.__add_input_np(self.x_err, x_err[:,i], i)
                        except IndexError:
                            self.x_err.append([])
                    except ValueError:
                        pass
                    try:
                        try:
                            self.__add_input_np(self.y_err, y_err[:,i], i)
                        except IndexError:
                            self.y_err.append([])
                    except ValueError:
                        pass
                    try:
                        try:
                            self.__add_input_np(self.dif_top, fill[:,i], i)
                        except IndexError:
                            self.dif_top.append([])
                    except ValueError:
                        pass
                    try:
                        try:
                            self.__add_input_np(self.dif_bot, fill_alt[:,i], i)
                        except IndexError:
                            try:
                                self.__add_input_np(self.dif_bot, fill[:,i], i)
                            except IndexError:
                                self.dif_bot.append([])
                    except ValueError:
                        pass
                except TypeError:
                    raise TypeError("All data inputs must have same type and shape")
                try:
                    self.__add_input_str(self.labels, labels[i], i)
                except IndexError:
                    self.__add_input_str(self.labels, '', i)
        elif len(x.shape) == 3:
            if x.shape[2] != 6:
                raise ValueError("X-input must have size 6 in last dimension")
            for i in range(x.shape[0]):
                self.x.append(x[i,:,0])
                try:
                    try:
                        self.__add_input_np(self.y, x[i,:,1], i)
                    except ValueError:
                        raise ValueError("All datasets must have y values")
                except IndexError:
                    raise IndexError("All datasets must have x and y values")
                try:
                    self.__add_input_np(self.x_err, x[i,:,2], i)
                except IndexError:
                    self.x_err.append([])
                try:
                    self.__add_input_np(self.y_err, x[i,:,3], i)
                except IndexError:
                    self.y_err.append([])
                try:
                    self.__add_input_np(self.dif_top, x[i,:,4], i)
                except IndexError:
                    self.dif_top.append([])
                try:
                    self.__add_input_np(self.dif_bot, x[i,:,5], i)
                except IndexError:
                    self.dif_bot.append([])
                try:
                    self.__add_input_str(self.labels, labels[i], i)
                except IndexError:
                    self.__add_input_str(self.labels, '', i)
        else:
            raise ValueError("X-input shape cannot have more than 3 dimensions")
            
    def __pandas_input(self, x, labels):
        self.x = []
        self.y = []
        self.x_err = []
        self.y_err = []
        self.dif_top = []
        self.dif_bot = []
        self.labels = []
        count = 0
        for label in x.columns:
            if label.split('.')[0] == 'x':
                self.x.append(np.array(x.loc[:,label]))
                try:
                    self.labels.append(labels[count].replace(' ','.'))
                except IndexError:
                    try:
                        self.labels.append(label.split('.')[1].replace(' ','-'))
                    except IndexError:
                        self.labels.append("Dataset-{}".format(count+1))
                count += 1
            if label.split('.')[0] == 'y':
                self.y.append(np.array(x.loc[:,label]))
            if label.split('.')[0] == 'x_err':
                self.x_err.append(np.array(x.loc[:,label]))
            if label.split('.')[0] == 'y_err':
                self.y_err.append(np.array(x.loc[:,label]))
            if label.split('.')[0] == 'fill':
                self.dif_top.append(np.array(x.loc[:,label]))
            if label.split('.')[0] == 'fill_alt':
                self.dif_bot.append(np.array(x.loc[:,label]))
            
        if self.x_err == []:
            for i in range(len(self.x)):
                self.x_err.append([])
        if self.y_err == []:
            for i in range(len(self.x)):
                self.y_err.append([])
        if self.dif_top == []:
            for i in range(len(self.x)):
                self.dif_top.append([])
        if self.dif_bot == []:
            self.dif_bot = self.dif_top
                
        a = len(self.x) != len(self.y)
        b = len(self.x) != len(self.x_err)
        c = len(self.x) != len(self.y_err)
        d = len(self.x) != len(self.dif_top)
        e = len(self.x) != len(self.dif_bot)
        
        if a or b or c or d or e:
            raise ValueError("Insufficient data provided. [x-err, y-err, fill, fill_alt] must be provided for all datasets or no datasets")

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
                'label': self.labels[i].replace('-', ' '),
                'fill-label': '{} fill'.format(self.labels[i].replace('-', ' ')),
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
                          'size':10,
                          'markevery':1},
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
        self.root.resizable(0, 0)
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        app = window(plot_data_Dict, master=self.root)
        if PLATFORM != "Darwin":
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
    import pandas as pd
    
    data = pd.read_excel("test_plot_data.xlsx", header=0)
    
    x_data = [np.array(data.loc[:,'x']), np.array(data.loc[:,'x.1'])]
    y_data = [np.array(data.loc[:,'y']), np.array(data.loc[:,'y.1'])]
    x_err_data = [np.array(data.loc[:,'x_err']), np.array(data.loc[:,'x_err.1'])]
    y_err_data = [np.array(data.loc[:,'y_err']), np.array(data.loc[:,'y_err.1'])]
    fill_data = [np.array(data.loc[:,'fill']), np.array(data.loc[:,'fill.1'])]
    fill_alt_data = [np.array(data.loc[:,'fill_alt']), np.array(data.loc[:,'fill_alt.1'])]
    labels_data = ['Experimental', 'Computation']
    
    print("Case 1: Ordinary List Style Input")
    
    plotEditor(x=x_data, y=y_data, x_err=x_err_data, y_err=y_err_data, 
                fill=fill_data, fill_alt=fill_alt_data)
    
    x_data = np.array(data.loc[:,'x.1'])
    y_data = np.array(data.loc[:,'y.1'])
    x_err_data = np.array(data.loc[:,'x_err.1'])
    y_err_data = np.array(data.loc[:,'y_err.1'])
    fill_data = np.array(data.loc[:,'fill.1'])
    fill_alt_data = np.array(data.loc[:,'fill_alt.1'])
    labels_data = 'Computation'
    
    print("Case 2: Single Numpy Array Input")
    plotEditor(x=x_data, y=y_data, x_err=x_err_data, y_err=y_err_data, 
                fill=fill_data, fill_alt=fill_alt_data)
    
    x_data = np.array([np.array(data.loc[:,'x']), np.array(data.loc[:,'x.1'])]).transpose()
    y_data = np.array([np.array(data.loc[:,'y']), np.array(data.loc[:,'y.1'])]).transpose()
    x_err_data = np.array([np.array(data.loc[:,'x_err']), np.array(data.loc[:,'x_err.1'])]).transpose()
    y_err_data = np.array([np.array(data.loc[:,'y_err']), np.array(data.loc[:,'y_err.1'])]).transpose()
    fill_data = np.array([np.array(data.loc[:,'fill']), np.array(data.loc[:,'fill.1'])]).transpose()
    fill_alt_data = np.array([np.array(data.loc[:,'fill_alt']), np.array(data.loc[:,'fill_alt.1'])]).transpose()
    labels_data = ['Experimental', 'Computation']
    
    print("Case 3: 2D Numpy Array Input")
    plotEditor(x=x_data, y=y_data, x_err=x_err_data, y_err=y_err_data, 
                fill=fill_data, fill_alt=fill_alt_data)
    
    input_data = np.zeros((2,101,6))
    input_data[0,:,0] = x_data[:,0]
    input_data[1,:,0] = x_data[:,1]
    input_data[0,:,1] = y_data[:,0]
    input_data[1,:,1] = y_data[:,1]
    input_data[0,:,2] = x_err_data[:,0]
    input_data[1,:,2] = x_err_data[:,1]
    input_data[0,:,3] = y_err_data[:,0]
    input_data[1,:,3] = y_err_data[:,1]
    input_data[0,:,4] = fill_data[:,0]
    input_data[1,:,4] = fill_data[:,1]
    input_data[0,:,5] = fill_alt_data[:,0]
    input_data[1,:,5] = fill_alt_data[:,1]
    print("Case 4: 3D Numpy Array Input")
    plotEditor(x=input_data)
    
    print("Case 5: Pandas DataFrame Input")
    plotEditor(x=data)    
