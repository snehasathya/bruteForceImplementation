import pandas as pd
import statistics as std
from datetime import datetime


store_data = pd.read_csv('store_data.csv', header=None)

store_data.head()

store_data

store_data.shape
records = []
for i in range(0, 50):
    records.append([str(store_data.values[i,j]) for j in range(0, 20)])

#Extraction of unique values from records
listNew = []
for line in records:    
    for word in line:
        listNew.append(word)
        
items = list(dict.fromkeys(listNew))
items.remove('nan')
    
    
start_time = datetime.now()

first_list = []

for i in range(0, len(items)):
    for j in range(i+1, len(items)):
        first_list.append(items[i] + ',' + items[j])

              
second_list_temp = []
second_list = []
for i in range(0, len(first_list)):
    for j in range(0, len(records)):
        str1 = str(first_list[i])
        if ('nan' in records[j]):
            records[j].remove('nan')
        str2 = str(',').join(map(str, records[j]))
    
       
        if str1 not in str2:
            continue
        else:
            if (first_list[i] not in second_list):
                second_list.append(first_list[i])
                    
third_List = []

for i in range(0, len(second_list)):
    for j in range(i+1, len(second_list)):
        str1 = str(second_list[i])
        str2 = str(second_list[j])
                
        strnew1 = str1.split(",")
        strnew2 = str2.split(",")
        
        if (strnew1[0] not in strnew2[0] and strnew1[1] not in strnew2[1] 
            and strnew1[1] not in strnew2[1] and strnew1[1] not in strnew2[0]):
             third_List.append(strnew1[0] + ',' + strnew1[1] + ',' + strnew2[1])   
        else:
            if (strnew1[0] in strnew2[0] or strnew1[1] in strnew2[0]):
                third_List.append(strnew1[0] + ',' + strnew1[1] + ',' + strnew2[1])   
            else:
                third_List.append(strnew1[0] + ',' + strnew1[1] + ',' + strnew2[0])
       
        
            
fourth_list_temp = []
fourth_list_temp2 =[]
fourth_list = []

for i in range(0, len(third_List)):
    for j in range(0, len(records)):
        str1 = str(third_List[i])
        if ('nan' in records[j]):
            records[j].remove('nan')
        str2 = str(',').join(map(str, records[j]))
    
        if str1 not in str2:
            continue
        else:
            if (third_List[i] not in fourth_list_temp):
                fourth_list_temp.append(third_List[i])
            else:
                fourth_list.append(third_List[i])
                    


fifth_list = []

for i in range(0, len(fourth_list)):
    for j in range(i+1, len(fourth_list)):
        str1 = str(fourth_list[i])
        str2 = str(fourth_list[j])
        
        strnew1 = str1.split(",")
        strnew2 = str2.split(",")
        
        newList = []
        
        for k in range(0, len(strnew1)):
            newList.append(strnew1[k])
        for h in range(0, len(strnew2)):
            newList.append(strnew2[h])
        
        
        newList = list(dict.fromkeys(newList))
      
        if (newList not in fifth_list):
            fifth_list.append(newList)

print("Fifth is", fifth_list)
sixth_list_temp = []
sixth_list = []

for i in range(0, len(fifth_list)):
    for j in range(0, len(records)):
        str1 = str(',').join(map(str, fifth_list[i]))
        str2 = str(',').join(map(str, records[j]))
        
    
        if str1 not in str2:
            continue
        else:
            if (fifth_list[i] not in sixth_list_temp):
                sixth_list_temp.append(fifth_list[i])
            else:
                if (fifth_list[i] not in sixth_list):
                    sixth_list.append(fifth_list[i])
        
print("Sixth", sixth_list)

elapsed_time = datetime.now() - start_time
print("Time taken ", elapsed_time)


       




