import csv
txt = open('dataset.csv').readlines()
results = open('json.txt','w')
reader = csv.reader(txt)
json_data = []
reader.next()
headers = reader.next()
#print(headers)
for row in reader:
    d = dict(zip(headers,row))
    json_data.append(d)
#print(json_data)
results.write(str(json_data))
print(type(results))
results.close()
