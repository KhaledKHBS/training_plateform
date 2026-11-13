from django import forms
from .models import Course , CourseDocument


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["title", "description",
                  "price", "duration", "instructor"]
        labels = {
            "title": "Titre de la formation",
            "description": "Description",
            "price": "Prix (EURO)",
            "duration": "Durée (heures)",
            "instructor": "Formateur",
        }
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ex : Django pour débutants",
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Décrivez le contenu de la formation…",
            }),
            "price": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "0.00",
                "step": "0.01",
                "min": "0",
            }),
            "duration": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Ex : 20",
                "min": "1",
            }),
            "instructor": forms.Select(attrs={"class": "form-control"}),
        }

    def clean_title(self):
        title = self.cleaned_data["title"].strip()
        if len(title) < 3:
            raise forms.ValidationError("Titre trop court.")
        return title

class CourseDocumentForm(forms.ModelForm):
    class Meta:
        model = CourseDocument
        fields = ["course", "title", "file"]
