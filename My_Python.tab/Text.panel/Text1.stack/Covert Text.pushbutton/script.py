
from Autodesk.Revit.UI.Selection.Selection import PickObjects
from Autodesk.Revit.UI.Selection import ObjectType
from Autodesk.Revit.DB import Element,Location,TextNote,Point,XYZ,UVGridlineType,Level,Transaction,UV 
from Autodesk.Revit.Creation.Document import NewRoom
#get UIDocument
uidoc = __revit__.ActiveUIDocument
doc = uidoc.Document

#pick Object
pick = uidoc.Selection.PickObjects(ObjectType.Element)
#print(pick)

# CREAT ROOM
#Retrieve Element
roomPointX = []
roomPointY = []
listtext = []
for eleid in pick:
    elementid = eleid.ElementId 
    element = doc.GetElement(elementid)
    #get text
    textNote = element.Text
    listtext.append(textNote)
    #print(textNote)
    #Create a UV structure which determines the room location
    loca = element.Coord
    listX = loca.X 
    listY = loca.Y
    roomPointX.append(listX)
    roomPointY.append(listY)
    #get level from text note
    ownerid = element.OwnerViewId
    view = doc.GetElement(ownerid)
    genlevel = view.GenLevel
t = Transaction(doc,"Creat New Room")
t.Start()
listroom = []
#Create a new room
for X,Y in zip(roomPointX,roomPointY):
    room = doc.Create.NewRoom(genlevel,UV(X,Y))
    listroom.append(room)
#SET PARAMETER
listParameter = []
for paraRoom in listroom:
    parameterName = paraRoom.LookupParameter("Name")
    listParameter.append(parameterName)
    #print(parameterName)
for nameroom,text in zip(listParameter,listtext):
    roomName = nameroom.Set(text)
t.Commit()
