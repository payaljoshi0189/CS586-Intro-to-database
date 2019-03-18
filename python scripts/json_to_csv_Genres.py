#working on small file
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


with open('genres_1995.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader, None)
    cnt = 0
    print("Started processing...")

    genres_data_processed_file = open('genres_data_processed.csv', 'a')
    fieldnames = ['movieID', 'genreID']
    csvwriter = csv.writer(genres_data_processed_file, delimiter=',', dialect='excel')

    for row in reader:
        if row:
            if row[0] != '' or row[1] != '[]':
                genres = row[0]
                movieIds = row[1]

                if movieIds in movieIDList:
                    genres_with_double_quotes = str(genres).replace("'", '"')
                    genres_with_no_apostrophe = str(genres_with_double_quotes).replace('"', "")
                    genres_with_unicode_chars = str(genres_with_no_apostrophe).replace('\xa0', '')

                    print('KEYWORD_ID_STRING', genres_with_unicode_chars)
                    movies_genres_data = json.loads(genres_with_double_quotes)

                    for record in movies_genres_data:
                        all_genre_ids = record["id"]
                        all_genres = record["name"]
                        final_list = [movieIds, all_genre_ids]

                        if cnt == 0:
                            csvwriter.writerow(fieldnames)
                        else:
                            csvwriter.writerow(final_list)

                        cnt += 1
    genres_data_processed_file.close()