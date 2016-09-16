import csv

c = 0
with open('avg_scores_by_country_complete4.csv', 'rb') as rfile:
	#dialect = csv.Sniffer().sniff(rfile.read(50))
	reader = csv.reader(rfile)
	with open('median_scores_by_country_complete.csv', 'wb') as wfile:
		writer = csv.writer(wfile)
		for row in reader:
			if row[1] == "Chinese Taipei":
				row[1] = "China"
			if row[1] == "United Kingdom":
				row[1] = "England"
			if row[1] == "Russian Federation":
				row[1] = "Russia"
			if row[1] == "Slovak Republic":
				row[1] = "Slovakia"
			if row[1] == "Korea":
				row[1] = "South Korea"
			if row[1] == "United States of America":
				row[1] = "USA"
			writer.writerow(row)


