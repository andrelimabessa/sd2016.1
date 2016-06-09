class Index(object):

    def valorJogada(self, qt_Tiros):
        mapComand = {}
        print ("%d Tiro: " %(qt_Tiros))
        X = input("Informe a Coordenada X:\n")
        Y = input("Informe a Coordenada Y:\n")
        mapComand["X"] = X
        mapComand["Y"] = Y
        return str(mapComand)