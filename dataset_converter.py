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
		elif key == 'latitude' or key == 'longitude' or key == 'frequency' or key == 'maxERP' or key == 'antennaHeight_AGL':
			entry[key] = float(value)
results.write(str(json_data))
print(type(results))
results.close()
