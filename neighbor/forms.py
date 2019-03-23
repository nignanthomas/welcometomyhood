from django import forms
from .models import Profile, Business, Neighborhood, Post, Comment

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        fields = ('name', 'location', 'occupants')

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user', 'neighborhood']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'neighborhood']
