__author__ = 'Esmir Acosta'

from unittest import TestCase
from mockito import *
from departamento import *
from empleado import *


class TestDepartamento(TestCase):
    def test_get_salario_total(self):
        # GENERO LOS MOCKS DE LA CLASE EMPLEADO
        e1 = mock(Empleado)
        e2 = mock(Empleado)
        e3 = mock(Empleado)
        #LLAMADAS DEL MOCK AL METODO
        when(e1).get_salario().thenReturn(12000)
        when(e2).get_salario().thenReturn(14400)
        when(e3).get_salario().thenReturn(16800)
        #ME CREO UN NUEVO DEPARTAMENTO
        dept = Departamento('Informatica', 1111)
        #ANIADO LOS EMPLEADOS CREADOS CON EL MOCK AL NUEVO DEPARTAMENTO
        dept.aniadir_empleado(e1)
        dept.aniadir_empleado(e2)
        dept.aniadir_empleado(e3)
        #REALIZO LA COMPROBACION CON ASSERT
        self.assertEqual(dept.get_salario_total(), 43200)

    def test_get_salario_total_mensual(self):
        e1 = mock(Empleado)
        e2 = mock(Empleado)
        e3 = mock(Empleado)
        when(e1).get_salario_mensual().thenReturn(1000)
        when(e2).get_salario_mensual().thenReturn(1200)
        when(e3).get_salario_mensual().thenReturn(1400)
        dept = Departamento('Informatica', 1111)
        dept.aniadir_empleado(e1)
        dept.aniadir_empleado(e2)
        dept.aniadir_empleado(e3)
        self.assertEqual(dept.get_salario_total_mensual(), 1200)