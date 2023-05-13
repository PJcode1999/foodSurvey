from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "first_name",
                  "last_name", "password1", "password2")
        model = get_user_model()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already in use.')
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                "The two password fields didn't match."
            )
        return cleaned_data

    def __init__(self, *args, **kwargs,):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Username"
        self.fields["first_name"].label = "First Name"
        self.fields["last_name"].label = "Last Name"
        self.fields["email"].label = "Email address"

MOOD_CHOICES = [
    ('Happy', 'Happy'),
    ('Angry', 'Angry'),
    ('Dehydrated', 'Dehydrated'),
    ('Depressed', 'Depressed'),
    ('Excited', 'Excited'),
    ('Unwelly', 'Unwelly'),
]
RESTAURANT_CHOICES = [
    (1, 'PizzaHut'), (2, 'Dominos'), (3, 'BeijingStreet'), (4, 'KakeDiHatti'), (5, 'ItalianJoint'), (6,'ChineseYum'), (7, 'SagarRatna'), (8, 'QDs'), (9, 'DCafe'), (10, 'Tamasha'), (11, 'MasalaTrail'),
]

FOOD_CHOICES = [
    (1, 'Cholle Bhature'), (2, 'Rajma Chawal'), (3, 'Pasta'), (4, 'Garlic Bread'), (5, 'Ham'), (6, 'Spring Roll'), (7, 'Idli'), (8, 'Dosa'), (9, 'Noodles'), (10,'Chilly Paneer'), (11, 'Vada pao'), (12, 'Aaloo Tikki'), (13, 'Tea'), (14, 'Ice Cream'), (15, 'Chocolates'), (16, 'Pastries'), (17, 'Juices'), (18, 'Soft Drinks')
]

class Feedback(forms.Form):

    Restaurant = forms.CharField(
        widget=forms.Select(choices=RESTAURANT_CHOICES))
    Food = forms.CharField(widget=forms.Select(choices=FOOD_CHOICES))
    Mood = forms.CharField(label='How are you feeling today?',
                           widget=forms.Select(choices=MOOD_CHOICES))
    Rating = forms.DecimalField(
        label='Rating(On a scale of 5)', max_value=5, min_value=0)
