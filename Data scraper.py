# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 20:23:05 2020

@author: abhij
"""
from pandas import DataFrame
import matplotlib.pyplot as plt


# Function to scrape the data

def scrape(): 
    
    file = open(r"C:\Users\abhij\Desktop\Projects\SEDS BPHC\Avionics\lOG.txt", "r") #put your filepath here
    file_1 = file.readlines()
    
    raw_data = []
    processed_data = []
    a_data = []
    x_data = []
    y_data = []
    t_data = []
    
    
    
    for line in file_1:
        if line != '*** TAKEOFF ***\n' and line != '** Going Down **\n' and line != "\n":
            raw_data.append(line)
    #put all the lines which aren't useless into a list of strings
    
    for datapoint in raw_data:
        
        
        Altitude = ''
        Orientation_x = ''
        Orientation_y = ''
        Time = ''
        
        
        
        
        for char in range(0,len(datapoint)):
            if datapoint[char] == ":":
                x = char + 2
                while datapoint[x] != "m":
                    Altitude = Altitude + datapoint[x]
                    x += 1
                    
            if datapoint[char] == "X":
                x = char + 2
                while datapoint[x] != ",":
                    Orientation_x = Orientation_x + datapoint[x]
                    x += 1
            
            if datapoint[char] == "Y":
                x = char + 2
                while datapoint[x] != ")":
                    Orientation_y = Orientation_y + datapoint[x]
                    x += 1
            
            if datapoint[char] == "+":
                x = char + 1
                while datapoint[x] != "s":
                    Time = Time + datapoint[x]
                    x += 1
            
        
        a_data.append(Altitude)
        x_data.append(Orientation_x)
        y_data.append(Orientation_y)
        t_data.append(Time)
        
        
    processed_data.append(a_data)
    processed_data.append(x_data)
    processed_data.append(y_data)
    processed_data.append(t_data)
    
    return(processed_data)

#Function to plot the Time Vs. Altitude Graph
    
def plot_height(Altitude, Time):
    
    
    for x in range(0,len(Altitude)):
        Altitude[x] = float(Altitude[x])
        Time[x] = float(Time[x])
    
    
    
    max_height = 0
    i = 0
    for x in range(0,len(Altitude)):
        if Altitude[x] > max_height:
            max_height = Altitude[x]
            i = x
            
    plt.scatter(Time[i],Altitude[i],s = 300 , c= "red", marker = "2")  
    
    plt.plot(Time, Altitude)
    
    
    
    
    
    
        
        
    
    
#main function
          
def main():
    
    data = scrape()
    pan_data = {'Altitude':      data[0], 
                'Orientation X': data[1],
                'Orientation Y': data[2],
                'Time':          data[3]}
    
    df = DataFrame(pan_data, columns = ['Altitude', 'Orientation X', 'Orientation Y', 'Time'])
    
    export_excel = df.to_excel (r'C:\Users\abhij\Desktop\Projects\SEDS BPHC\Avionics\export_dataframe.xlsx', index = None, header=True)
    #put where you want your excel file to go here
    
    plot_height(data[0], data[3])
    
    
            
main()