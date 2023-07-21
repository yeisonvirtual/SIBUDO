class Estudiante:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        estudiante = self.session.get('estudiante')

        if not estudiante:
            estudiante = self.session['estudiante'] = {
                'id':0,
                'cedula':0,
                'nombre':'',
                'apellido':'',
                'estado':0
            }

        self.estudiante = estudiante
    
    def guardar_estudiante(self):
        self.session['estudiante'] = self.estudiante
        self.session.modified = True
    
    def actualizar(self, new_estudiante):
        self.estudiante = {
            'id':new_estudiante.id,
            'cedula':new_estudiante.cedula,
            'nombre':new_estudiante.nombre,
            'apellido':new_estudiante.apellido,
            'estado':new_estudiante.estado
        }
        self.guardar_estudiante()
    
    def limpiar(self):
        self.estudiante = {
            'id':0,
            'cedula':0,
            'nombre':'',
            'apellido':'',
            'estado':0
        }
        self.guardar_estudiante()