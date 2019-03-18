#Python script to fetch Production company metadata
import csv
import json
import sys
import re


with open('movie_ids_1995.csv', 'r', encoding='utf-8') as csvfile:
    movieIDList = []
    movie_reader = csv.reader(csvfile, delimiter=',')
    for row in movie_reader:
        movieIDList.append(row[0])
    print(movieIDList)


with open('productions_1995.csv', 'r', encoding='utf-8') as csvfile:
    companyDict = {}
    reader = csv.reader(csvfile, delimiter=',')
    next(reader, None)
    cnt = 0
    print("Started processing...")

    productions_metadata_file = open('productions_metadata.csv', 'a')
    fieldnames = ['companyID', 'companyName']
    csvwriter = csv.writer(productions_metadata_file, delimiter=',', dialect='excel')

    # for each row in production_1995
    for row in reader:
        if row:
            if row[0] != '' or row[1] != '[]':
                movieIds = row[0]
                productionCompanies = row[1]

                if movieIds in movieIDList:
                    productions_with_double_quotes = str(productionCompanies).replace("'", '"')
                    movie_production_data = json.loads(productions_with_double_quotes)

                    #for each JSON object in the a row
                    for record in movie_production_data:
                        all_company_ids = record["id"]
                        all_company_names = record["name"]
                        companyDict[ all_company_ids] = all_company_names

    # Write to CSV file
    csvwriter.writerow(fieldnames)
    for item in sorted (companyDict.items()):
        csvwriter.writerow(item)

    print(companyDict)
    productions_metadata_file.close()