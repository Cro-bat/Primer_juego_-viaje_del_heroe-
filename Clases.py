class Lugar:
    def __init__(self, prob_min, prob_max, descripcion, evento_1, evento_2):
        self.prob_min = prob_min
        self.prob_max = prob_max
        self.descripcion = descripcion
        self.evento_1 = evento_1
        self.evento_2 = evento_2

class Evento:
    def __init__(self, nombre, premio, premio_es_atajo, castigo, probabilidad, descripcion, descripcion_premio, descripcion_castigo):
        self.nombre = nombre
        self.premio = premio
        self.premio_es_atajo = premio_es_atajo
        self.castigo = castigo
        self.probabilidad = probabilidad
        self.descripcion = descripcion
        self.descripcion_premio = descripcion_premio
        self.descripcion_castigo = descripcion_castigo
