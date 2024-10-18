class ParentClass:
    def __init__(self):
        self.public = "Parents public"
        self._protected = "Parents _protected"
        self.__private = "Parents __private"

    def getPublic(self):
        return self.public

    def get_protected(self):
        return self._protected

    def get__private(self):
        return self.__private


    def __privateMethode(self):
        return "ich bin privat"
