import pandas
import csv
import math

with open("data.csv", newline = "") as f:
  reader = csv.reader(f)
  fileData = list(reader)

totalData = 0
totalAmount = len(fileData)
dataList = []

for data in fileData:
  totalData += float(data[0]) + float(data[1]) + float(data[2]) + float(data[3]) + float(data[4]) + float(data[5]) + float(data[6]) + float(data[7]) + float(data[8]) + float(data[9])
  dataList.append(data[0]) 
  dataList.append(data[1]) 
  dataList.append(data[2]) 
  dataList.append(data[3]) 
  dataList.append(data[4]) 
  dataList.append(data[5]) 
  dataList.append(data[6]) 
  dataList.append(data[7]) 
  dataList.append(data[8]) 
  dataList.append(data[9]) 

mean = totalData/totalAmount
squaredList = []

for x in dataList:
  num = int(x) - mean
  num = num ** 2
  squaredList.append(num)

sum = 0

for i in squaredList:
  sum = sum + i

result = sum/totalAmount
standardDivision = math.sqrt(result)

print(standardDivision)