__author__ = 'Esmir Acosta'

from empleado import *

class Departamento():

    def __init__(self, nombre_depto, id_depto):
        self.nombre_depto = nombre_depto
        self.id_depto = id_depto
        self.empleados = []

    def aniadir_empleado(self, empleado):
        self.empleados.append(empleado)

    def get_salario_total(self):
        salario_total = 0
        for i in self.empleados:
            salario_total += i.get_salario()
        return salario_total




