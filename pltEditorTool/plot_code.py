save_plot_list = ["import numpy as np\n",
"import matplotlib.pyplot as plt\n",
"from matplotlib.gridspec import GridSpec\n",
"\n",
"class plot():\n",
"    def __init__(self, axis_dict, fname):\n",
"        self.axis_list = axis_dict['axes']\n",
"        self.axis_data = axis_dict['axis data']\n",
"        self.fig = plt.figure(constrained_layout=True, \n",
"                              figsize=(axis_dict['fig_size'][1], \n",
"                                       axis_dict['fig_size'][0]))\n",
"        self.rows = axis_dict['gsr']\n",
"        self.cols = axis_dict['gsc']\n",
"        self.gs = GridSpec(self.rows, self.cols, figure=self.fig)\n",
"        self.save_fname = fname\n",
"        self.axis_names = []\n",
"        self.axes = []\n",
"        self.sharex = axis_dict['sharex']\n",
"        self.sharey = axis_dict['sharey']\n",
"        for i in range(axis_dict['gsr']):\n",
"            self.axes.append([])\n",
"            self.axis_names.append([])\n",
"            for j in range(axis_dict['gsc']):\n",
"                self.axes[i].append('')\n",
"                self.axis_names[i].append('')\n",
"                \n",
"\n",
"    def show_plot(self):\n",
"        label_length = ''\n",
"        cbar_map=[]\n",
"        cbar_axis=[]\n",
"        ax = []\n",
"        count = 0\n",
"        for axis in self.axis_list:\n",
"            data = self.axis_data[axis]\n",
"            ax.append(self.fig.add_subplot(self.gs[data['position'][0]:data['position'][0]+data['position'][2], \n",
"                                              data['position'][1]:data['position'][1]+data['position'][3]]))\n",
"            colorbar = 0\n",
"            for plot_num in range(len(data['plots'])):\n",
"                plot = data['plots_data'][plot_num]\n",
"                \n",
"                if plot['fill']['exist'] == 1 and len(plot['dif_top'])>0:\n",
"                    ax[count].fill_between(np.array(plot['x']),\n",
"                                    np.array(plot['y'])+np.array(plot['dif_top']),\n",
"                                    np.array(plot['y'])-np.array(plot['dif_bot']),\n",
"                                     alpha=plot['fill']['alpha'],\n",
"                                     edgecolor=plot['fill']['edge_col'],\n",
"                                     facecolor=plot['fill']['face_col'],\n",
"                                     linewidth=plot['fill']['line_wid'],\n",
"                                     linestyle=plot['fill']['line_sty'],\n",
"                                     label=plot['fill-label'])\n",
"                    label_length += 'label'\n",
"                \n",
"                no_err_data = (plot['y_err'].size == 0 and plot['x_err'].size == 0)\n",
"                if plot['scatter']['exist'] == 1:\n",
"                    if plot['scatter']['colorbar'] == 1:\n",
"                        colorbar = 1\n",
"                    # set cmap\n",
"                    color_map = plt.get_cmap(plot['scatter']['cmap'])\n",
"                    # check for color vector\n",
"                    if plot['scatter']['current_color'] == 'None':\n",
"                        color = plot['marker']['face_col']\n",
"                        colorbar = 0\n",
"                        norm=[]\n",
"                    else:\n",
"                        col_index = plot['scatter']['color_vector_names'].index(plot['scatter']['current_color'])\n",
"                        color = np.array(plot['scatter']['color_vectors'][col_index])                        \n",
"                        \n",
"                    # check for size vector\n",
"                    if plot['scatter']['current_size'] == 'None':\n",
"                        size = plot['marker']['size']**2\n",
"                    else:\n",
"                        sz_index = plot['scatter']['size_vector_names'].index(plot['scatter']['current_size'])\n",
"                        size = np.array(plot['scatter']['size_vectors'][sz_index])\n",
"                        size = ((size-size.min())/(size.max()-size.min()))*20*plot['marker']['size']\n",
"\n",
"                    cset = ax[count].scatter(x=plot['x'],y=plot['y'],\n",
"                                s=size,\n",
"                                c=color,\n",
"                                marker=plot['scatter']['type'],\n",
"                                alpha=plot['scatter']['alpha'],\n",
"                                edgecolors=plot['scatter']['edge'],\n",
"                                linewidths=plot['marker']['edge_wid'], \n",
"                                cmap=color_map)          \n",
"                    if colorbar == 1:\n",
"                        cbar_map.append(cset)\n",
"                        cbar_axis.append(ax[count])\n",
"                else:\n",
"                    if plot['ebar']['exist'] == 1 and not no_err_data:\n",
"                        if len(plot['y_err']) == 0:\n",
"                            #plot['y_err'] = np.zeros_like(np.array(plot['y']))\n",
"                            ax[count].errorbar(x=plot['x'],y=plot['y'],\n",
"                                    xerr=plot['x_err'],\n",
"                                    ecolor=plot['ebar']['color'],\n",
"                                    elinewidth=plot['ebar']['linew'],\n",
"                                    capsize=plot['ebar']['capsize'],\n",
"                                    capthick=plot['ebar']['capthick'],\n",
"                                    color=plot['line']['color'],\n",
"                                    linestyle=plot['line']['style'],\n",
"                                    linewidth=plot['line']['width'],\n",
"                                    marker=plot['marker']['type'],\n",
"                                    markeredgecolor=plot['marker']['edge_col'],\n",
"                                    markeredgewidth=plot['marker']['edge_wid'],\n",
"                                    markerfacecolor=plot['marker']['face_col'],\n",
"                                    markersize=plot['marker']['size'],\n",
"                                    label=plot['label'])\n",
"                        if len(plot['x_err']) == 0:\n",
"                            #plot['x_err'] = np.zeros_like(np.array(plot['x']))\n",
"                            ax[count].errorbar(x=plot['x'],y=plot['y'],\n",
"                                    yerr=plot['y_err'],\n",
"                                    ecolor=plot['ebar']['color'],\n",
"                                    elinewidth=plot['ebar']['linew'],\n",
"                                    capsize=plot['ebar']['capsize'],\n",
"                                    capthick=plot['ebar']['capthick'],\n",
"                                    color=plot['line']['color'],\n",
"                                    linestyle=plot['line']['style'],\n",
"                                    linewidth=plot['line']['width'],\n",
"                                    marker=plot['marker']['type'],\n",
"                                    markeredgecolor=plot['marker']['edge_col'],\n",
"                                    markeredgewidth=plot['marker']['edge_wid'],\n",
"                                    markerfacecolor=plot['marker']['face_col'],\n",
"                                    markersize=plot['marker']['size'],\n",
"                                    label=plot['label'])\n",
"                        if (len(plot['x_err']) != 0) and (len(plot['y_err']) != 0):\n",
"                            ax[count].errorbar(x=plot['x'],y=plot['y'],\n",
"                                    yerr=plot['y_err'],xerr=plot['x_err'],\n",
"                                    ecolor=plot['ebar']['color'],\n",
"                                    elinewidth=plot['ebar']['linew'],\n",
"                                    capsize=plot['ebar']['capsize'],\n",
"                                    capthick=plot['ebar']['capthick'],\n",
"                                    color=plot['line']['color'],\n",
"                                    linestyle=plot['line']['style'],\n",
"                                    linewidth=plot['line']['width'],\n",
"                                    marker=plot['marker']['type'],\n",
"                                    markeredgecolor=plot['marker']['edge_col'],\n",
"                                    markeredgewidth=plot['marker']['edge_wid'],\n",
"                                    markerfacecolor=plot['marker']['face_col'],\n",
"                                    markersize=plot['marker']['size'],\n",
"                                    label=plot['label'])\n",
"                        label_length += 'label'\n",
"                    else:\n",
"                        ax[count].plot(plot['x'],plot['y'],\n",
"                                color=plot['line']['color'],\n",
"                                linestyle=plot['line']['style'],\n",
"                                linewidth=plot['line']['width'],\n",
"                                marker=plot['marker']['type'],\n",
"                                markeredgecolor=plot['marker']['edge_col'],\n",
"                                markeredgewidth=plot['marker']['edge_wid'],\n",
"                                markerfacecolor=plot['marker']['face_col'],\n",
"                                markersize=plot['marker']['size'],\n",
"                                label=plot['label'])\n",
"                        label_length += 'label'\n",
"                    \n",
"            style = ['normal', 'italic']\n",
"            weight = ['normal', 'bold']\n",
"            scale = ['linear', 'log']\n",
"            # if colorbar == 1:\n",
"                # cbar_map.append(cm.ScalarMappable(norm=color, cmap=color_map))\n",
"                # cbar_axis.append(ax[count])\n",
"            ax[count].set_xlim(data['x_lim'])\n",
"            ax[count].set_ylim(data['y_lim']) \n",
"            ax[count].set_xscale(scale[data['xscale']])\n",
"            ax[count].set_yscale(scale[data['yscale']])\n",
"            if data['xticks'] == 0:\n",
"                ax[count].set_xticks([],[])\n",
"            if data['yticks'] == 0:\n",
"                ax[count].set_yticks([],[])\n",
"            ax[count].set_xlabel(data['x_label'], fontsize=data['axis_text']['size'], \n",
"                          fontstyle=style[data['axis_text']['Italic']], \n",
"                          fontweight=weight[data['axis_text']['Bold']])\n",
"            ax[count].set_ylabel(data['y_label'], fontsize=data['axis_text']['size'], \n",
"                          fontstyle=style[data['axis_text']['Italic']],  \n",
"                          fontweight=weight[data['axis_text']['Bold']])\n",
"            ax[count].set_title(data['title'], fontsize=data['title_text']['size'], \n",
"                          fontstyle=style[data['title_text']['Italic']],\n",
"                          fontweight=weight[data['title_text']['Bold']])\n",
"            if label_length != 0:\n",
"                if data['legend'] != 'None':\n",
"                    ax[count].legend(loc=data['legend'], \n",
"                              fontsize=data['legendFontSize'])\n",
"            count += 1\n",
"        if colorbar == 1:\n",
"            for i in range(len(cbar_map)):\n",
"                self.fig.colorbar(cbar_map[i], ax=cbar_axis[i])\n",
"        plt.show()\n",
"        \n",
"if __name__ == '__main__':\n",
"    data_dict = np.load('plot_data.npy',allow_pickle='TRUE').item()\n",
"    plot_obj = plot(data_dict, '')\n",
"    plot_obj.show_plot()\n"]

save_plot2_list = ["import numpy as np\n",
"import matplotlib.pyplot as plt\n",
"from matplotlib.gridspec import GridSpec\n",
"\n",
"class plot():\n",
"    def __init__(self, axis_dict, fname):\n",
"        self.axis_list = axis_dict['axes']\n",
"        self.axis_data = axis_dict['axis data']\n",
"        self.fig = plt.figure(constrained_layout=True, \n",
"                              figsize=(axis_dict['fig_size'][1], \n",
"                                       axis_dict['fig_size'][0]))\n",
"        self.rows = axis_dict['gsr']\n",
"        self.cols = axis_dict['gsc']\n",
"        self.gs = GridSpec(self.rows, self.cols, figure=self.fig)\n",
"        self.save_fname = fname\n",
"        self.axis_names = []\n",
"        self.axes = []\n",
"        self.sharex = axis_dict['sharex']\n",
"        self.sharey = axis_dict['sharey']\n",
"        for i in range(axis_dict['gsr']):\n",
"            self.axes.append([])\n",
"            self.axis_names.append([])\n",
"            for j in range(axis_dict['gsc']):\n",
"                self.axes[i].append('')\n",
"                self.axis_names[i].append('')\n",
"                \n",
"\n",
"    def show_plot2(self):\n",
"        label_length = ''\n",
"        cbar_map=[]\n",
"        cbar_axis=[]\n",
"        for axis in self.axis_list:\n",
"            data = self.axis_data[axis]\n",
"            self.axis_names[data['position'][0]][data['position'][1]] = axis\n",
"            \n",
"        last_row = self.axis_names[len(self.axis_names)-1]\n",
"        first_col = []\n",
"\n",
"        for i in range(self.rows):\n",
"            first_col.append(self.axis_names[i][0])\n",
"        \n",
"        for i in range(self.rows):\n",
"            for j in range(self.cols):\n",
"                if self.axis_names[i][j] != '':\n",
"                    label_length = ''\n",
"                    data = self.axis_data[self.axis_names[i][j]]\n",
"                    try:\n",
"                        if self.sharex == 1:\n",
"                            if self.sharey == 1:\n",
"                                if (self.axis_names[i][j] in last_row):\n",
"                                    if (self.axis_names[i][j] in first_col):\n",
"                                        y_label = self.axis_data[self.axis_names[i][j]]['y_label']\n",
"                                        x_label = self.axis_data[self.axis_names[i][j]]['x_label']\n",
"                                        x_lim = self.axis_data[self.axis_names[i][j]]['x_lim']\n",
"                                        y_lim = self.axis_data[self.axis_names[i][j]]['y_lim']\n",
"                                        x_scale = self.axis_data[self.axis_names[i][j]]['xscale']\n",
"                                        y_scale = self.axis_data[self.axis_names[i][j]]['yscale']\n",
"                                    else:\n",
"                                        y_label = ''\n",
"                                        y_lim = self.axis_data[self.axis_names[i][0]]['y_lim']\n",
"                                        x_label = self.axis_data[self.axis_names[i][j]]['x_label']\n",
"                                        x_lim = self.axis_data[self.axis_names[i][j]]['x_lim']\n",
"                                        x_scale = self.axis_data[self.axis_names[i][j]]['xscale']\n",
"                                        y_scale = self.axis_data[self.axis_names[i][0]]['yscale']\n",
"                                        \n",
"                                else:\n",
"                                    if (self.axis_names[i][j] in first_col):\n",
"                                        y_label = self.axis_data[self.axis_names[i][j]]['y_label']\n",
"                                        y_lim = self.axis_data[self.axis_names[i][j]]['y_lim']\n",
"                                        x_label = ''\n",
"                                        x_lim = self.axis_data[self.axis_names[len(self.axis_names)-1][j]]['x_lim']\n",
"                                        x_scale = self.axis_data[self.axis_names[len(self.axis_names)-1][j]]['xscale']\n",
"                                        y_scale = self.axis_data[self.axis_names[i][j]]['yscale']\n",
"                                    else:\n",
"                                        y_label = ''\n",
"                                        y_lim = self.axis_data[self.axis_names[i][0]]['y_lim']\n",
"                                        x_label = ''\n",
"                                        x_lim = self.axis_data[self.axis_names[len(self.axis_names)-1][j]]['x_lim']\n",
"                                        x_scale = self.axis_data[self.axis_names[len(self.axis_names)-1][j]]['xscale']\n",
"                                        y_scale = self.axis_data[self.axis_names[i][0]]['yscale']\n",
"                            else:\n",
"                                if (self.axis_names[i][j] in last_row):\n",
"                                    y_label = self.axis_data[self.axis_names[i][j]]['y_label']\n",
"                                    x_label = self.axis_data[self.axis_names[i][j]]['x_label']\n",
"                                    x_lim = self.axis_data[self.axis_names[i][j]]['x_lim']\n",
"                                    y_lim = self.axis_data[self.axis_names[i][j]]['y_lim']\n",
"                                    x_scale = self.axis_data[self.axis_names[i][j]]['xscale']\n",
"                                    y_scale = self.axis_data[self.axis_names[i][j]]['yscale']\n",
"                                else:\n",
"                                    y_label = self.axis_data[self.axis_names[i][j]]['y_label']\n",
"                                    y_lim = self.axis_data[self.axis_names[i][j]]['y_lim']\n",
"                                    x_label = ''\n",
"                                    x_lim = self.axis_data[self.axis_names[len(self.axis_names)-1][j]]['x_lim']\n",
"                                    x_scale = self.axis_data[self.axis_names[len(self.axis_names)-1][j]]['xscale']\n",
"                                    y_scale = self.axis_data[self.axis_names[i][j]]['yscale']\n",
"                        else: \n",
"                            if self.sharey == 1:\n",
"                                if (self.axis_names[i][j] in first_col):\n",
"                                    y_label = self.axis_data[self.axis_names[i][j]]['y_label']\n",
"                                    x_label = self.axis_data[self.axis_names[i][j]]['x_label']\n",
"                                    x_lim = self.axis_data[self.axis_names[i][j]]['x_lim']\n",
"                                    y_lim = self.axis_data[self.axis_names[i][j]]['y_lim']\n",
"                                    x_scale = self.axis_data[self.axis_names[i][j]]['xscale']\n",
"                                    y_scale = self.axis_data[self.axis_names[i][j]]['yscale']\n",
"                                else:\n",
"                                    y_label = ''\n",
"                                    y_lim = self.axis_data[self.axis_names[i][0]]['y_lim']\n",
"                                    x_label = self.axis_data[self.axis_names[i][j]]['x_label']\n",
"                                    x_lim = self.axis_data[self.axis_names[i][j]]['x_lim']\n",
"                                    x_scale = self.axis_data[self.axis_names[i][j]]['xscale']\n",
"                                    y_scale = self.axis_data[self.axis_names[i][0]]['yscale']\n",
"                            else:\n",
"                                y_label = self.axis_data[self.axis_names[i][j]]['y_label']\n",
"                                x_label = self.axis_data[self.axis_names[i][j]]['x_label']\n",
"                                x_lim = self.axis_data[self.axis_names[i][j]]['x_lim']\n",
"                                y_lim = self.axis_data[self.axis_names[i][j]]['y_lim']\n",
"                                x_scale = self.axis_data[self.axis_names[i][j]]['xscale']\n",
"                                y_scale= self.axis_data[self.axis_names[i][j]]['yscale']\n",
"                    except Exception as e:\n",
"                        # print(e.args)\n",
"                        messagebox.showerror(title='Plot error', \n",
"                                             message='Error encountered plotting figure. Ensure plots with shared x or shared y have matching columns or rows.')\n",
"                        return\n",
"                    \n",
"                    self.axes[i][j] = self.fig.add_subplot(self.gs[data['position'][0]:data['position'][0]+data['position'][2], \n",
"                                                  data['position'][1]:data['position'][1]+data['position'][3]])\n",
"                    for plot_num in range(len(data['plots'])):\n",
"                        plot = data['plots_data'][plot_num]\n",
"                        \n",
"                        if plot['fill']['exist'] == 1 and len(plot['dif_top'])>0:\n",
"                            self.axes[i][j].fill_between(np.array(plot['x']),\n",
"                                                         np.array(plot['y'])+np.array(plot['dif_top']),\n",
"                                                         np.array(plot['y'])-np.array(plot['dif_bot']),\n",
"                                                         alpha=plot['fill']['alpha'],\n",
"                                                         edgecolor=plot['fill']['edge_col'],\n",
"                                                         facecolor=plot['fill']['face_col'],\n",
"                                                         linewidth=plot['fill']['line_wid'],\n",
"                                                         linestyle=plot['fill']['line_sty'],\n",
"                                                         label=plot['fill-label'])\n",
"                            label_length += 'label'\n",
"                        \n",
"                        no_err_data = (plot['y_err'].size == 0 and plot['x_err'].size == 0)\n",
"                        if plot['scatter']['exist'] == 1:\n",
"                            if plot['scatter']['colorbar'] == 1:\n",
"                                colorbar = 1\n",
"                            # set cmap\n",
"                            color_map = plt.get_cmap(plot['scatter']['cmap'])\n",
"                            # check for color vector\n",
"                            if plot['scatter']['current_color'] == 'None':\n",
"                                color = plot['marker']['face_col']\n",
"                                colorbar = 0\n",
"                            else:\n",
"                                col_index = plot['scatter']['color_vector_names'].index(plot['scatter']['current_color'])\n",
"                                color = np.array(plot['scatter']['color_vectors'][col_index])\n",
"                                \n",
"                            # check for size vector\n",
"                            if plot['scatter']['current_size'] == 'None':\n",
"                                size = plot['marker']['size']**2\n",
"                            else:\n",
"                                sz_index = plot['scatter']['size_vector_names'].index(plot['scatter']['current_size'])\n",
"                                size = np.array(plot['scatter']['size_vectors'][sz_index])\n",
"                                size = ((size-size.min())/(size.max()-size.min()))*20*plot['marker']['size']\n",
"                            cset = self.axes[i][j].scatter(x=plot['x'],y=plot['y'],\n",
"                                        s=size,\n",
"                                        c=color,\n",
"                                        marker=plot['scatter']['type'],\n",
"                                        alpha=plot['scatter']['alpha'],\n",
"                                        edgecolors=plot['scatter']['edge'],\n",
"                                        linewidths=plot['marker']['edge_wid'], \n",
"                                        cmap=color_map)           \n",
"                            if colorbar == 1:\n",
"                                cbar_map.append(cset)\n",
"                                cbar_axis.append(self.axes[i][j])\n",
"                        \n",
"                        else:\n",
"                            if plot['ebar']['exist'] == 1 and not no_err_data:\n",
"                                if len(plot['y_err']) == 0:\n",
"                                    #plot['y_err'] = np.zeros_like(np.array(plot['y']))\n",
"                                    self.axes[i][j].errorbar(x=plot['x'],y=plot['y'],\n",
"                                            xerr=plot['x_err'],\n",
"                                            ecolor=plot['ebar']['color'],\n",
"                                            elinewidth=plot['ebar']['linew'],\n",
"                                            capsize=plot['ebar']['capsize'],\n",
"                                            capthick=plot['ebar']['capthick'],\n",
"                                            color=plot['line']['color'],\n",
"                                            linestyle=plot['line']['style'],\n",
"                                            linewidth=plot['line']['width'],\n",
"                                            marker=plot['marker']['type'],\n",
"                                            markeredgecolor=plot['marker']['edge_col'],\n",
"                                            markeredgewidth=plot['marker']['edge_wid'],\n",
"                                            markerfacecolor=plot['marker']['face_col'],\n",
"                                            markersize=plot['marker']['size'],\n",
"                                            label=plot['label'])\n",
"                                if len(plot['x_err']) == 0:\n",
"                                    #plot['x_err'] = np.zeros_like(np.array(plot['x']))\n",
"                                    self.axes[i][j].errorbar(x=plot['x'],y=plot['y'],\n",
"                                            yerr=plot['y_err'],\n",
"                                            ecolor=plot['ebar']['color'],\n",
"                                            elinewidth=plot['ebar']['linew'],\n",
"                                            capsize=plot['ebar']['capsize'],\n",
"                                            capthick=plot['ebar']['capthick'],\n",
"                                            color=plot['line']['color'],\n",
"                                            linestyle=plot['line']['style'],\n",
"                                            linewidth=plot['line']['width'],\n",
"                                            marker=plot['marker']['type'],\n",
"                                            markeredgecolor=plot['marker']['edge_col'],\n",
"                                            markeredgewidth=plot['marker']['edge_wid'],\n",
"                                            markerfacecolor=plot['marker']['face_col'],\n",
"                                            markersize=plot['marker']['size'],\n",
"                                            label=plot['label'])\n",
"                                if (len(plot['x_err']) != 0) and (len(plot['y_err']) != 0):\n",
"                                    self.axes[i][j].errorbar(x=plot['x'],y=plot['y'],\n",
"                                            yerr=plot['y_err'],xerr=plot['x_err'],\n",
"                                            ecolor=plot['ebar']['color'],\n",
"                                            elinewidth=plot['ebar']['linew'],\n",
"                                            capsize=plot['ebar']['capsize'],\n",
"                                            capthick=plot['ebar']['capthick'],\n",
"                                            color=plot['line']['color'],\n",
"                                            linestyle=plot['line']['style'],\n",
"                                            linewidth=plot['line']['width'],\n",
"                                            marker=plot['marker']['type'],\n",
"                                            markeredgecolor=plot['marker']['edge_col'],\n",
"                                            markeredgewidth=plot['marker']['edge_wid'],\n",
"                                            markerfacecolor=plot['marker']['face_col'],\n",
"                                            markersize=plot['marker']['size'],\n",
"                                            label=plot['label'])\n",
"                                label_length += 'label'\n",
"                            else:\n",
"                                self.axes[i][j].plot(plot['x'],plot['y'],\n",
"                                                     color=plot['line']['color'],\n",
"                                                     linestyle=plot['line']['style'],\n",
"                                                     linewidth=plot['line']['width'],\n",
"                                                     marker=plot['marker']['type'],\n",
"                                                     markeredgecolor=plot['marker']['edge_col'],\n",
"                                                     markeredgewidth=plot['marker']['edge_wid'],\n",
"                                                     markerfacecolor=plot['marker']['face_col'],\n",
"                                                     markersize=plot['marker']['size'],\n",
"                                                     label=plot['label'])\n",
"                                label_length += 'label'\n",
"                            \n",
"                    style = ['normal', 'italic']\n",
"                    weight = ['normal', 'bold']\n",
"                    scale = ['linear', 'log']\n",
"                    self.axes[i][j].set_xlim(x_lim)\n",
"                    self.axes[i][j].set_ylim(y_lim) \n",
"                    self.axes[i][j].set_xscale(scale[x_scale])\n",
"                    self.axes[i][j].set_yscale(scale[y_scale]) \n",
"                    if data['xticks'] == 0:\n",
"                        self.axes[i][j].set_xticks([],[])\n",
"                    if data['yticks'] == 0:\n",
"                        self.axes[i][j].set_yticks([],[])\n",
"                    self.axes[i][j].set_xlabel(x_label, \n",
"                                               fontsize=data['axis_text']['size'], \n",
"                                               fontstyle=style[data['axis_text']['Italic']],\n",
"                                               fontweight=weight[data['axis_text']['Bold']])\n",
"                    self.axes[i][j].set_ylabel(y_label, \n",
"                                               fontsize=data['axis_text']['size'], \n",
"                                               fontstyle=style[data['axis_text']['Italic']],\n",
"                                               fontweight=weight[data['axis_text']['Bold']])\n",
"                    self.axes[i][j].set_title(data['title'], \n",
"                                              fontsize=data['title_text']['size'], \n",
"                                              fontstyle=style[data['title_text']['Italic']], \n",
"                                              fontweight=weight[data['title_text']['Bold']])\n",
"                    if label_length != '':\n",
"                        if data['legend'] != 'None':\n",
"                            self.axes[i][j].legend(loc=data['legend'], \n",
"                                                   fontsize=data['legendFontSize'])\n",
"        if colorbar == 1:\n",
"            for i in range(len(cbar_map)):\n",
"                self.fig.colorbar(cbar_map[i], ax=cbar_axis[i])\n",
"        plt.show()\n",
"        \n",
"if __name__ == '__main__':\n",
"    data_dict = np.load('plot_data.npy',allow_pickle='TRUE').item()\n",
"    plot_obj = plot(data_dict, '')\n",
"    plot_obj.show_plot()\n"]



def write_code_file(save_dir, choice):
    if choice == 'save_plot':
        data = save_plot_list
    elif choice == 'save_plot2':
        data = save_plot2_list
        
    with open(save_dir+'figure_plot_code.py','w') as f:
        f.writelines(data)
       