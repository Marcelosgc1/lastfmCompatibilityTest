import csv
from classes import *
from pathlib import Path
import heapq as pq


def write_formatted_value(writer, value, weight):
    writer.writerow({'weight': weight, 'name': value, 'listeners': list(value.num.keys())})


def Numerical_And_Logarithm_Stats(data: list, Scrobbles: dict, typeFile):
    log = open("output/log" + typeFile + ".csv", "w", encoding='utf-8')
    num = open("output/num" + typeFile + ".csv", "w", encoding='utf-8')

    list1 = []
    list2 = []
    for i in data:
        pq.heappush(list1, (i.countLog() * -1, i))
        pq.heappush(list2, (i.countNum(Scrobbles) * -1, i))
    

    field_names = ['weight', 'name', 'listeners']
    writer1 = csv.DictWriter(log, fieldnames=field_names)
    writer2 = csv.DictWriter(num, fieldnames=field_names)
    
    writer1.writeheader()
    writer2.writeheader()
    
    while (list1 and list2):
        value = pq.heappop(list1)
        write_formatted_value(writer1, value[1], value[0])
        value = pq.heappop(list2)
        write_formatted_value(writer2, value[1], value[0])
    
    log.close()
    num.close()
    

dicUsers = {}
dicArt = {}
dicAlb = {}
dicTrk = {}

artistsList = []
albunsList = []
tracksList = []

users = ['haimond','Jackson_Joe','Marcelosgc1','OsvaldoMusicas','PbzSmith','suicidxbladxs']

for i in users:
    dicUsers[i] = 0
    temp = {}
    with open('users/' + i + '.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for r in reader:
            dicUsers[i]+=1

            if r['artist_mbid'] == "":
                r['artist_mbid'] = r['artist']

            if r['album_mbid'] == "":
                r['album_mbid'] = r['album']

            if r['track_mbid'] == "":
                r['track_mbid'] = r['track']
            
            if dicArt.get(r['artist_mbid']) == None:
                dicArt[r['artist_mbid']] = Artist(i, r['artist'], r['artist_mbid'])
                artistsList.append(dicArt[r['artist_mbid']])
            else:
                dicArt[r['artist_mbid']].add(i)

            if dicAlb.get(r['album_mbid']) == None:
                dicAlb[r['album_mbid']] = Album(i, r['album'], r['album_mbid'], r['artist'])
                albunsList.append(dicAlb[r['album_mbid']])
            else:
                dicAlb[r['album_mbid']].add(i)

            if dicTrk.get(r['track_mbid']) == None:
                dicTrk[r['track_mbid']] = Track(i, r['track'], r['track_mbid'], r['artist'], r['album'])
                tracksList.append(dicTrk[r['track_mbid']])
            else:
                dicTrk[r['track_mbid']].add(i)


#print(dicUsers)


path = Path("output")
path.mkdir(exist_ok=True)

Numerical_And_Logarithm_Stats(artistsList, dicUsers, "Artist")
Numerical_And_Logarithm_Stats(albunsList, dicUsers, "Album")
Numerical_And_Logarithm_Stats(tracksList, dicUsers, "Tracks")