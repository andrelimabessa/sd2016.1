from Entities.FieldManager import FieldManager
from Entities.Player import Player

fieldManager = FieldManager(5)
fieldManager.markCoords(2,4, True)
fieldManager.markCoords(2,4, False)
fieldManager.printFieldAsText()