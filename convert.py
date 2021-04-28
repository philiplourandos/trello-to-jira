#!/bin/python3

import csv
import json
import sys
import jsonpath_rw_ext
from jsonpath_ng.ext import parse

inputFile = sys.argv[1]

print(f"Input file: {inputFile}")

csvHeader = ['id', 'description', 'shortUrl', 'start', 'url']

with open(inputFile, "r", encoding="UTF-8") as reader:
    jsonContent = json.load(reader)

    cards = jsonpath_rw_ext.match('$.cards', jsonContent)

    totalCards = len(cards[0])

    if totalCards > 0:
        with open('jira.csv', 'w', newline='') as csvfile:
            ticketWriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            ticketWriter.writerow(csvHeader)

            for cardIndex in range(totalCards):
                ticketWriter.writerow([cards[0][cardIndex]['id'], cards[0][cardIndex]['desc'], 
                    cards[0][cardIndex]['shortUrl'], cards[0][cardIndex]['start'], cards[0][cardIndex]['url']])
