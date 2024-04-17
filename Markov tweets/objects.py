class myobj:
    avar = 0
    def myfunc(self, b):
        self.avar = b +1
        return self.avar
    
    def Twofun(self,c):
        d = c + 1
        self.avar = c + d
        return self.avar

# mo = myobj()
# mo.avar
#
# dd = mo.myfunc(7)
# print(dd)

print(myobj().Twofun(2))
print(type(myobj()))