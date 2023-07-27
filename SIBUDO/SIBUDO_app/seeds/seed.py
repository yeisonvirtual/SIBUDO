import random
from faker import Faker
from django.contrib.auth.models import User, Group
from gestion_usuarios.models import persona
from django.core.exceptions import ObjectDoesNotExist
from gestion_recursos.models import libro, cantidad_libro, trabajo, cantidad_trabajo
from gestion_prestamos.models import Prestamo, Recurso_Disponible, Sancion
from datetime import date, timedelta
from django.db.models import Q
from datetime import datetime

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

def crear_personas(num_personas):
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

def crear_libros_trabajos(num_elementos):
    # Crear libros de prueba
    for _ in range(num_elementos):
        nombre = fake.catch_phrase()
        autor = fake.name()
        edicion = random.randint(1, 10)
        anio = random.randint(1990, 2023)
        isbn = fake.isbn13()
        
        libro_n = libro.objects.create(nombre=nombre, autor=autor, edicion=edicion, anio=anio, isbn=isbn)
        
        # Crear cantidad disponible de libros
        cantidad = random.randint(1, 20)
        cantidad_libro_n = cantidad_libro.objects.create(libro=libro_n, cantidad=cantidad)
        cantidad_libro_n.save()

        id_nuevo = libro.objects.get(isbn=isbn)
        now = datetime.now()

        recurso_disponible = Recurso_Disponible(id_recurso=id_nuevo.id, tipo_recurso=1, n_disponibles=cantidad, tipo_prestamo=1, created=now, updated=now)
        recurso_disponible.save()
        

    # Crear trabajos de prueba
    for _ in range(num_elementos):
        titulo = fake.job()
        autor = fake.name()
        palabras_clave = ', '.join(fake.words(5))
        fecha = fake.date_this_decade()
        
        trabajo_n = trabajo.objects.create(titulo=titulo, autor=autor, palabras_clave=palabras_clave, fecha=fecha)
        
        # Crear cantidad disponible de trabajos
        cantidad = random.randint(1, 10)
        cantidad_trabajo_n = cantidad_trabajo.objects.create(trabajo=trabajo_n, cantidad=cantidad)
        cantidad_trabajo_n.save()

        id_nuevo = trabajo.objects.get(titulo=titulo)
        now = datetime.now()
        recurso_disponible = Recurso_Disponible(id_recurso=id_nuevo.id, tipo_recurso=2, n_disponibles=cantidad, tipo_prestamo=0, created=now, updated=now)
        recurso_disponible.save()


######################## Intruccionses ############################
# Instrucciones para ejecutar
# en la ruta donde se encuentra el manage.py
# abrir la consola para usar el compilador de phyton dentro de contexto del entorno virtual con el comando
#
# python manage.py shell
#
# copiar este codigo dentro de la consola:


# from SIBUDO_app.seeds.seed import crear_director, crear_personas, crear_libros_trabajos, crear_prestamos
# crear_director()
# crear_personas(20)
# crear_libros_trabajos(20)


#
#
#
# salir de la consola con exit()

###################################Instrucciones################################









################################ ignorar ####################

# def crear_prestamos():
#     personas = persona.objects.all()
#     libros_n = libro.objects.all()
#     # trabajos_n = trabajo.objects.all()

#     fecha_inicio = date(1990, 1, 1)
#     fecha_actual = date.today()
#     diferencia_dias = (fecha_actual - fecha_inicio).days

#     #libros
#     try:
#         for persona_obj in personas:
#             print("entroooooooo")
#             libro_aleatorio = random.choice(libros_n)
#             dias_aleatorios = random.randint(0, diferencia_dias)
#             fecha_aleatorea = fecha_inicio + timedelta(days=dias_aleatorios)

#             id_est = persona_obj.id
#             tipo_recurso = 1
#             id_recurso = libro_aleatorio.id
#             fecha_prestamo = fecha_aleatorea
#             fecha_devolucion = fecha_aleatorea + timedelta(days=7)
#             estado_prestamo = 1

#             persona_obj.estado = 0
#             libro_disponible = Recurso_Disponible.objects.get(Q(id_recurso = libro_aleatorio.id) & Q(tipo_recurso = 1) )

#             libro_disponible.n_disponibles-=1
        
#             prestamo = Prestamo(id_est= id_est,tipo_recurso=tipo_recurso,  id_recurso= id_recurso, fecha_prestamo=fecha_prestamo, fecha_devolucion=fecha_devolucion, estado_prestamo=estado_prestamo)

#             prestamo.save()
#             libro_disponible.save()
#             persona_obj.save()

#     except ObjectDoesNotExist:
#         pass
    

    # for persona_obj in personas:
    #     # Asignar libros disponibles a la persona
    #     cantidad_libros = random.randint(1, 5)  # Puedes ajustar la cantidad de libros por persona
    #     libros_aleatorios = random.sample(list(libros), cantidad_libros)

    #     for libro in libros_aleatorios:
    #         cantidad = random.randint(1, 3)  # Puedes ajustar la cantidad de copias prestadas por libro
    #         CantidadLibro.objects.create(libro=libro, cantidad=cantidad)

    #     # Asignar trabajos disponibles a la persona
    #     cantidad_trabajos = random.randint(1, 5)  # Puedes ajustar la cantidad de trabajos por persona
    #     trabajos_aleatorios = random.sample(list(trabajos), cantidad_trabajos)

    #     for trabajo in trabajos_aleatorios:
    #         cantidad = random.randint(1, 3)  # Puedes ajustar la cantidad de copias prestadas por trabajo
    #         CantidadTrabajo.objects.create(trabajo=trabajo, cantidad=cantidad)
