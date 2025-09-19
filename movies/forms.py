from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'rating']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Movie title', 'class': 'input'}),
            'rating': forms.NumberInput(attrs={'step': '0.1', 'min': '0', 'max': '10', 'class': 'input'}),
        }

    def clean_rating(self):
        r = self.cleaned_data.get('rating')
        if r is None:
            raise forms.ValidationError("Rating is required.")
        if r < 0 or r > 10:
            raise forms.ValidationError("Rating must be between 0.0 and 10.0")
        return r

