class Countable:
    def __init__(self, name, identifier, user) -> None:
        self.num = {} 
        self.num[user] = 1  
        self.identifier = identifier
        self.name = name
        self.weight = -1
        self.weightLog = -1

    def add(self, user) -> None:
        if self.num.get(user) == None:
            self.num[user] = 0
        self.num[user]+=1

    def countNum(self, scr: dict) -> int:        
        sum = 0
        for i in self.num:
            sum += self.num[i] / scr[i]
        self.weight = sum * self.num.__len__()

        return self.weight
    
    def countLog(self) -> int:        
        log = 1
        for i in self.num:
            log *= self.num[i]
        self.weightLog = log

        return self.weightLog
    
    def __lt__(self, other):
        return True


class Track(Countable):
    def __init__(self, user, name, identifier, artist, album) -> None:
        self.artist = artist
        self.album = album
        super().__init__(name, identifier, user)


    def __str__(self):
        return self.name + "/" + self.artist + "/" + self.album

class Album(Countable):
    def __init__(self, user, name, identifier, artist) -> None:
        self.artist = artist
        super().__init__(name, identifier, user)

    def __str__(self):
        return self.name + "/" + self.artist


class Artist(Countable):

    def __init__(self, user, name, identifier) -> None:
        super().__init__(name, identifier, user)

    def __str__(self):
        return self.name
