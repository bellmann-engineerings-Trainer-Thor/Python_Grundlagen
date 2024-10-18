from ParentClass import ParentClass
from ChildClass import ChildClass


#################################################################################################
# ParentClass - ObjektAttribute nutzen
#################################################################################################
print("ParentClass - ObjektAttribute nutzen")

parent = ParentClass()
print(parent.public)
print(parent._protected)  # Funktioniert, aber sollte nicht verwendet werden. Konvention
# print(parent.__private)  # Dies wird einen AttributeError verursachen, da __private privat ist

#################################################################################################
# ChildClass - ObjektAttribute nutzen
#################################################################################################
print("ChildClass - ObjektAttribute nutzen")

child = ChildClass()
print(child.public)
print(child._protected)  # Funktioniert, aber sollte nicht verwendet werden. Konvention
# print(child.__private)  # Dies wird einen AttributeError verursachen, da __private privat ist


#################################################################################################
# ParentClass - ObjektMethoden nutzen
#################################################################################################
print("ParentClass - ObjektMethoden nutzen")

parent = ParentClass()
print(parent.getPublic())
print(parent.get_protected())
print(parent.get__private())
# print(parent.__privateMethode())   # Auch Funktionen können privat sein


#################################################################################################
# ChildClass - ObjektMethoden nutzen
#################################################################################################
print("ChildClass - ObjektMethoden nutzen")

child = ChildClass()
print(child.getPublic())
print(child.get_protected())
print(child.get__private())

#################################################################################################
# !!!!!!!!  hier sehen wir die darseinsberechtigung von "_" dem Protected-Modifier
#################################################################################################
child.changePrivate()
print(child.get__private())

# print(child.__privateMethode())   # Auch Funktionen können privat sein

