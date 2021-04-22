from rest_framework.test import APITestCase

from empleados.models import Empleado
from puestos.models import Puesto


class TestEmpleadoCRUD(APITestCase):

    def setUp(self):
        self.host = 'http://127.0.0.1:8000/'
        self.puesto = Puesto.objects.create(
            cargo='Cargo 1',
            area='Area 1'
        )

        self.empleado = Empleado.objects.create(
            nombre="Empleado 1",
            apellido="Empleado 1",
            email="empleado@gmail.com",
            puesto=self.puesto
        )

    def test_get_empleados(self):
        response = self.client.get(f'{self.host}empleados/')
        print(response.status_code)
        print(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(self.empleado.id, response.data[0]['id'])

    def test_post_empleados(self):
        data = {
            'nombre': "Empleado 1",
            'apellido': "Empleado 1",
            'email': "empleado@gmail.com",
            'puesto': [self.puesto.id]
        }

        response = self.client.post(f'{self.host}empleados/', data)

        self.assertEqual(response.status_code, 201, response.data)
        self.assertEqual(Empleado.objects.all().count(), 2)

    def test_delete_empleado(self):
        response = self.client.delete(f'{self.host}empleados/1/')
        empleado = Empleado.objects.all()
        self.assertEqual(response.status_code, 204)
        self.assertEqual(len(empleado), 0)

    def test_patch_empleados(self):
        data = {
            'nombre': 'Miguel'
        }
        response = self.client.patch(f'{self.host}empleados/1/', data)
        empleado = Empleado.objects.get(id=1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(empleado.nombre, 'Miguel')