from django.core.mail import send_mail
from django.shortcuts import render
from django.views import View
from django.core.exceptions import ObjectDoesNotExist

import RODO_Form.local_settings
from rodo_app.models import Training, User
from rodo_app.forms import RodoForm
from RODO_Form.settings import EMAIL_HOST_USER, BASE_URL


class FormView(View):

    def get(self, request, form_url):
        error = ""
        try:
            Training.objects.get(training_url=form_url)
        except ObjectDoesNotExist:
            error = "Brak szkolenia o takim adresie"
        form = RodoForm()
        return render(request, "form.html", {'form': form, 'form_url': form_url, 'error': error})

    def post(self, request, form_url):
        User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            user_email=request.POST['email'],
            phone=request.POST['phone'],
            address=request.POST['address'],
            post_code=request.POST['post_code'],
            city=request.POST['city'],
            consent_1=request.POST['consent_1'],
            consent_2=request.POST['consent_2'],
            consent_3=request.POST['consent_3'],
            training=Training.objects.get(training_url=form_url)
        )
        recipient = request.POST['email']
        url = User.objects.get(user_email=request.POST['email'],
                               training=Training.objects.get(training_url=form_url)).user_url
        subject = "Potwierdzenie adresu e-mail"
        message = f"Potwierdź adres email klikając w link: {BASE_URL}/confirm/{url}"
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        return render(request, "form_finished.html")


class ConfirmationView(View):

    def get(self, request, url):
        error = ""
        try:
            user = User.objects.get(user_url=url)
            user.email_confirmed = True
            user.save()

            training = Training.objects.get(pk=user.training.pk)
            subject = "Nowy uczestnik szkolenia"
            message = f"Użytkownik potwierdził udział w szkoleniu.\n\n\
                        Dane szkolenia:\n\
                        Nazwa szkolenia: {training.name}\n\
                        Data szkolenia: {training.start_date} - {training.end_date}\n\n\
                        Dane uczestnika:\n\
                        Imię i nazwisko: {user.first_name} {user.last_name}\n\
                        Adres e-mail: {user.user_email}\n\
                        Numer telefonu: {user.phone}\n\
                        Adres: {user.post_code}, {user.city}, {user.address}\
                        "
            send_mail(subject, message, EMAIL_HOST_USER, [training.training_email], fail_silently=False)

        except ObjectDoesNotExist:
            error = "Brak emaila do potwierdzenia"
        return render(request, "email_confirmed.html", {'error': error})


class FormFinishedView(View):

    def get(self, request):
        print(RODO_Form.local_settings.SECRET_KEY)
        return render(request, "form_finished.html")
