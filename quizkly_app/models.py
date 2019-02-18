from django.db import models

# for all people who signed up mailing list

class Contact(models.Model):

    submitted = models.DateTimeField(auto_now_add = True)
    email = models.CharField(max_length = 30)
    beta = models.BooleanField()

    class Meta:

        ordering = ('submitted',)
