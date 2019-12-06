class ReglasSintacticas:
    def __init__(self):
        self.tabla_lr = []
        self.extra = []
        self.id_reglas = []
        self.long_reglas = []
        self.id_regla_int = []
        self.leer_reglas()

    def leer_reglas(self):
        file = open('compilador.lr','r')
        for linea in file.readlines():
            linea = linea.split('\t')
            if len(linea) > 3:
                for index, item in enumerate(linea):
                    try:
                        linea[index] = int(item)
                    except ValueError:
                        raise Exception('La tabla lr contiene valores invalidos. {}'.format(item))
                self.tabla_lr.append(linea)
            else:
                for index, item in enumerate(linea):
                    try:
                        linea[index] = int(item.strip())
                    except ValueError:
                        linea[index] = item.strip()
                if len(linea) == 1:
                    self.id_regla_int.append(linea[0])
                    self.long_reglas.append(0)
                    self.id_reglas.append(0)
                elif len(linea) == 2:
                    self.id_regla_int.append(linea[1])
                    self.long_reglas.append(0)
                    self.id_reglas.append(linea[0])
                elif len(linea) == 3:
                    self.id_regla_int.append(linea[0])
                    self.long_reglas.append(linea[1])
                    self.id_reglas.append(linea[2])
                self.extra.append(linea)
        file.close()

a = ReglasSintacticas()