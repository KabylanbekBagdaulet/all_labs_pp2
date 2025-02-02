class String:
    def getstring(self):
        self.sentence=input("Sentence:")
    def printstring(self):
        print("Upper case:"+self.sentence.upper())
        
check1=String()
check1.getstring()
check1.printstring()