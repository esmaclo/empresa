__author__ = 'Esmir Acosta'
from empleado import *


class Departamento():
    """
    Clase que representa un departamento
    """
    def __init__(self, nombre_depto, id_depto):
        """
        Metodo constructor de la clase Departamento

        Inicializa dos atributos con los datos pasados como parametros y aparte una lista vacia de empleados

        :param nombre_depto: Nombre del departamento
        :type nombre_depto: str
        :param id_depto: Identificador del departamento
        :type id_depto: str
        """
        self.nombre_depto = nombre_depto
        self.id_depto = id_depto
        self.empleados = []

    def aniadir_empleado(self, empleado):
        """
        Aniadir un empleado

        Metodo que aniade un empleado a la lista de empleados

        :param empleado: Empleado a aniadir a la lista de empleados del departamento
        :type empleado: Empleado
        """
        self.empleados.append(empleado)

    def get_salario_total(self):
        """
        Metodo que devuelve el salario total de los empleados

        Se calcula el salario total de los empleados del departamento

        :var salario_total: Empieza con 0 y se ira sumando todos los salarios de los empleados
        :type salario_total: int
        :var i: Contendra cada empleado de la lista de empleados por cada iteracion del for
        :type i: Empleado
        :return: Devuelve el salario total de todos los empleados
        :rtype: int
        """
        salario_total = 0
        for i in self.empleados:
            salario_total += i.get_salario()
        return salario_total

    def get_nombre_depto(self):
        """
        Metodo consultor del atributo propio nombre_depto

        Devuelve el nombre del departamento

        :return: Nombre del departamento
        :rtype: str
        """
        return self.nombre_depto

    def get_salario_total_mensual(self):
        """
        Metodo que devuelve la media del salario de los empleados

        Se calcula la media a partir de la suma del salario mensual de cada empleado y dividiendo por el numero de ellos

        :var s_m_total: Contendra la suma del salario mensual de cada empleado
        :type s_m_total: int
        :return: Devuelve la media de salario mensual
        :rtype: int
        """
        s_m_total = 0
        for i in self.empleados:
            s_m_total += i.get_salario_mensual()
        return  s_m_total / len(self.empleados)