from django.db import models
import random
import string


def url_generator():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))


class Training(models.Model):
    name = models.CharField(max_length=64)
    start_date = models.DateField()
    end_date = models.DateField()
    training_email = models.EmailField()
    training_url = models.CharField(max_length=64, default=url_generator)

    def __str__(self):
        return f"{self.name}"


class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    user_email = models.EmailField()
    phone = models.CharField(max_length=16)
    address = models.CharField(max_length=64)
    post_code = models.CharField(max_length=6)
    city = models.CharField(max_length=32)
    consent_1 = models.CharField(max_length=16)
    consent_2 = models.CharField(max_length=16)
    consent_3 = models.CharField(max_length=16)
    user_url = models.CharField(max_length=64, default=url_generator)
    email_confirmed = models.BooleanField(default=False)
    training = models.ForeignKey(Training, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
