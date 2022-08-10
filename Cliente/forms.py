from django.forms import EmailField, Form, IntegerField, CharField


class ClienteFormulario (Form):

    nombre= CharField()
    direccion= CharField()
    ciudad= CharField()
    email= EmailField()

class MascotaFormulario(Form):
    nombre_mascota= CharField()
    tipo= CharField()
    genero= CharField()
    edad= IntegerField()

class ProcedimientoFormulario(Form):
    procedimiento= CharField()
    costo= IntegerField()
