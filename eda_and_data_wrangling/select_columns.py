import csv

with open('sample2.csv', 'rb') as rfile:
	dialect = csv.Sniffer().sniff(rfile.read(500))
	reader = csv.reader(rfile, dialect)
	with open('selected_columns_sample.csv', 'wb') as wfile:
		writer = csv.writer(wfile)
		for row in reader:
			columns = []
			index = [1, 429, 501, 541, 546]
			for i in index:
				columns.append(row[i])
			writer.writerow(columns)
			

