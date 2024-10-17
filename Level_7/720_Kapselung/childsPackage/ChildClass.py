from ..parentsPackage.ParentClass import ParentClass

class ChildClass(ParentClass):
    def __init__(self):
        super().__init__()
        self.public = "Childs public"
        self._protected = "Childs _protected"
        self.__private = "Childs __private"
