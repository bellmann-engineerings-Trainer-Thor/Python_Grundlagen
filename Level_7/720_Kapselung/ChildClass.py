from ParentClass import ParentClass

class ChildClass(ParentClass):

    def __init__(self):
        pass

    def changePrivate(self):
        self.__private = "Childs private"
