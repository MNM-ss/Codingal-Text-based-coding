class myClass:
    _privatevar = 27;
    def _privmeth(self):
        print("I'm in class myClass")

    def _hello(self):
        print("Private variable Value: ", myClass._privatevar)

foo = myClass()
foo.hello()
#foo._privmeth



