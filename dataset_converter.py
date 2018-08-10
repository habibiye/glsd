import csv
txt = open('dataset.csv').readlines()
results = open('json.txt','w')
reader = csv.reader(txt)
json_data = []
#reader.__next__()
headers = reader.__next__()
print(headers)
for row in reader:
    d = dict(zip(headers,row))
    json_data.append(d)
print(len(json_data))
for entry in json_data:
	for key, value in entry.items():
		if key == 'recordNumber' or key == 'channel':
			entry[key] = int(value)
<<<<<<< HEAD
		elif key == 'latitude' or key == 'longitude':
=======
		elif key == 'latitude' or key == 'longitude' or key == 'frequency' or key == 'maxERP' or key == 'antennaHeight_AGL':
>>>>>>> 671c7c08c3a09d855b5cb776da0e00bfab04cc23
			entry[key] = ((float(value) * 1e4)//1)/1.e4
		elif key == 'frequency' or key == 'maxERP' or key == 'antennaHeight_AGL':
			entry[key] = float(value)
		elif key == 'siteName':
			entry[key] = value.replace('(','').replace(')',"").replace('/',"").replace(' ',"")
json_data = str(json_data)
json_data = json_data.replace("'",'"')
results.write(json_data)
print(type(results))
results.close()
