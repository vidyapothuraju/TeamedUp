"""views of django"""
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render
from django.shortcuts import redirect

from .models import Profile

from .forms import user_main_form, user_letter_form


from TeamedUp.Web_to_bot import message_sender



def web():
    """social"""
    return [
        {
            # facebook
            'link': 'https://www.facebook.com/Teamed-Up-363186321537325',
            'class': 'feather feather-facebook fea icon-sm fea-social',
            'path': 'M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z',
            'x': '-1000',
            'y': '-1000',
            'width': '-1000',
            'height': '-1000',
            'rx': '-1000',
            'ry': '-1000',
            'x1': '-1000',
            'y1': '-1000',
            'x2': '-1000',
            'y2': '-1000',
            'cx': '-1000',
            'cy': '-1000',
            'r': '-1000',
        },
        {
            # instagram
            'link': 'https://www.instagram.com/teamedup_recruitment/ ',
            'class': "feather feather-instagram fea icon-sm fea-social",
            'path': "M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z",
            'x': '2',
            'y': '2',
            'width': '20',
            'height': '20',
            'rx': '5',
            'ry': '5',
            'x1': '17.5',
            'y1': '6.5',
            'x2': '17.51',
            'y2': '6.5',
            'cx': '',
            'cy': '',
            'r': '',
        },

    ]


def start_user_link():
    """Info for start page"""
    return {
        'web': web(),

    }



def start_user(request):
    """first page for user"""
    data = start_user_link()
    data['success']=' '
    #print('\n\n',Profile.objects.all().count(),'\n\n')
    return render(request, 'start.html', data)


def create_user_profile(biscuits):
    """create profile """
    Profile.objects.create(biscuits=biscuits)


@transaction.atomic
def update_profile_user(request):
    """ update profile user """
    data = {}
    #t=request.COOKIES['csrftoken']
    #if len(Profile.objects.filter(biscuits=t))==0:
    #    create_user_profile(t)
    if request.method == 'POST':
        user_form = user_main_form(request.POST)
        if user_form.is_valid() \
                and(len(Profile.objects.all().filter(email=request.POST['email']))==0)\
                and(len(Profile.objects.all().filter(insta=request.POST['insta']))==0)\
                and(len(Profile.objects.all().filter(telega=request.POST['telega']))==0):

            user_form.save()
            data = start_user_link()
            t = Profile.objects.latest('id').get_id()
            message_sender(t, request.POST['sport'])
            data['success']="Registration is success"
            return render(request, 'start.html', data)
            # messages.success(request, ('Ваш профиль был успешно обновлен!'))
        else:
            if not(len(Profile.objects.all().filter(email=request.POST['email']))==0):
                data['email_error']="This email address we already know."
            if not (len(Profile.objects.all().filter(insta=request.POST['insta']))==0):
                data['insta_error'] = "This instagram we already know."
            if not (len(Profile.objects.all().filter(telega=request.POST['telega']))==0):
                data['telega_error'] = "This telegram we already know."
            data['error']= user_form.errors
            data['user_form'] = user_form
            return render(request, 'accounts/prof_set.html', data)



    user_form = user_main_form()
    data['user_form'] = user_form
    return render(request, 'accounts/prof_set.html', data)


@login_required
@transaction.atomic
def update_letter(request):
    """ update letter """

    data = {}
    if request.method == 'POST':
        letter_form = user_letter_form(request.POST, instance=request.user.profile)

        flag = True

        if letter_form.is_valid():
            letter_form.save()
        else:
            data['error'] = '1'

            data['letter_form'] = letter_form
            flag = False

        if flag:
            return redirect('profile')

        return render(request, '/accounts/prof_letter.html', data)

    letter_form = user_letter_form(instance=request.user.profile)

    data['letter_form'] = letter_form

    return render(request, 'accounts/prof_letter.html', data)