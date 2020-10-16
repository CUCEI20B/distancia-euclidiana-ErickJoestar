import algoritmos


class Particula:
    def __init__(self, origen_x, origen_y, destino_x, destino_y):
        self.id = id
        self.origen_x = 0
        self.origen_y = 0
        self.destino_x = 0
        self.destino_y = 0
        self.velocidad = 0
        self.red = 0
        self.green = 0
        self.blue = 0
        self.distancia = algoritmos.distancia_euclidiana(
            origen_x, origen_y, destino_x, destino_y)

    __str__(self):
        print("id:", id,
              " origen_x:", self.origen_x,
              " origen_y:", self.origen_y,
              " destino_x:", self.destino_x,
              " destino_y:" self.destino_y,
              " distancia:" self.distancia)
