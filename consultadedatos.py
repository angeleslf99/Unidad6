class BusquedaSecuencial:
    def busqueda(self, lista, clave):
        #print(lista)
      #  print(clave)
        encontrado = False
        for f in range(0, len(lista)):
            for c in range(0, len(lista[f])):
                if lista[f][c] == clave:
                    encontrado = True
                    break
        return encontrado
        #encontrado = False