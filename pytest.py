# -*- coding: utf-8 -*-
"""
@author: pkeppel - DSP-Exam 4
"""
"""
import section
"""
import os
import re
import pandas as pd
import numpy as np
import itertools as it
import string
import random


"""
Set Working Directory
Directory path for working python file and output saved dataframes

filename = "samplednatest.txt" contains 3 strings of random length
with characters representing randomly generate printable characters. Creation
of this txt file was performed in a seperate python script

pytest.py loads this 'corrupt' file for testing and goes through the analysis 
performed in Exam4.py
"""
SetDirectory = r"G:\My Drive\URI\Data##\Exam4"
filename = "samplednatest.txt"
os.chdir(SetDirectory)
"""
For github the directory can be changed to the following by removing comments:
url = "https://github.com/keppe026/DSP-Exam4/sampledna.txt"
directory = getcwd()
filename = directory + 'sampledna.txt'
r = requests.get(url)
"""

"""
Possible Kmers Function
"""
def poskmers():
    count=0
    var3=dict()
    for i in range(0,linecount):
        count=count+1
        var1=kmax[i]-k[i+1]+1
        var2=pow(4,k[i+1])
        var3[count]=np.minimum(var1,var2)
    return var3

"""
Observed Kmers Function
"""
def obskmers():
    split_string=[]
    unique_string=[]
    splitpoints=[]
    for i in range(0,linecount):
        string=linee[i]
        for n in range(1,len(string)+1):
            split_string.append([string[j:j+n] for j in range(0,len(string)-n+1)])
    for k in range(0,len(split_string)):
        unique_string.append(len(set(split_string[k])))
    splitpoints=list(it.accumulate(kmax))
    sublists = zip(it.chain([0], splitpoints), it.chain(splitpoints, [None]))
    split_list = list(unique_string[i:j] for i,j in sublists)
    split_list=split_list[:-1]
    return split_list

"""
Linguistic Complexity
"""
def lingcomp(possibkmers,observkmers):
    poss_sum=[np.sum(possibkmers[j]) for j in range(1,linecount+1)]
    obs_sum=np.array([np.sum(observkmers[j]) for j in range(0,linecount)])
    complexity=obs_sum/poss_sum
    return complexity

"""
Scipting for file input - flexible for files with different line numbers and 
string lengths. The script creates arrays for the k values after removing any
characters that are not A,T,C, or G
"""
kmax=[]
count=0
linee=[]
k=dict()
with open(filename,'r') as f:
    linecount=len(f.readlines())
with open(filename,'r') as f:
    for line in f:
        count=count+1
        line=re.sub('[^ATCG]','',line) # Remove all char not = ATCG
        lines=np.array([line],dtype='object')
        linee.append(lines[0]) # Store
        kmax.append(len(line)) # Create Integer list of k
        k[count]=np.linspace(1,kmax[count-1],kmax[count-1])
        
"""
Scipting to Call Functions for possible kmers, observed kmers, and complexity
"""
"""
kmax is calculated automatically above but the user can override this setting
by providing an alternative kmax array before calling the functions

kmax=[9,9,9]
for i in range(0,linecount)
    k[count]=np.linespace(1,kmax[count-1],kmax[count-1]))

"""
possibkmers=poskmers()
observkmers=obskmers()
complexity=lingcomp(possibkmers,observkmers)
"""
Create DataFrame
"""
d1={'k': k[1],'Observed kmers': observkmers[0],'Possible kmers': possibkmers[1]}
d2={'Linguistic Complexity': [complexity[0]]}
df1=pd.DataFrame(data=d1)
df2=pd.DataFrame(data=d2)
print(df1)
print(df2)

d3={'k': k[2],'Observed kmers': observkmers[1],'Possible kmers': possibkmers[2]}
d4={'Linguistic Complexity': [complexity[1]]}
df3=pd.DataFrame(data=d3)
df4=pd.DataFrame(data=d4)
print(df3)
print(df4)

d5={'k': k[3],'Observed kmers': observkmers[2],'Possible kmers': possibkmers[3]}
d6={'Linguistic Complexity': [complexity[2]]}
df5=pd.DataFrame(data=d5)
df6=pd.DataFrame(data=d6)
print(df5)
print(df6)

"""
Save Dataframes
"""
df1.to_csv('Line1-k-Observed-Possible.txt',header=True,index=False,sep='\t')
df2.to_csv('Line1-Complexity.txt',header=True,index=False,sep='\t')
df3.to_csv('Line2-k-Observed-Possible.txt',header=True,index=False,sep='\t')
df4.to_csv('Line2-Complexity.txt',header=True,index=False,sep='\t')
df5.to_csv('Line3-k-Observed-Possible.txt',header=True,index=False,sep='\t')
df6.to_csv('Line3-Complexity.txt',header=True,index=False,sep='\t')

