# -*- coding: utf-8 -*-
"""
Project: XXXX
Title: Resize recursive parent folder
Author: Malcolm McCabe
Created: 2/7/2022
Last Updated: 2/11/2022
"""

import pandas as pd

"""
Presteps
1. Add Count_slash column: counts occurences of "/" in FullPath
2. Order by:
    Count_slash ascending
    FullPath A-Z
"""

#Import CSV
df = pd.read_csv("XXXX.csv")

#Keep only necessary columns and create a list
path_size = df[['Full Path', 'Slash count']].to_numpy().tolist()

# Path list
path_list = []
for path in path_size:
    path_list.append(path[0])
    
path_list_2 = path_list.copy()
print(len(path_list_2))



# Create empty lists - to be used to append final sizes
final_list_path = []


#print(path_list)
for i in reversed(path_list):
    print(i)
    up_one_path = i.rsplit('/', 1)[0]
   # print(i)
    #print(up_one_path)
    if up_one_path in path_list_2:
        final_list_path.append(i)
    


df_final = pd.DataFrame(final_list_path)
df_final.to_csv("output.csv")