from django import forms 

from ticketsApp.models import *

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
""" from .models import Usuario """




class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['telefono', 'correo', 'nombre', 'rut']
        labels = {
            'telefono': 'Teléfono',
            'correo': 'Correo',
            'nombre': 'Nombre',
            'rut': 'RUT',
        }

class TicketForm(forms.ModelForm):
    servicio = forms.ModelChoiceField(queryset=Servicio.objects.all())
    tipo = forms.ModelChoiceField(queryset=Tipo.objects.all())
    criticidad = forms.ModelChoiceField(queryset=Criticidad.objects.all())
    estado = forms.ModelChoiceField(queryset=Estado.objects.all())
    area = forms.ModelChoiceField(queryset=Area.objects.all())

    servicio.widget.attrs['class'] = 'form-control'
    tipo.widget.attrs['class'] = 'form-control'
    criticidad.widget.attrs['class'] = 'form-control'
    estado.widget.attrs['class'] = 'form-control'
    area.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Ticket
        fields = ['detalle', 'observacion', 'servicio', 'tipo', 'criticidad', 'estado', 'area']






class AreasForms(forms.Form):
    area = forms.CharField(label='Area', max_length=25)


class AreasForms(forms.ModelForm):
    area = forms.CharField(label='Area', max_length=25)
    area.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Area
        fields= '__all__'



class CriticidadesForms(forms.Form):
    criticidad = forms.CharField(label='Criticidad', max_length=25)


class CriticidadesForms(forms.ModelForm):
    criticidad = forms.CharField(label='Criticidad', max_length=25)
    criticidad.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Criticidad
        fields= '__all__'



class EstadosForms(forms.Form):
    estado = forms.CharField(label='Estado', max_length=25)


class EstadosForms(forms.ModelForm):
    estado = forms.CharField(label='Estado', max_length=25)

    estado.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Estado
        fields= '__all__'



class ServiciosForms(forms.Form):
    servicio = forms.CharField(label='Servicio', max_length=25)


class ServiciosForms(forms.ModelForm):
    servicio = forms.CharField(label='Servicio', max_length=25)

    servicio.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Servicio
        fields= '__all__'



class TiposForms(forms.Form):
    tipo = forms.CharField(label='Tipo', max_length=25)


class TiposForms(forms.ModelForm):
    tipo = forms.CharField(label='Tipo', max_length=25)

    tipo.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Tipo
        fields= '__all__'



class SingUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=False)
    email = forms.EmailField(required=False)

    first_name.widget.attrs['class'] = 'form-control'
    last_name.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2')
        


class CrearStuff(UserCreationForm):
    email = forms.EmailField(required=False)

    email.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    def save(self, commit = True):
        user= super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_staff = True
        if commit:
            user.save()
        return user


class CrearEjecutivo(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    password.widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']




class TicketConUsuarioForm(forms.ModelForm):
    usuario = forms.ModelChoiceField(queryset=Usuario.objects.all(), label="Seleccionar Usuario")
    
    detalle = forms.CharField(label='Detalle', max_length=100)
    observacion = forms.CharField(label='Observación', max_length=100)
    servicio = forms.ModelChoiceField(queryset=Servicio.objects.all())
    tipo = forms.ModelChoiceField(queryset=Tipo.objects.all())
    criticidad = forms.ModelChoiceField(queryset=Criticidad.objects.all())
    estado = forms.ModelChoiceField(queryset=Estado.objects.all())
    area = forms.ModelChoiceField(queryset=Area.objects.all())

    detalle.widget.attrs['class'] = 'form-control'
    observacion.widget.attrs['class'] = 'form-control'
    servicio.widget.attrs['class'] = 'form-control'
    tipo.widget.attrs['class'] = 'form-control'
    criticidad.widget.attrs['class'] = 'form-control'
    estado.widget.attrs['class'] = 'form-control'
    area.widget.attrs['class'] = 'form-control'
    

    class Meta:
        model = Ticket
        fields = ['usuario', 'detalle', 'observacion', 'servicio', 'tipo', 'criticidad', 'estado', 'area']