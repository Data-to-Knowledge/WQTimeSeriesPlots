# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 16:52:10 2019

@author: TinaB
"""
### This script creates a contour (3D) plot of lake temperature at different depth over time

#import csv
import pandas as pd
import plotly
import plotly.graph_objs as go

# set path for data to be imported
datapath_in = 'C:\\data\\loggers\\'

########### Lake Pearson
## import csv
df = pd.read_csv(datapath_in+"pearson_mod_all.csv")
print df

loggerdata = df.drop(df.columns[0], axis = 1) # drop first column (date & time)
print loggerdata

### plotly example for data object
#data = [
#    go.Contour(
#        z=[[10, 10.625, 12.5, 15.625, 20],
#           [5.625, 6.25, 8.125, 11.25, 15.625],
#           [2.5, 3.125, 5., 8.125, 12.5],
#           [0.625, 1.25, 3.125, 6.25, 10.625],
#           [0, 0.625, 2.5, 5.625, 10]],
#        x=[-9, -6, -5 , -3, -1],
#        y=[0, 1, 4, 5, 7]
#    )]
#
#plotly.offline.plot(data)
#py.iplot(data)

z1 = loggerdata.to_numpy() #turn temperature data into a numpy array 
z = z1.transpose()  #transpose this array
y1 = df.Time.to_numpy() #turn time data into a numpy array 
x = [14.5, 11.5, 8.5, 6, 3.5, 1] #Logger positions (depth)
print 'building object'
#data2 = [(go.Contour(z=z1,x=x,y=y1,))] # standard plot
data2 = [(go.Contour(z=z,x=y1,y=x,
                     autocontour=False,contours=dict(start=12,end=21,size=1) # this sets contours from 12 to 21 degress at spacing of 1 degree
                ))]
print 'plotting'
plotly.offline.plot(data2, filename='contour_PS_all_depth')
print 'finished plotting'

########## Grasmere
df2 = pd.read_csv(datapath_in+"grasmere.csv")
print df2

loggerdata2 = df2.drop(df2.columns[0], axis = 1)
print loggerdata2

z2 = loggerdata2.to_numpy()
zG = z2.transpose()
yG = df2.Time.to_numpy()
xG = [11.2, 9.7, 7.7, 5.7, 3.7, 1.7]
print x
print 'building object'
#data2 = [(go.Contour(z=z1,x=x,y=y1,))]
data3 = [(go.Contour(z=zG,x=yG,y=xG,
                     autocontour=False,contours=dict(start=12,end=21,size=0.5)
#            contours=dict(
#            coloring ='heatmap',
#            showlabels = True,
#            labelfont = dict(
#                family = 'Raleway',
#                size = 12,
#                color = 'white',))
                ))]
print 'plotting'
plotly.offline.plot(data3, filename='contour_GM_all_depth')
print 'finished plotting'

