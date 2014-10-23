__author__ = 'Esmir Acosta'

from unittest import TestCase
from mockito import *
from departamento import *
from empleado import *

class TestDepartamento(TestCase):
    def test_get_salario_total(self):
        #GENERO LOS MOCKS DE LA CLASE EMPLEADO
        e1 = mock(Empleado)
        e2 = mock(Empleado)
        e3 = mock(Empleado)
        #LLAMADAS DEL MOCK AL METODO
        when(e1).get_salario().thenReturn(15000)
        when(e2).get_salario().thenReturn(18000)
        when(e3).get_salario().thenReturn(20000)
        #ME CREO UN NUEVO DEPARTAMENTO
        dept = Departamento('Informatica',1111)
        #ANIADO LOS EMPLEADOS CREADOS CON EL MOCK AL NUEVO DEPARTAMENTO
        dept.aniadir_empleado(e1)
        dept.aniadir_empleado(e2)
        dept.aniadir_empleado(e3)
        #REALIZO LA COMPROBACION CON ASSERT
        self.assertEqual(dept.get_salario_total(),53000)
