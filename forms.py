from django.contrib.auth.models import User
from datetime import datetime

from django import forms

from .models import Profile, Univer_Profile
""", Club_Profile, Open_Position_for_Un, Open_Position_for_Cl, Extra_Languages, \
    Achivment, Teem"""


class User_Form_Reg(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}))

    class Meta:
        model = User
        fields = (
            'email',
        )


class UserForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}))

    class Meta:
        model = User
        fields = (
            'email',
        )


def c_name():
    data = [i for i in open('Country.txt').readlines()]
    return data

CHOICES = [
    ('right', 'right'),
    ('left', 'left'),
]

UN_or_CL = [
    ('University', 'University'),
    ('Club', 'Club')
]

HAND = [
    ('Right', 'Right'),
    ('Left', 'Left'),
]

class user_main_form(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}))
    year = datetime.now()
    birth_date = forms.DateField(
        widget=forms.SelectDateWidget(years=range(int(str(year)[0:4]) - 12, 1970, -1),
                                      attrs={'class': 'form-select form-select-sm', 'style': 'margin-top: 10px;'}))
    #phone_num = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'class': 'form-control ps-5'}))
    country = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}))
   # whats_app = forms.BooleanField(
    #    widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: auto;'}),
    #    label='WhatsApp', label_suffix='')
    insta = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}))
    telega = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}), label='Telegram')
    agree_to_private_rule = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: auto;'}),
        label='Agree to private rule', label_suffix='')



    eng_skill = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}),
                                help_text='Please, choose from 1 to 10')
    '''languages = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}),
                                help_text='Please, enter language which you speak'
                                          '<br> Exemple: English, Russian, German')'''
    languages = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}),
                                help_text='Please, choose from 1 to 10')
    eng_class = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}), label='English')
    math_class = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}), label='Math')
    natural_science_class = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}),
                                               label='Natural / Physical science')
    additional_class = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}),
                                          label='Additional class')
    social_science = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}),
                                        label='Social science')
    additional_courses = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}),
                                            label='Additional courses')
    sat = forms.BooleanField(required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: auto;'}), label='SAT',
        label_suffix='', help_text='')

    act = forms.BooleanField(required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: auto;required="false";'}), label='ACT',
        label_suffix='', help_text='<a style = "color: #9933ff;" href = "https://www.act.org/" > Click <a/>')

    toefl = forms.BooleanField(required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: auto;required="false";'}), label='TOEFL',
        label_suffix='', help_text='<a style = "color: #9933ff;" href = "https://www.ets.org/toefl" > Click <a/>')

    ielts = forms.BooleanField(required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: auto;required="false";'}), label='IELTS',
        label_suffix='', help_text='')

    scholarship = forms.BooleanField(required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: auto;required="false";'}),
        label='Scholarship',
        label_suffix='')



    sport = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}))
    position = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}))
    main_achivment = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}))
    sport_org_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}),
                                     label='Name of sports organization')
    sport_org_link = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}),
                                    label='Link of sports organization')
    highlights_link = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}))
    stats_link = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}))
    live_stream_link = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}))
    # highlights_link2= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}))
    height_inch = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}))
    height_cm = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}))
    weight_pound = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}))
    weight_kg = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}))
    university_or_club = forms.ChoiceField(widget=forms.RadioSelect(attrs={}),
                                           choices=UN_or_CL)
    ex = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}), label="Experience")
    pay_or_not = forms.BooleanField(required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: auto;'}),
        label='Pay or not', label_suffix='')
    league_resolution = forms.BooleanField(required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: auto;required="false";'}),
        label='League resolution', label_suffix='',
        help_text='<a style="color: #9933ff;" href = "https://www.ncaa.org/student-athletes/future/international-student-athletes">Click<a/>')
    hand = forms.ChoiceField(widget=forms.RadioSelect(attrs={}),
                             choices=HAND, label_suffix='', label='Hand')
    national_teem = forms.BooleanField(required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: auto;required="false";'}),
        label='National teem', label_suffix='')

    class Meta:
        model = Profile
        fields = (
            'first_name',
            'last_name',
            'email',
            'birth_date',
            # 'phone_num',
            'country',
            # 'whats_app',
            'insta',
            'telega',
            'agree_to_private_rule',
            'eng_skill',
            'languages',
            'scholarship',
            'eng_class',
            'math_class',
            'natural_science_class',
            'additional_class',
            'social_science',
            'additional_courses',
            'sat',
            'act',
            'toefl',
            'ielts',
            'sport',
            'main_achivment',
            'ex',
            'position',
            'sport_org_name',
            'sport_org_link',
            'stats_link',
            'live_stream_link',
            'highlights_link',
            'pay_or_not',
            'hand',
            'height_inch',
            'height_cm',
            'weight_pound',
            'weight_kg',
            'league_resolution',
            'national_teem',
            'university_or_club',
        )


class user_letter_form(forms.ModelForm):
    letter = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control ps-5'}))

    class Meta:
        """model = Profile"""
        fields = (
            'letter',
        )


class Un_ProfileForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control ps-5'}))
    link = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}))
    univers_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}))

    class Meta:
        """model = Univer_Profile"""
        fields = (
            'univers_name',
            'link',
            'description'
        )


class Cl_ProfileForm(forms.ModelForm):
    class Meta:
        '''model = Club_Profile'''
        fields = (
            'link',
        )


GRANT_CHOOSE = [
    ('Full', 'Full'),
    ('Not full', 'Not full'),
    ('None', 'None')
]


class Un_Position_Form(forms.ModelForm):
    active = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: auto;'}),
        label='Show this position', label_suffix='')
    sport_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}))

    teem_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}))

    position = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}))

    grant = forms.ChoiceField(widget=forms.RadioSelect(attrs={}), label_suffix='', label='Grant', choices=GRANT_CHOOSE)

    requirements = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control ps-5'}))

    class Meta:
        '''model = Open_Position_for_Un'''
        fields = (
            'active',
            'sport_name',
            'position',
            'grant',
            'requirements',
            'teem_name',
        )


class Cl_Position_Form(forms.ModelForm):
    class Meta:
        '''model = Open_Position_for_Cl'''
        fields = (
            'active',
            'sport_name',
            'position',
        )


class User_Lang_Form(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}))
    level = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}), label='Your level')
    flag = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: auto;'}),
        label='Show', label_suffix='')

    class Meta:
        '''model = Extra_Languages'''
        fields = (
            'name',
            'level',
            'flag',
        )


ACH_TYPE = [
    ('Club', 'Club'),
    ('Regional', 'Regional'),
    ('National', 'National'),
    ('Records', 'Records'),
]


class User_Ach_Form(forms.ModelForm):
    title_of_achiv = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}))
    type = forms.ChoiceField(widget=forms.RadioSelect(attrs={}),
                             choices=ACH_TYPE, label_suffix='', label='Type of achivment')
    year = datetime.now()
    date = forms.DateField(
        widget=forms.SelectDateWidget(years=range(int(str(year)[0:4]), 1970, -1),
                                      attrs={'class': 'form-select form-select-sm', 'style': 'margin-top: 10px;'}))
    flag = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: auto;'}),
        label='Show', label_suffix='')

    class Meta:
        '''model = Achivment'''
        fields = (
            'title_of_achiv',
            'type',
            'date',
            'flag',
        )


class User_Teem_Form(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}))
    link = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control ps-5'}))
    flag = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: auto;'}),
        label='Show', label_suffix='')

    class Meta:
        '''model = Teem'''
        fields = (
            'name',
            'link',
            'flag',
        )
