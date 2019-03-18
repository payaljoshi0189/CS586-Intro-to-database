#Python script to fetch Genres metadata
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
    genersDict = {}
    reader = csv.reader(csvfile, delimiter=',')
    next(reader, None)
    cnt = 0
    print("Started processing...")

    genres_metadata_file = open('genres_metadata.csv', 'a')
    fieldnames = ['genreID', 'genre']
    csvwriter = csv.writer(genres_metadata_file, delimiter=',', dialect='excel')

    # for each row in genres_1995
    for row in reader:
        if row:
            if row[0] != '' or row[1] != '[]':
                genres = row[0]
                movieIds = row[1]

                if movieIds in movieIDList:
                    genres_with_double_quotes = str(genres).replace("'", '"')
                    movie_genres_data = json.loads(genres_with_double_quotes)

                    #for each JSON object in the a row
                    for record in movie_genres_data:
                        all_genre_ids = record["id"]
                        all_genre_names = record["name"]
                        genersDict[ all_genre_ids] = all_genre_names

    # Write to CSV file
    csvwriter.writerow(fieldnames)
    for item in sorted (genersDict.items()):
        csvwriter.writerow(item)

    print(genersDict)
    genres_metadata_file.close()