from django.core.files.storage import FileSystemStorage
from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Small_admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Profile(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    #biscuits =models.CharField(max_length=150, blank=False,null=True)
    id = models.IntegerField(primary_key=True)
    user_flag = models.BooleanField(default=False, blank=False)
    is_user = models.BooleanField(default=True, blank=False)

    # avatar = models.ImageField(upload_to='static/Users/data/photos/',default='static/Users/data/photos/temp.jpg',blank=False)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(null=True, blank=False)
    #phone_num = models.CharField(max_length=12, blank=True)
    country = models.CharField(max_length=100, blank=True)
   #whats_app = models.BooleanField(default=True, blank=True)
    email = models.EmailField(blank=False)
    insta = models.CharField(max_length=50, blank=True)
    telega = models.CharField(max_length=50, blank=False, default='')
    agree_to_private_rule = models.BooleanField(default=False, blank=True)
    bio_check = models.BooleanField(default=False)

    '''  '''
    eng_skill = models.CharField(max_length=2, blank=False)
    languages = models.CharField(max_length=150, blank=False)
    scholarship = models.BooleanField(default=False)
    # school classes
    eng_class = models.IntegerField(default=0, blank=True)
    math_class = models.IntegerField(default=0, blank=True)
    natural_science_class = models.IntegerField(default=0, blank=True)
    additional_class = models.IntegerField(default=0, blank=True)
    social_science = models.IntegerField(default=0, blank=True)
    additional_courses = models.IntegerField(default=0, blank=True)
    # end classes
    # tests
    sat = models.BooleanField(default=False)
    act = models.BooleanField(default=False)
    toefl = models.BooleanField(default=False)
    ielts = models.BooleanField(default=False)
    # end tests

    '''  '''
    sport = models.CharField(max_length=200, blank=False)
    ex = models.IntegerField(blank=False, default=0)
    position = models.CharField(max_length=200, blank=False)
    sport_org_name = models.CharField(max_length=200, blank=False)
    sport_org_link = models.CharField(max_length=200, blank=False)
    highlights_link = models.CharField(max_length=200, blank=True)
    stats_link = models.CharField(max_length=200, blank=True)
    live_stream_link = models.CharField(max_length=200, blank=True)
    pay_or_not = models.BooleanField(default=False, blank=True)
    hand = models.CharField(max_length=10, blank=True)
    height_inch = models.IntegerField(default=0, blank=True)
    height_cm = models.IntegerField(default=0, blank=True)
    weight_pound = models.IntegerField(default=0, blank=True)
    weight_kg = models.IntegerField(default=0, blank=True)
    league_resolution = models.BooleanField(default=False)
    university_or_club = models.CharField(max_length=10, blank=False)
    national_teem = models.BooleanField(default=False)
    sport_check = models.BooleanField(default=False)
    main_achivment = models.CharField(max_length=200, blank=True)

    '''  '''
    letter = models.CharField(max_length=1500, blank=True)

    def get_id(self):
        return(self.id)

'''
class Achivment(models.Model):
    id = models.IntegerField(primary_key=True)
    title_of_achiv = models.CharField(max_length=75, blank=False, default='')
    type = models.CharField(max_length=9, blank=False, default='')
    date = models.DateField(null=True, blank=False)
    flag = models.BooleanField(default=False)


class Extra_Languages(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25, blank=False)
    level = models.IntegerField(blank=False, default=0)
    flag = models.BooleanField(default=False)

class Teem(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25, blank=True)
    link = models.CharField(max_length=50, blank=True)
    flag = models.BooleanField(default=False)

'''

class Univer_Profile(models.Model):
    id = models.IntegerField(primary_key=True)
    active = models.BooleanField(default=False, blank=False)
    counter_start = Profile.objects.all().count()
    univers_name = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=500, blank=True)
    country = models.CharField(max_length=100, blank=True)
    telegram = models.CharField(max_length=50, blank=True, default='')
    telegram_id = models.CharField(max_length=50, blank=True, default='')

    count_pos = models.IntegerField(default=0)

    is_un = models.BooleanField(default=True, blank=False)

    link = models.CharField(max_length=200, blank=True)

    flag = models.BooleanField(default=False, blank=True)

'''


class Club_Profile(models.Model):
    id = models.IntegerField(primary_key=True)
    active = models.BooleanField(default=False, blank=False)

    club_name = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=500, blank=True)
    country = models.CharField(max_length=100, blank=True)


    count_pos = models.IntegerField(default=0)

    is_cl = models.BooleanField(default=True, blank=False)

    link = models.CharField(max_length=200, blank=True)

    flag = models.BooleanField(default=False, blank=False)


class Open_Position_for_Un(models.Model):
    pass


class Open_Position_for_Cl(models.Model):
    id = models.IntegerField(primary_key=True)
    active = models.BooleanField(default=True, blank=False)

    sport_name = models.CharField(max_length=30, blank=True)
    position = models.CharField(max_length=30, blank=True)
    requirements = models.CharField(max_length=300, blank=True)
    close = models.BooleanField(default=False)


class Tutor(models.Model):
    id = models.IntegerField(primary_key=True)
    active = models.BooleanField(default=False, blank=False)

    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(null=True, blank=False)
    phone_num = models.CharField(max_length=12, blank=True)
    country = models.CharField(max_length=100, blank=True)
    first_language = models.CharField(max_length=100, blank=True)
    second_language = models.CharField(max_length=100, blank=True)
    third_language = models.CharField(max_length=100, blank=False)
    whats_app = models.BooleanField(default=True, blank=True)
    telega = models.CharField(max_length=50, blank=True, default='')
    zoom = models.CharField(max_length=50, blank=True, default='')
    discord = models.CharField(max_length=50, blank=True, default='')
    about_me = models.CharField(max_length=500, blank=False,default='')

'''