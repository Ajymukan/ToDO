from .models import ToDo
from django.forms import ModelForm
 
class FormToDo(ModelForm):
    class Meta:
        model = ToDo
        fields = '__all__'
        # fiels = ['Title', 'des']