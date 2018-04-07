# -*- coding: utf-8 -*-
"""
GCorless
4-7-2018
Simple DatFile Extraction and Plotting Script
"""
from matplotlib import pyplot as plt
import numpy as np
import os


#point to datafile
directory_in_str = r"C:\Users\name\Documents\Data_Folder\Data"

directory = os.fsencode(directory_in_str)

#the headers.csv provide the x values for our plots
dir_Headers = r"C:\Users\name\Documents\Data_Headers\Headers.csv"


headers = np.genfromtxt(dir_Headers,delimiter=",")

#get the distribution
x_headers = headers[:,0]
avg_list = []
list_titles = []
blnFirst = True

for file in os.listdir(directory):
     
     filename = os.fsdecode(file)
     if filename.endswith(".csv"):
         raw_data = np.genfromtxt(directory_in_str + "/" + filename,delimiter=",")
         raw_data = raw_data.transpose()
         
         raw_data_average = np.mean(raw_data, axis=1)
         
         if blnFirst == True:
             avg_list = raw_data_average
             list_titles.append(filename)
             blnFirst = False
         else:
             avg_list = np.vstack([avg_list, raw_data_average])
             list_titles.append(filename)
         #raw_DF = pd.DataFrame(raw_data)
     else:
         continue
     
#keep average separate so we can plot it thicker to stand out
avg_of_avg = np.mean(avg_list, axis=0)
std_of_avg = np.std(avg_list, axis=0)

print (list_titles)

#plot all of the separate data rows on the same graph
for row in avg_list:
    plt.plot(x_headers, row)

#add in the average separately to be distinguished
plt.plot(x_headers, avg_of_avg,color='black',linewidth=3)
plt.show()

#stdev shaded graph
plt.figure()
plt.plot(x_headers, avg_of_avg)
plt.fill_between(x_headers, avg_of_avg + std_of_avg, avg_of_avg - std_of_avg,alpha=0.4)

#to save the data file if necessary
#np.savetxt(directory_in_str + "/test.csv", avg_list, delimiter=",")