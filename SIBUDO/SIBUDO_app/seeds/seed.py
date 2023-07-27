import random
from faker import Faker
from django.contrib.auth.models import User, Group
from gestion_usuarios.models import persona
from django.core.exceptions import ObjectDoesNotExist

fake = Faker()

def crear_director():
    # Generar Perfil de Director
    username = 'director'
    password = 'asdF.1234'
    email = 'director@director.com'
    rol = 'Director'

    # Crear el usuario en la base de datos
    user, created = User.objects.get_or_create(username=username, email=email, first_name='Director', last_name='Director')
    user.set_password(password)
    user.save()

    # Obtener o crear un grupo (en este ejemplo, le llamaremos "MiGrupo")
    group, _ = Group.objects.get_or_create(name=rol)

    # Asignar el usuario al grupo
    user.groups.add(group)

def crear_datos_de_prueba_persona(num_personas):
    for _ in range(num_personas):
        # Generar datos ficticios para la persona
        cedula = fake.unique.random_int(min=1000000, max=99999999)
        nombre = fake.first_name()
        apellido = fake.last_name()
        fecha_nacimiento = fake.date_of_birth()
        genero = random.choice(['M', 'F', 'O'])

        # Crear un nuevo usuario asociado a la persona
        username = fake.user_name()
        password = 'asdF.1234'
        email = fake.email()

        # Verificar si el usuario ya existe en la base de datos
        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=nombre, last_name=apellido)

            # Crear la persona y vincularla al usuario
            person = persona.objects.create(cedula=cedula, nombre=nombre, apellido=apellido,
                                            fecha_nacimiento=fecha_nacimiento, genero=genero, user=user)

            # Crear un grupo
            grupos = random.choice(['Estudiante', 'Bibliotecario'])
            grupo, _ = Group.objects.get_or_create(name=grupos)

            # Asignar el usuario al grupo
            user.groups.add(grupo)

            # Guardar la persona y el usuario en la base de datos
            person.save()
            user.save()

# Instrucciones para ejecutar
# en la ruta donde se encuentra el manage.py
# abrir la consola para usar el compilador de phyton dentro de contexto del entorno virtual con el comando
#
# python manage.py shell
#
# copiar este codigo dentro de la consola:
# from SIBUDO_app.seeds.seed import crear_director, crear_datos_de_prueba_persona

# # Llamar a la función para crear el director
# crear_director()

# # Llamar a la función para generar los datos de prueba para las personas
# crear_datos_de_prueba_persona(10)
# 
# salir de la consola con exit
# luego ctrl + z
# luego enter