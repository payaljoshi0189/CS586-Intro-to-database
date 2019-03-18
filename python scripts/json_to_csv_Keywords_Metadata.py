#Python script to fetch keywords metadata
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


with open('keywords.csv', 'r', encoding='utf-8') as csvfile:
    keywordsDict = {}
    reader = csv.reader(csvfile, delimiter=',')
    next(reader, None)
    cnt = 0
    print("Started processing...")

    keywords_metadata_file = open('keywords_metadata.csv', 'a')
    fieldnames = ['keywordID', 'keyword']
    csvwriter = csv.writer(keywords_metadata_file, delimiter=',', dialect='excel')

    # for each row in keywords.csv
    for row in reader:
        if row:
            if row[0] != '' or row[1] != '[]':
                movieIds = row[0]
                movieKeywords = row[1]

                if movieIds in movieIDList:
                    keywords_with_double_quotes = str(movieKeywords).replace("'", '"')
                    keyword_data = json.loads(keywords_with_double_quotes)

                    #for each JSON object in the a row
                    for record in keyword_data:
                        all_keyword_ids = record["id"]
                        all_keywords = record["name"]
                        keywordsDict[ all_keyword_ids] = all_keywords

    # Write to CSV file
    csvwriter.writerow(fieldnames)
    for item in sorted (keywordsDict.items()):
        csvwriter.writerow(item)

    print(keywordsDict)
    keywords_metadata_file.close()