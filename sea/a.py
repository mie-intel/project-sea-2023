import json

f = open('movies/movies.json')

data = json.load(f);

for i in range(len(data)):
	data[i]["seats"] = list();
	for j in range(1, 65):
		data[i]["seats"].append(0);

for i in data:
	for j in i:
		print(j);
	print();

with open("movies2.json", "w") as outfile:
	json.dump(data, outfile)
