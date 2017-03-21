import numpy as np
import csv
import glob
import re
import os

cwd = os.getcwd()

listofposlist =[]
labellist =[]

#takes data from files in a directory
for file in glob.glob(str(cwd)+'/PlanetsUniq/*.txt'):
    linepos = 0
    with open(file, 'r') as file2:
        filedata = file2.read()
#finds the mass data in the file
    mass = filedata.find('kg')
    massend = filedata[mass:].find('$')
    mass1 = float(filedata[mass:massend+mass].translate(None, 'kg )~=-+'))

    massorder1 = filedata.find('Mass, 10^')
    massorder2 = filedata.find('Mass (10^')
    massorder3 = filedata.find('Mass Pluto (10^')
    massorder = 0

    if massorder1 >=  0:
        massorder = float(filedata[massorder1+len('Mass, 10^'):massorder1+len('Mass, 10^')+2])
    if massorder2 >= 0:
        massorder = float(filedata[massorder2+len('Mass (10^'):massorder2+len('Mass (10^')+2])
    if massorder3 >= 0:
        massorder = float(filedata[massorder3+len('Mass Pluto (10^'):massorder3+len('Mass Pluto (10^')+2])

    mass2 = mass1*10.0**float(massorder)
    #finds the position data in the files
    pos = filedata.find('$$SOE')
    pos = filedata[pos+6: pos + filedata[pos+6:].find('\n')]
    poslist = pos.split(',')
    del poslist[0], poslist[0],poslist[-1],poslist[-1],poslist[-1]
#adds the found data to lists
    poslist.insert(0, mass2)
    listofposlist.append(poslist)
    #finds the name of the body and adds it to a list
    name = str(file)
    name = name[name.find("PlanetsUniq/")+12:name.find(".txt")]
    labellist.append(name)
#puts the data from the files into arrays before collecting the data with the correct labels into a final array
bodies = np.array(listofposlist)
labels = np.array(labellist)
bodiesfinal = np.insert(bodies, 1,labels,axis=1)
