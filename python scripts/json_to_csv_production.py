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
    reader = csv.reader(csvfile, delimiter=',')
    next(reader, None)
    cnt = 0
    print("Started processing...")

    productions_data_processed_file = open('productions_data_processed.csv', 'a')
    fieldnames = ['movieID', 'companyID']
    csvwriter = csv.writer(productions_data_processed_file, delimiter=',', dialect='excel')

    for row in reader:
        if row:
            if row[0] != '' or row[1] != '[]':
                movieIds = row[0]
                productionCompanies = row[1]

                if movieIds in movieIDList:
                    productions_with_double_quotes = str(productionCompanies).replace("'", '"')
                    productions_with_no_apostrophe = str(productions_with_double_quotes).replace('"', "")
                    #productions_with_unicode_chars = str(productions_with_no_apostrophe).replace('\xa0', '')

                    print('KEYWORD_ID_STRING', productions_with_double_quotes)
                    movie_keyword_data = json.loads(productions_with_double_quotes)

                    for record in movie_keyword_data:
                        all_company_ids = record["id"]
                        all_comany_names = record["name"]
                        final_list = [movieIds, all_company_ids]

                        if cnt == 0:
                            csvwriter.writerow(fieldnames)
                        else:
                            csvwriter.writerow(final_list)

                        cnt += 1
    productions_data_processed_file.close()