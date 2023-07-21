from .estudiante import Estudiante

def estudiante_candidato(request):
    estudiante = Estudiante()
    return {'estudiante':estudiante}