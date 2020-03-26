#!/usr/bin/env python

import csv
complaints = []
with open("complaints.csv") as csvfile:
    csv_reader = csv.reader(csvfile)  
    complaints_header = next(csv_reader) 
    for row in csv_reader:  
        complaints.append(row)


#Select the useful information from the original dataset.
def subset(list):
    if len(list)==0:
        return list
    data = []
    for i in range(len(list)):
        temp = []
         #year
        temp.append(int(float(list[i][0][0:4])))
         #product
        temp.append(list[i][1])
         #company
        temp.append(list[i][7])
        data.append(temp)
    data=sorted(data,key=lambda x:(x[0],x[1]))
    return data

#Select the year and product name from the list
def find_year_and_product(list):
    if len(list)==0:
        return list
    output = []
    seen_year = []
    seen_product = []
    for i in range(len(list)):
        temp = []
        if list[i][0] in seen_year and list[i][1] in seen_product:
            continue
        seen_year.append(list[i][0])
        seen_product.append(list[i][1])
        temp.append(list[i][1])
        temp.append(list[i][0])
        output.append(temp)
    return output

def match(list_output,list_data):
    for i in range(len(list_output)):
        count_complaints = 0
        seen_company = []
        dict = {}
        for j in range(len(list_data)):
            if list_output[i][0] == list_data[j][1] and list_output[i][1] == list_data[j][0]:
                count_complaints += 1
                if list_data[j][2] not in seen_company:
                    seen_company.append(list_data[j][2])
                if list_data[j][2] not in dict:
                    dict[list_data[j][2]] = 0
                if list_data[j][2] in dict:
                    dict[list_data[j][2]] += 1
        maximum = max(dict.values())
        #temp = maximum/count_complaints*100
        list_output[i].append(count_complaints)
        list_output[i].append(len(seen_company))
        list_output[i].append(round(maximum/count_complaints*100))
    return list_output

#Main Function
def consumer_complaints(list):
        data = subset(complaints)
        output = find_year_and_product(data)
        output_final = match(output,data)
        for i in range(len(output_final)):
            output_final[i][0]=output_final[i][0].replace(',','-')
        csvfile = open('output.csv', 'w',newline='')
        writer = csv.writer(csvfile,delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerows(output_final)
        csvfile.close()
        
consumer_complaints(complaints)
