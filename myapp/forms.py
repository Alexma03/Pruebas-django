from django import forms

class CreateNewTask(forms.Form):
    name = forms.CharField(label="Nombre de la tarea", max_length=200)
    description = forms.CharField(label="Descripcion de la tarea",widget=forms.Textarea)