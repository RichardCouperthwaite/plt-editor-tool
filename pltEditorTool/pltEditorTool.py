# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 15:14:52 2017

@author: richardc
"""
from sys import argv
from os import getcwd
from PyQt5 import uic, QtWidgets, QtGui
from tkcolorpicker import askcolor
import matplotlib.pyplot as plt
import numpy as np
import platform
import tkinter as tk
from tkinter import messagebox

PLATFORM = platform.system()

# try:
#     from .util import save_axis_data, save_plot_data, set_axis_data, set_plot_data
# except ImportError:
#     from util import save_axis_data, save_plot_data, set_axis_data, set_plot_data
try:
    from .plot_functions import plot_class
except ImportError:
    from plot_functions import plot_class


if PLATFORM == "Linux":
    plt.rcParams["font.family"] = 'DeJaVu Serif'
elif PLATFORM == "Darwin":
    plt.rcParams["font.family"] = 'DeJaVu Serif'
else:
    plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['mathtext.fontset'] = 'stix'

form_class = uic.loadUiType("./pltEditorGUI-1.ui")[0]

class MyWindowClass(QtWidgets.QMainWindow, form_class):
    def __init__(self, parent, data_dict):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.data_dict = data_dict
        self.selected_plots = []
        self.axis_dict = {}
        add_first_axis(self)
        set_axis_data(self, 'axis1')
        self.axis_count = 1
        self.populate_GUI()
        self.current_plot = self.cbPlotSelect.currentText()
        self.selected_axis_value = self.cbAxisList.currentText()
        self.cbPlotSelect.currentIndexChanged.connect(self.plot_changed)
        self.cbAxisList.currentIndexChanged.connect(self.axis_changed)
        self.chbSelMult.stateChanged.connect(self.select_multi)
        self.chbS.stateChanged.connect(self.scatter_selected)
        self.chbEB.stateChanged.connect(self.normal_plot_selected)
        self.chbL.stateChanged.connect(self.normal_plot_selected)
        self.chbM.stateChanged.connect(self.normal_plot_selected)
        self.chbF.stateChanged.connect(self.normal_plot_selected)
        self.btnClearSel.clicked.connect(self.clear_selected)
        self.btnEBCol.clicked.connect(self.ebColChange)
        self.btnLCol.clicked.connect(self.lColChange)
        self.btnMEC.clicked.connect(self.meColChange)
        self.btnMFC.clicked.connect(self.mfColChange)
        self.btnFFC.clicked.connect(self.ffColChange)
        self.btnFEC.clicked.connect(self.feColChange)
        self.btnScatECol.clicked.connect(self.seColChange)
        self.btnScatFCol.clicked.connect(self.sfColChange)
        self.btnAddAxis.clicked.connect(self.add_axis)
        self.btnRemAxis.clicked.connect(self.rem_axis)
        self.btnAddPlot.clicked.connect(self.add_plot)
        self.btnRemPlot.clicked.connect(self.rem_plot)
        self.btnGenPlot.clicked.connect(self.show_plot)
        self.btnSavePlot.clicked.connect(self.save_plot)
        
    def populate_GUI(self):
        self.tabWidget.setCurrentIndex(0)
        self.cbPlotSelect.addItems(self.data_dict.keys())
        self.cbAllData.addItems(self.data_dict.keys())
        set_plot_data(self, list(self.data_dict.keys())[0])
        
    def ebColChange(self):
        new_col = get_color(self.colors['Errorbar'])
        sSheet = 'background-color: rgb({}, {}, {});'.format(new_col[0]*255, 
                                                             new_col[1]*255, 
                                                             new_col[2]*255)
        self.btnEBCol.setStyleSheet(sSheet)
        self.colors['Errorbar'] = new_col
    
    def lColChange(self):
        new_col = get_color(self.colors['Line'])
        sSheet = 'background-color: rgb({}, {}, {});'.format(new_col[0]*255, 
                                                             new_col[1]*255, 
                                                             new_col[2]*255)
        self.btnLCol.setStyleSheet(sSheet)
        self.colors['Line'] = new_col
        
    def meColChange(self):
        new_col = get_color(self.colors['MarkerEdge'])
        sSheet = 'background-color: rgb({}, {}, {});'.format(new_col[0]*255, 
                                                             new_col[1]*255, 
                                                             new_col[2]*255)
        self.btnMEC.setStyleSheet(sSheet)
        self.colors['MarkerEdge'] = new_col
        
    def mfColChange(self):
        new_col = get_color(self.colors['MarkerFace'])
        sSheet = 'background-color: rgb({}, {}, {});'.format(new_col[0]*255, 
                                                             new_col[1]*255, 
                                                             new_col[2]*255)
        self.btnMFC.setStyleSheet(sSheet)
        self.colors['MarkerFace'] = new_col
        
    def ffColChange(self):
        new_col = get_color(self.colors['FillFace'])
        sSheet = 'background-color: rgb({}, {}, {});'.format(new_col[0]*255, 
                                                             new_col[1]*255, 
                                                             new_col[2]*255)
        self.btnFFC.setStyleSheet(sSheet)
        self.colors['FillFace'] = new_col
        
    def feColChange(self):
        new_col = get_color(self.colors['FillEdge'])
        sSheet = 'background-color: rgb({}, {}, {});'.format(new_col[0]*255, 
                                                             new_col[1]*255, 
                                                             new_col[2]*255)
        self.btnFEC.setStyleSheet(sSheet)
        self.colors['FillEdge'] = new_col
        
    def seColChange(self):
        new_col = get_color(self.colors['ScatterEdge'])
        sSheet = 'background-color: rgb({}, {}, {});'.format(new_col[0]*255, 
                                                             new_col[1]*255, 
                                                             new_col[2]*255)
        self.btnScatECol.setStyleSheet(sSheet)
        self.colors['ScatterEdge'] = new_col
        
    def sfColChange(self):
        new_col = get_color(self.colors['ScatterFace'])
        sSheet = 'background-color: rgb({}, {}, {});'.format(new_col[0]*255, 
                                                             new_col[1]*255, 
                                                             new_col[2]*255)
        self.btnScatFCol.setStyleSheet(sSheet)
        self.colors['ScatterFace'] = new_col
        
    def select_multi(self):
        if self.chbSelMult.isChecked():
            self.lstPlotSel.addItem(self.current_plot)
            self.selected_plots.append(self.current_plot)
        else:
            for i in range(self.lstPlotSel.count()):
                save_plot_data(self, self.lstPlotSel.item(i).text(), True)
            self.selected_plots = []
            self.lstPlotSel.clear()
            
        pass
    
    def clear_selected(self):
        remaining_items = []
        for i in range(self.lstPlotSel.count()):
            if self.lstPlotSel.item(i) not in self.lstPlotSel.selectedItems():
                remaining_items.append(self.lstPlotSel.item(i).text())
                
        self.lstPlotSel.clear()
        self.lstPlotSel.addItems(remaining_items)
        self.selected_plots = remaining_items
        
    def scatter_selected(self):
        if self.chbS.isChecked():
            self.chbEB.setChecked(False)
            self.chbL.setChecked(False)
            self.chbM.setChecked(False)
            self.chbF.setChecked(False)
            self.chbS.setChecked(True)
        else:
            if (not self.chbEB.isChecked()) and \
                (not self.chbL.isChecked()) and \
                (not self.chbM.isChecked()) and \
                (not self.chbF.isChecked()):
                    self.chbL.setChecked(True)
        
    def normal_plot_selected(self):
        if self.chbS.isChecked():
            self.chbS.setChecked(False)

    def plot_changed(self):
        event = self.cbPlotSelect.currentText() 
        if self.chbSelMult.isChecked():
            if event not in self.selected_plots:
                self.lstPlotSel.addItem(event)
                self.selected_plots.append(event)
        # save current plot data
        else:
            save_plot_data(self, self.current_plot)
            set_plot_data(self, event)
            self.current_plot = event
            
    def add_axis(self):
        add_new_axis(self)
    
    def rem_axis(self):
        del_curr_axis(self)
            
    def axis_changed(self):
        event = self.cbAxisList.currentText()
        if event != self.selected_axis_value:
            try:
                save_axis_data(self, self.selected_axis_value)
                set_axis_data(self, event)
                self.selected_axis_value = event
            except KeyError:
                return
        else:
            return
        
    def add_plot(self):
        add_plot_to_axis(self)
        
    def rem_plot(self):
        remove_plot_from_axis(self)
    
    def show_plot(self):
        plt.close(1)
        self.collect_current_data()
        test_grid = np.zeros((self.sbRowNum.value(), self.sbColNum.value()))

        plot_dict = {}
        plot_dict['axes'] = list(self.axis_dict.keys())
        plot_dict['axis data'] = self.axis_dict
        plot_dict['fig_size'] = [2+2*self.sbRowNum.value(), 2.5+2.5*self.sbColNum.value()]
        plot_dict['gsr'] = self.sbRowNum.value()
        plot_dict['gsc'] = self.sbColNum.value()
        plot_dict['sharex'] = self.chbShareX.isChecked()
        plot_dict['sharey'] = self.chbShareY.isChecked()
        plot_dict['Fig_title'] = {'title':self.eFigTitle.text(),
                                  'size':self.sbFigTitSz.value(),
                                  'bold':self.chbFigTitBold.isChecked(),
                                  'italic':self.chbFigTitIt.isChecked()}
        plot_dict['Fig_legend'] = {'position':self.cbFigLegPos.currentText(),
                                   'size':self.sbFigLegFontSz.value(),
                                   'ncol':self.sbFigLegNcol.value(),
                                   'correction':self.sbFigPlotCor.value()}
        
        plot_obj = plot_class(plot_dict, '')

        try:
            for axis in plot_dict['axes']:
                data = plot_dict['axis data'][axis]
                for i in range(data['position'][2]):
                    for j in range(data['position'][3]):
                        test_grid[data['position'][0]+i, data['position'][1]+j] = 1
            if np.sum(test_grid) != plot_dict['gsr']*plot_dict['gsc']:
                QtWidgets.QMessageBox.warning(self, 'Grid Error', "All Grid Spaces must be filled!")
                return
        except IndexError:
            QtWidgets.QMessageBox.warning(self, 'Grid Error', "Grid index of plot exceeds Grid Bounds!")
            return

        if (self.chbShareX.isChecked() == 0) and (self.chbShareY.isChecked() == 0):
            plot_obj.show_plot(False)
            # print(plot_dict)
        else:
            # plot_obj.show_plot_sharexy(False)
            pass
        
    def save_plot(self):
        x = [1,2,3,4,5]
        y = [2,3,4,5,6]
        plt.plot(x,y)
        plt.show()
        
    def collect_current_data(self):
        save_plot_data(self, self.current_plot)
        save_axis_data(self, self.selected_axis_value)



def get_color(color):
    currColor = QtGui.QColor.fromRgb(color[0],color[1],color[2])
    col = QtWidgets.QColorDialog.getColor(initial=currColor)
    return (col.getRgb()[0]/255, col.getRgb()[1]/255, col.getRgb()[2]/255)

def set_plot_data(window, index):
    currentData = window.data_dict[index]
    window.colors = {'MarkerEdge': currentData['marker']['edge_col'],
                   'MarkerFace': currentData['marker']['face_col'],
                   'Errorbar': currentData['ebar']['color'],
                   'Line': currentData['line']['color'],
                   'FillFace': currentData['fill']['face_col'],
                   'FillEdge': currentData['fill']['edge_col'],
                   'ScatterFace': currentData['scatter']['face_col'],
                   'ScatterEdge': currentData['scatter']['edge_col']}
    styleSheet = 'background-color: rgb({}, {}, {});'.format(window.colors['MarkerEdge'][0]*255,
                                                             window.colors['MarkerEdge'][1]*255,
                                                             window.colors['MarkerEdge'][2]*255)
    window.btnMEC.setStyleSheet(styleSheet)
    styleSheet = 'background-color: rgb({}, {}, {});'.format(window.colors['MarkerFace'][0]*255,
                                                             window.colors['MarkerFace'][1]*255,
                                                             window.colors['MarkerFace'][2]*255)
    window.btnMFC.setStyleSheet(styleSheet)
    styleSheet = 'background-color: rgb({}, {}, {});'.format(window.colors['Errorbar'][0]*255,
                                                             window.colors['Errorbar'][1]*255,
                                                             window.colors['Errorbar'][2]*255)
    window.btnEBCol.setStyleSheet(styleSheet)
    styleSheet = 'background-color: rgb({}, {}, {});'.format(window.colors['Line'][0]*255,
                                                             window.colors['Line'][1]*255,
                                                             window.colors['Line'][2]*255)
    window.btnLCol.setStyleSheet(styleSheet)
    styleSheet = 'background-color: rgb({}, {}, {});'.format(window.colors['FillFace'][0]*255,
                                                             window.colors['FillFace'][1]*255,
                                                             window.colors['FillFace'][2]*255)
    window.btnFFC.setStyleSheet(styleSheet)
    styleSheet = 'background-color: rgb({}, {}, {});'.format(window.colors['FillEdge'][0]*255,
                                                             window.colors['FillEdge'][1]*255,
                                                             window.colors['FillEdge'][2]*255)
    window.btnFEC.setStyleSheet(styleSheet)
    styleSheet = 'background-color: rgb({}, {}, {});'.format(window.colors['ScatterFace'][0]*255,
                                                             window.colors['ScatterFace'][1]*255,
                                                             window.colors['ScatterFace'][2]*255)
    window.btnScatECol.setStyleSheet(styleSheet)
    styleSheet = 'background-color: rgb({}, {}, {});'.format(window.colors['ScatterEdge'][0]*255,
                                                             window.colors['ScatterEdge'][1]*255,
                                                             window.colors['ScatterEdge'][2]*255)
    window.btnScatFCol.setStyleSheet(styleSheet)
    
    window.chbEB.setChecked(currentData['ebar']['exist'])
    window.sbEBLW.setValue(currentData['ebar']['linew'])
    window.sbEBCS.setValue(currentData['ebar']['capsize'])
    window.sbEBCT.setValue(currentData['ebar']['capthick'])
    
    window.chbL.setChecked(currentData['line']['exist'])
    window.cbLS.setCurrentText(currentData['line']['style'])
    window.sbLW.setValue(currentData['line']['width'])
    window.sbLAlpha.setValue(currentData['line']['alpha'])
    
    window.chbM.setChecked(currentData['marker']['exist'])
    window.cbMT.setCurrentText(currentData['marker']['type'])
    window.sbMEW.setValue(currentData['marker']['edge_wid'])
    window.sbMS.setValue(currentData['marker']['size'])
    window.sbMEvery.setValue(currentData['marker']['markevery'])
    
    window.chbF.setChecked(currentData['fill']['exist'])       
    window.sbFA.setValue(currentData['fill']['alpha'])
    window.sbFEW.setValue(currentData['fill']['line_wid'])
    window.cbFES.setCurrentText(currentData['fill']['line_sty'])
    
    window.chbS.setChecked(0)
    window.cbSMT.setCurrentText(currentData['scatter']['type'])
    window.cbSCV.addItems(currentData['scatter']['color_vector_names']) 
    window.cbSCV.setCurrentText(currentData['scatter']['current_color'])
    window.sbScatSz.setValue(currentData['scatter']['size'])
    window.cbSSV.addItems(currentData['scatter']['size_vector_names'])
    window.cbSSV.setCurrentText(currentData['scatter']['current_size'])
    window.sbScatAlpha.setValue(currentData['scatter']['alpha'])
    window.cbScatCmap.setCurrentText(currentData['scatter']['cmap'])
    window.chbSCB.setChecked(currentData['colorbar'])
    
    window.ePlotTitle.setText(currentData['label'])
    window.eFillTitle.setText(currentData['fill-label'])


def save_plot_data(window, index, multi=False):
    currentData = window.data_dict[index]
    currentData['marker']['edge_col'] = window.colors['MarkerEdge']
    currentData['marker']['face_col'] = window.colors['MarkerFace']
    currentData['ebar']['color'] = window.colors['Errorbar']
    currentData['line']['color'] = window.colors['Line']
    currentData['fill']['face_col'] = window.colors['FillFace']
    currentData['fill']['edge_col'] = window.colors['FillEdge']
    currentData['scatter']['face_col'] = window.colors['ScatterFace']
    currentData['scatter']['edge'] = window.colors['ScatterEdge']

    
    currentData['ebar']['exist'] = window.chbEB.isChecked()
    currentData['ebar']['linew'] = window.sbEBLW.value()
    currentData['ebar']['capsize'] = window.sbEBCS.value()
    currentData['ebar']['capthick'] = window.sbEBCT.value()
    
    currentData['line']['exist'] = window.chbL.isChecked()
    currentData['line']['style'] = window.cbLS.currentText()
    currentData['line']['width'] = window.sbLW.value()
    currentData['line']['alpha'] = window.sbLAlpha.value()
    
    currentData['marker']['exist'] = window.chbM.isChecked()
    currentData['marker']['type'] = window.cbMT.currentText()
    currentData['marker']['edge_wid'] = window.sbMEW.value()
    currentData['marker']['size'] = window.sbMS.value()
    currentData['marker']['markevery'] = window.sbMEvery.value()
    
    currentData['fill']['exist'] = window.chbF.isChecked()       
    currentData['fill']['alpha'] = window.sbFA.value()
    currentData['fill']['line_wid'] = window.sbFEW.value()
    currentData['fill']['line_sty'] = window.cbFES.currentText()
    
    currentData['scatter']['exist'] = window.chbS.isChecked()
    currentData['scatter']['type'] = window.cbSMT.currentText()
    currentData['scatter']['current_color'] = window.cbSCV.currentText()    
    currentData['scatter']['size'] = window.sbScatSz.value()
    currentData['scatter']['current_size'] = window.cbSSV.currentText()
    currentData['scatter']['alpha'] = window.sbScatAlpha.value()
    currentData['scatter']['cmap'] = window.cbScatCmap.currentText()
    currentData['colorbar'] = window.chbSCB.isChecked()
    
    if not multi:
        currentData['label'] = window.ePlotTitle.text()
        currentData['fill-label'] = window.eFillTitle.text()
        
        
def save_axis_data(window, index):
    window.axis_dict[index]['plots'] = []
    for i in range(window.cbSelData.count()):
        window.axis_dict[index]['plots'].append(window.cbSelData.itemText(i))

    window.axis_dict[index]['position'][0] = window.sbAxisRow.value()
    window.axis_dict[index]['position'][1] = window.sbAxisCol.value()
    window.axis_dict[index]['position'][2] = window.sbAxisRowSpan.value()
    window.axis_dict[index]['position'][3] = window.sbAxisColSpan.value()

    window.axis_dict[index]['x_label'] = window.eXAxLab.text()
    window.axis_dict[index]['y_label'] = window.eYAxLab.text()

    window.axis_dict[index]['axis_text']['size'] = window.sbAxFontSize.value()

    window.axis_dict[index]['x_lim'][0] = float(window.eXAxisLow.text())
    window.axis_dict[index]['x_lim'][1] = float(window.eXAxisHigh.text())
    window.axis_dict[index]['y_lim'][0] = float(window.eYAxisLow.text())
    window.axis_dict[index]['y_lim'][1] = float(window.eYAxisHigh.text())
    window.axis_dict[index]['xticks'] = window.chbXTick.isChecked()
    window.axis_dict[index]['yticks'] = window.chbYTick.isChecked()
    window.axis_dict[index]['xscale'] = window.chbXScale.isChecked()
    window.axis_dict[index]['yscale'] = window.chbYScale.isChecked()

    window.axis_dict[index]['axis_text']['Bold'] = window.chbAxFontBold.isChecked()
    window.axis_dict[index]['axis_text']['Italic'] = window.chbAxFontItal.isChecked()

    window.axis_dict[index]['title'] = window.ePltTitle.text()
    window.axis_dict[index]['title_text']['size'] = window.sbTFontSize.value()
    window.axis_dict[index]['title_text']['Bold'] = window.chbTBold.isChecked()
    window.axis_dict[index]['title_text']['Italic'] = window.chbTItal.isChecked()

    window.axis_dict[index]['legend'] = window.cbLegPos.currentText()
    window.axis_dict[index]['legendFontSize'] = window.sbLegFontSize.value()
    
def set_axis_data(window, index):
    window.selected_axis_value = index
    window.cbSelData.clear()
    window.cbSelData.addItems(window.axis_dict[index]['plots'])

    window.cbAxisList.setCurrentText(index)

    window.sbAxisRow.setValue(window.axis_dict[index]['position'][0])
    window.sbAxisCol.setValue(window.axis_dict[index]['position'][1])
    window.sbAxisRowSpan.setValue(window.axis_dict[index]['position'][2])
    window.sbAxisColSpan.setValue(window.axis_dict[index]['position'][3])

    window.eXAxLab.setText(window.axis_dict[index]['x_label'])
    window.eYAxLab.setText(window.axis_dict[index]['y_label'])

    window.sbAxFontSize.setValue(window.axis_dict[index]['axis_text']['size'])

    window.eXAxisLow.setText(str(window.axis_dict[index]['x_lim'][0]))
    window.eXAxisHigh.setText(str(window.axis_dict[index]['x_lim'][1]))
    window.eYAxisLow.setText(str(window.axis_dict[index]['y_lim'][0]))
    window.eYAxisHigh.setText(str(window.axis_dict[index]['y_lim'][1]))
    window.chbXTick.setChecked(window.axis_dict[index]['xticks'])
    window.chbYTick.setChecked(window.axis_dict[index]['yticks'])
    window.chbXScale.setChecked(window.axis_dict[index]['xscale'])
    window.chbYScale.setChecked(window.axis_dict[index]['yscale'])

    window.chbAxFontBold.setChecked(window.axis_dict[index]['axis_text']['Bold'])
    window.chbAxFontItal.setChecked(window.axis_dict[index]['axis_text']['Italic'])

    window.ePltTitle.setText(window.axis_dict[index]['title'])
    window.sbTFontSize.setValue(window.axis_dict[index]['title_text']['size'])
    window.chbTBold.setChecked(window.axis_dict[index]['title_text']['Bold'])
    window.chbTItal.setChecked(window.axis_dict[index]['title_text']['Italic'])

    window.cbLegPos.setCurrentText(window.axis_dict[window.selected_axis_value]['legend'])
    window.sbLegFontSize.setValue(window.axis_dict[window.selected_axis_value]['legendFontSize'])


def add_first_axis(window):
    window.axis_dict['axis1'] = {'plots':[],
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
                               'legend':'lower right',
                               'legendFontSize':12,
                               'xticks': 1, 'yticks':1,
                               'xscale':0, 'yscale':0}
    max_x = -1e16
    min_x = 1e16
    max_y = -1e16
    min_y = 1e16
    
    for i in window.data_dict.keys():
        window.axis_dict['axis1']['plots_data'].append(window.data_dict[i])
        window.axis_dict['axis1']['plots'].append(i)
        if max(window.data_dict[i]['x']) > max_x:
            max_x = max(window.data_dict[i]['x'])
        if max(window.data_dict[i]['y']) > max_y:
            max_y = max(window.data_dict[i]['y'])
        if min(window.data_dict[i]['x']) < min_x:
            min_x = min(window.data_dict[i]['x'])
        if min(window.data_dict[i]['y']) < min_y:
            min_y = min(window.data_dict[i]['y'])
    window.axis_dict['axis1']['x_lim'] = [min_x, max_x]
    window.axis_dict['axis1']['y_lim'] = [min_y, max_y]
    window.cbAxisList.clear()
    window.cbAxisList.addItems(list(window.axis_dict.keys()))

def add_new_axis(window):
    window.axis_dict['axis{}'.format(window.axis_count+1)] = {
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
    window.cbAxisList.addItem('axis{}'.format(window.axis_count+1))
    window.cbAxisList.setCurrentIndex(window.cbAxisList.count()-1)
    window.axis_count += 1

def del_curr_axis(window):
    if window.cbAxisList.currentText() == 'axis1':
        QtWidgets.QMessageBox.warning(window, "Delete Axis", "Axis 1 cannot be deleted!")
        return
    temp_axis_dict = {}
    for i in range(window.cbAxisList.count()):
        if window.cbAxisList.itemText(i) != window.cbAxisList.currentText():
            temp_axis_dict[window.cbAxisList.itemText(i)] = window.axis_dict[window.cbAxisList.itemText(i)]
    window.axis_dict = temp_axis_dict
    window.cbAxisList.clear()
    window.cbAxisList.addItems(list(window.axis_dict.keys()))
    window.selected_axis_value = list(window.axis_dict.keys())[0]
    set_axis_data(window, list(window.axis_dict.keys())[0])
    
    
def add_plot_to_axis(window):
    plot_name = window.cbAllData.currentText()
    if plot_name not in window.axis_dict[window.selected_axis_value]['plots']:
        if window.axis_dict[window.selected_axis_value]['plots'][0] == '':
            window.cbSelData.clear()
            window.axis_dict[window.selected_axis_value]['plots'] = []
            window.axis_dict[window.selected_axis_value]['plots_data'] = []
            max_x = -1e16
            min_x = 1e16
            max_y = -1e16
            min_y = 1e16
        else:
            max_x = window.axis_dict[window.selected_axis_value]['x_lim'][1]
            min_x = window.axis_dict[window.selected_axis_value]['x_lim'][0]
            max_y = window.axis_dict[window.selected_axis_value]['y_lim'][1]
            min_y = window.axis_dict[window.selected_axis_value]['y_lim'][0]
        window.axis_dict[window.selected_axis_value]['plots'].append(plot_name)
        window.axis_dict[window.selected_axis_value]['plots_data'].append(window.data_dict[plot_name])

        if np.max(window.data_dict[plot_name]['x']) > max_x:
            max_x = np.max(window.data_dict[plot_name]['x'])
        if np.max(window.data_dict[plot_name]['y']) > max_y:
            max_y = np.max(window.data_dict[plot_name]['y'])
        if np.min(window.data_dict[plot_name]['x']) < min_x:
            min_x = np.min(window.data_dict[plot_name]['x'])
        if np.min(window.data_dict[plot_name]['y']) < min_y:
            min_y = np.min(window.data_dict[plot_name]['y'])
        window.axis_dict[window.selected_axis_value]['x_lim'] = [min_x, max_x]
        window.axis_dict[window.selected_axis_value]['y_lim'] = [min_y, max_y]


        window.eXAxisLow.setText(str(min_x))
        window.eXAxisHigh.setText(str(max_x))
        window.eYAxisLow.setText(str(min_y))
        window.eYAxisHigh.setText(str(max_y))

        window.cbSelData.addItem(plot_name)
        window.cbSelData.setCurrentIndex(window.cbSelData.count()-1)


def remove_plot_from_axis(window):
    plot_name = window.cbSelData.currentText()
    temp_plots = []
    temp_plots_data = []
    window.cbSelData.clear()
    max_x = -1e16
    min_x = 1e16
    max_y = -1e16
    min_y = 1e16

    for i in range(len(window.axis_dict[window.selected_axis_value]['plots'])):
        if window.axis_dict[window.selected_axis_value]['plots'][i] != plot_name:
            plot_name_temp = window.axis_dict[window.selected_axis_value]['plots'][i]
            temp_plots.append(window.axis_dict[window.selected_axis_value]['plots'][i])
            temp_plots_data.append(window.data_dict[window.axis_dict[window.selected_axis_value]['plots'][i]])
            if np.max(window.data_dict[plot_name_temp]['x']) > max_x:
                max_x = np.max(window.data_dict[plot_name_temp]['x'])
            if np.max(window.data_dict[plot_name_temp]['y']) > max_y:
                max_y = np.max(window.data_dict[plot_name_temp]['y'])
            if np.min(window.data_dict[plot_name_temp]['x']) < min_x:
                min_x = np.min(window.data_dict[plot_name_temp]['x'])
            if np.min(window.data_dict[plot_name_temp]['y']) < min_y:
                min_y = np.min(window.data_dict[plot_name_temp]['y'])

    if temp_plots == []:
        window.axis_dict[window.selected_axis_value]['plots'] = ['']
        window.axis_dict[window.selected_axis_value]['plots_data'] = ['']
        max_x = 1
        min_x = 0
        max_y = 1
        min_y = 0
    else:
        window.axis_dict[window.selected_axis_value]['plots'] = temp_plots
        window.axis_dict[window.selected_axis_value]['plots_data'] = temp_plots_data

    window.axis_dict[window.selected_axis_value]['x_lim'] = [min_x, max_x]
    window.axis_dict[window.selected_axis_value]['y_lim'] = [min_y, max_y]

    window.eXAxisLow.setText(str(min_x))
    window.eXAxisHigh.setText(str(max_x))
    window.eYAxisLow.setText(str(min_y))
    window.eYAxisHigh.setText(str(max_y))

    window.cbSelData.addItems(window.axis_dict[window.selected_axis_value]['plots'])
    window.cbSelData.setCurrentIndex(0)
    
    
    
    
    
    

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
        line_col = [(0,0,0), (0,0,1), (0,1,0), (1,0,0), (1,0,1),
                    (1,1,0), (0,1,1), (0.25,0.75,1), (0.75,0.25,1), (1,0.75,0.25)]
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
                           'alpha':0.5,
                           'face_col':line_col[col_count],
                           'edge_col':line_col[col_count],
                           'size':10},
                'colorbar':1}
            col_count += 1
            if col_count == 10:
                col_count = 0
        # self.root = tk.Tk()
        # self.root.title('Matplotlib Post Processor')
        # icon_file_dir = __file__.replace('pltEditorTool.py', 'icon2.png')
        # self.root.iconphoto(False, tk.PhotoImage(file=icon_file_dir))
        # self.root.resizable(0, 0)
        # self.root.protocol("WM_DELETE_WINDOW", self.callback)
        # app = window(plot_data_Dict, master=self.root)
        # if PLATFORM != "Darwin":
        #     app['bg'] = BG_BLUE
        # app.mainloop()
        #run the proper program
        QtWidgets.QApplication.setStyle("fusion")
        app2 = QtWidgets.QApplication(argv)
        myWindow = MyWindowClass(None, plot_data_Dict)
        myWindow.show()
        app2.exec_()    

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

    # def callback(self):
    #     if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
    #         plt.close(1)
    #         self.root.destroy()

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
    
    # x_data = np.array(data.loc[:,'x.1'])
    # y_data = np.array(data.loc[:,'y.1'])
    # x_err_data = np.array(data.loc[:,'x_err.1'])
    # y_err_data = np.array(data.loc[:,'y_err.1'])
    # fill_data = np.array(data.loc[:,'fill.1'])
    # fill_alt_data = np.array(data.loc[:,'fill_alt.1'])
    # labels_data = 'Computation'
    
    # print("Case 2: Single Numpy Array Input")
    # plotEditor(x=x_data, y=y_data, x_err=x_err_data, y_err=y_err_data, 
    #             fill=fill_data, fill_alt=fill_alt_data)
    
    # x_data = np.array([np.array(data.loc[:,'x']), np.array(data.loc[:,'x.1'])]).transpose()
    # y_data = np.array([np.array(data.loc[:,'y']), np.array(data.loc[:,'y.1'])]).transpose()
    # x_err_data = np.array([np.array(data.loc[:,'x_err']), np.array(data.loc[:,'x_err.1'])]).transpose()
    # y_err_data = np.array([np.array(data.loc[:,'y_err']), np.array(data.loc[:,'y_err.1'])]).transpose()
    # fill_data = np.array([np.array(data.loc[:,'fill']), np.array(data.loc[:,'fill.1'])]).transpose()
    # fill_alt_data = np.array([np.array(data.loc[:,'fill_alt']), np.array(data.loc[:,'fill_alt.1'])]).transpose()
    # labels_data = ['Experimental', 'Computation']
    
    # print("Case 3: 2D Numpy Array Input")
    # plotEditor(x=x_data, y=y_data, x_err=x_err_data, y_err=y_err_data, 
    #             fill=fill_data, fill_alt=fill_alt_data)
    
    # input_data = np.zeros((2,101,6))
    # input_data[0,:,0] = x_data[:,0]
    # input_data[1,:,0] = x_data[:,1]
    # input_data[0,:,1] = y_data[:,0]
    # input_data[1,:,1] = y_data[:,1]
    # input_data[0,:,2] = x_err_data[:,0]
    # input_data[1,:,2] = x_err_data[:,1]
    # input_data[0,:,3] = y_err_data[:,0]
    # input_data[1,:,3] = y_err_data[:,1]
    # input_data[0,:,4] = fill_data[:,0]
    # input_data[1,:,4] = fill_data[:,1]
    # input_data[0,:,5] = fill_alt_data[:,0]
    # input_data[1,:,5] = fill_alt_data[:,1]
    # print("Case 4: 3D Numpy Array Input")
    # plotEditor(x=input_data)
    
    # print("Case 5: Pandas DataFrame Input")
    # plotEditor(x=data)



