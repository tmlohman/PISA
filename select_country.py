import csv

datafile = "selected_columns_complete.csv"
savefile = "USA_data.csv"
country = "United States of America"

with open(datafile, 'rb') as rfile:
	reader = csv.reader(rfile)
	with open(savefile, 'wb') as wfile:
		writer = csv.writer(wfile)
		for row in reader:
			if row[0] == "country" or row[0] == country:
				writer.writerow(row)
			else: 
				continue
				

