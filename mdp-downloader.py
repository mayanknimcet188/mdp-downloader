from __future__ import unicode_literals
import youtube_dl

ydl_opts = {}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://bae.sgp1.digitaloceanspaces.com/videos/142/dash/3c328863dbadd9c5ca8f7bc444a6ea73.mpd'])
