from particula import Particula


class Admin:
    def __init__(self):
        self.inicio = {}

    def agregar_inicio(pt):
        self.inicio = {siguiente = self.inicio, particula = pt}

    def agregar_final(pt):
        ptr = self.inicio
        while(!(ptr.siguiente is None)):
            ptr = self.siguiente
        ptr.siguiente = {patrticula: pt}

    def mostrar():
        ptr = self.inicio
        while(!(ptr is None)):
            ptr.particula.print()
            ptr = ptr.siguiente
