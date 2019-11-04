# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 11:11:27 2019

@author: Zachary
"""
#The idea is to be able to run smote on all our data yet smote only 
# each type of protein using only data from its type
# This will require we add the class (type ) of protein as another column
#for identification 

import pandas as pd
import numpy as np
import random

basefile = pd.read_csv(r'72featNoLabels.csv')
output = []
for i in range(1,8795):
    pt1 = basefile.iloc[i-1:i,:]
    pt1 = np.array(pt1).flatten()
    for j in range(i,8795):
        smoteOut = []
        if i != j & basefile.iloc[i,73] == basefile.iloc[j,73]
            pt2 = basefile.iloc[j-1:j,:]
            pt2 = np.array(pt2).flatten()
            for k in range(0,len(pt2)-1):
                pt1k = round(pt1[k] * 100000)
                pt2k = round(pt2[k] * 100000)
                if pt1k > pt2k:
                    rand = random.randrange(pt2k,pt1k)
                elif pt1k < pt2k:
                    rand = random.randrange(pt1k,pt2k)
                else:
                    rand = pt1k
                rand = rand / 100000
                smoteOut.append(rand)
            smoutOut.append(basefile.iloc[j,73]) #Adds protein's type name to last column of 'smotted' values 
                
            output.append(smoteOut)
            
print(output)

f = open("smittenData.txt", 'w+')
for sublist in output:
    for value in sublist:
        f.write(str(value) + ' ')
    f.write('\n')

f.close()
