from ParentClass import ParentClass
from ..childsPackage.ChildClass import ChildClass

parent = ParentClass()
print(parent.public)
print(parent._protected)  # Funktioniert, aber sollte nicht verwendet werden. Konvention
print(parent.__private)  # Dies wird einen AttributeError verursachen, da __private privat ist
print(parent.get_private())  # Richtige Art, auf private Attribute zuzugreifen

child = ChildClass()
print(child.public)
print(child._protected)  # Funktioniert, aber sollte nicht verwendet werden. Konvention
print(child.__private)  # Dies wird einen AttributeError verursachen, da __private privat ist
print(child.get_private())  # Returniert das Parent __private
