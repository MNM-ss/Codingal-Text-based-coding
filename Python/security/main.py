class Password:

    def __init__(self):
        self.__currentpassword = 1234

    def check(self):
        print("Current Password: {}".format(self.__currentpassword))

    def setCurrentPassword(self, pp):
        self.__currentpassword = pp

c = Password()
c.check()

c._currentpassword  = 1000
c.check()

c.setCurrentPassword(1000)
c.check()
