import csv
import heapq as pq
import math as m

dicSongs = {}
dicUsers = {}

dicTotal = {}
dicLog = {}
musicasNumerico = []
musicasLog = []


users = ['haimond','Jackson_Joe','Marcelosgc1','OsvaldoMusicas','PbzSmith','suicidxbladxs']
#users = ['PbzSmith']
for i in users:
    temp = {}
    with open('projetomusica\\' + i + '.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for r in reader:
            r.pop()
            song = r[2]+'/'+r[0]

            if dicSongs.get(song)==None:
                dicSongs[song]=r

            if temp.get(song)==None:
                temp[song]=0
                
            temp[song]+=1
            
    
    for k, v in temp.items():
        if dicTotal.get(k)==None:
            dicTotal[k]=0
        dicTotal[k]+=v

        if dicLog.get(k)==None:
            dicLog[k]=1
        dicLog[k]*=v

    dicUsers[i]=temp



for k,v in dicTotal.items():
    pq.heappush(musicasNumerico, (v*(-1), k))
    pq.heappush(musicasLog, (dicLog[k]*(-1), k))

with open("projetomusica\\log.csv", "w", encoding='utf-8') as log:
    with open("projetomusica\\num.csv", "w", encoding='utf-8') as num:
        writer = csv.writer(log)
        writer2 = csv.writer(num)

        while musicasLog!=[]:
            logmus=pq.heappop(musicasLog)
            #if logmus[0]==-1:
            #    break
            nummus=pq.heappop(musicasNumerico)
            listaOuvintes = []
            for j in users:
                if dicUsers[j].get(logmus[1])!=None:
                    listaOuvintes.append(j)
                    
            t=[]
            t.append(logmus[0]*-1)
            t.append(logmus[1])
            t.append(listaOuvintes)
            writer.writerow(t)

            t=[]
            t.append(nummus[0]*-1)
            t.append(nummus[1])
            t.append(listaOuvintes)            
            writer2.writerow(t)