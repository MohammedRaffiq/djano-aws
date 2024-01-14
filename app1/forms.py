from django.forms import ModelForm
from .models import Room, Profile



class Createform(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'


class ProfilePicForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['img']