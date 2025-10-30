from django import forms
from instructorApp.models import User

class InstructorCreateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','username','email','password']
        widgets={
            'first_name':forms.TextInput(attrs={'class':'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent', 'placeholder':"enter name"}),
            'username':forms.TextInput(attrs={'class':'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent', 'placeholder':"enter your username"}),
            'email':forms.EmailInput(attrs={'class':'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent', 'placeholder':"your@email.com"}),
            'password':forms.PasswordInput(attrs={'class':'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent', 'placeholder':"••••••••"})
        }