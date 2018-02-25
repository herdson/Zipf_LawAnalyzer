#This module role to get target URL or file name
class Crawler:

    def __init__(self):
        self.name = ''

    def Setname(self, txt):
        self.name = txt

    def Getname(self):
        return self.name
