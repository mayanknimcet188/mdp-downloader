from __future__ import unicode_literals
import youtube_dl
import csv

urls = []
with open('./links.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        urls.extend(row)

ydl_opts = {}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(urls)
