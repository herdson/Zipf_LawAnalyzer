import collections
import urllib.request
import matplotlib.pyplot as plt


class Analy:
    def __init__(self):
        self.dectarget = ''
        self.txtdecoder = []
        self.result = {}
        self.detect = ''

    def settarget(self, txt):
        self.dectarget = txt

    #Detect name is filename or URL
    def setdetect(self, txt):
        self.detect = txt

    def gettarget(self):
        return self.dectarget

    def getdetect(self):
        return self.detect

    def counter(self):
        # Decode URL
        if self.getdetect() == 'URL':
            try:
                target = urllib.request.urlopen(self.dectarget)
                data = target.read()
                decoder = data.decode('utf-8')

            except:
                msg = "Process failed"
                return msg

        # Decode FILE
        elif self.getdetect() == 'FILE':
            try:
                target = open(self.dectarget, 'r')
                decoder = target.read()

            except:
                msg = "Process failed"
                return msg

        else: return "Error occured"

        #Make word list
        wdlist = decoder.upper().split()

        #Delete useless tokens
        for i in range(len(wdlist)):
            self.txtdecoder.append(wdlist[i].strip(",.?!#$:-;*\'\"[]{}()/"))

        #Generate word dictionary counted word numbers
        self.result = collections.Counter(wdlist)

        #Collect top 5 values
        resultchart = dict(self.result.most_common(5))
        maxval = int(max(resultchart.values()))

        #Based on the most top value, the remaining 4 values are explained as a ratio divided by 1st value.
        #(1st value is 1)
        for j in resultchart:
            resultchart[j] /= maxval


        # https://stackoverflow.com/questions/712082/barchart-sizing-of-text-barwidth-with-matplotlib-python
        # plt.figure(figsize=(8, 10))
        # https://stackoverflow.com/questions/21925007/using-dictionary-to-make-a-matplotlib-graph
        plt.bar(range(len(resultchart)), resultchart.values(), align='center' ,width=0.8)
        plt.xticks(range(len(resultchart)), list(resultchart.keys()))

        return plt.show()