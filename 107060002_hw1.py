import csv

cwb_filename = '107060002.csv'
data = []
new_data = []
header = []
ID = ["C0A880", "C0F9A0", "C0G640", "C0R190", "C0X260"]
ID_sorted = sorted(ID)
result_list = []

with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)

# remove invalid data (copy valid data to new list)
for i in range(len(data)):
    if data[i]['HUMD'] != '-99.000' and data[i]['HUMD'] != '-999.000':
        new_data.append(data[i])

# check if there exist invalid data
for i in range(len(new_data)):
    if new_data[i]['HUMD'] == '-99.000' or new_data[i]['HUMD'] == '-999.000':
        print("wrong!, i: {}".format(i))

# find out summation, collect and print data
Sum = 0

for i, name in enumerate(ID_sorted):
    Data = []
    for j in range(len(new_data)):
        if new_data[j]['station_id'] == name:
            Sum += float(new_data[j]['HUMD'])
    if Sum == 0:
        Data.append(name)
        Data.append('None')
    else:
        Data.append(name)
        Data.append(Sum)
    Sum = 0
    result_list.append(Data)

print(result_list)