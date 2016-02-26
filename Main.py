from Entities.FieldManager import FieldManager

fieldManager = FieldManager(5)
fieldManager.markCoords(2,4, True)
fieldManager.markCoords(2,4, False)
fieldManager.printFieldAsText()