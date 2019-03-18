#Python script to fetch keywords
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
    reader = csv.reader(csvfile, delimiter=',')
    next(reader, None)
    cnt = 0
    print("Started processing...")

    keywords_data_processed_file = open('keywords_data_processed.csv', 'a')
    fieldnames = ['movieID', 'keywordID']
    csvwriter = csv.writer(keywords_data_processed_file, delimiter=',', dialect='excel')

    for row in reader:
        if row:
            if row[0] != '' or row[1] != '[]':
                movieIds = row[0]
                keywords = row[1]

                #Check if the movie belongs to movies_1995 data
                if movieIds in movieIDList:
                    keyword_with_double_quotes = str(keywords).replace("'", '"')
                    keyword_with_no_apostrophe = str(keyword_with_double_quotes).replace('"', "")
                    keyword_with_unicode_chars = str(keyword_with_no_apostrophe).replace('\xa0', '')

                    print('KEYWORD_ID_STRING', keyword_with_double_quotes)
                    movie_keyword_data = json.loads(keyword_with_double_quotes)

                    for record in movie_keyword_data:
                        all_key_ids = record["id"]
                        all_keywords = record["name"]
                        final_list = [movieIds, all_key_ids]

                        if cnt == 0:
                            csvwriter.writerow(fieldnames)
                        else:
                            csvwriter.writerow(final_list)

                        cnt += 1
    keywords_data_processed_file.close()