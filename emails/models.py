from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.db import models



TEMPLATE_CHOICES = (
    ('emails/default_email.html', 'Generic'),
)


# Create your models here.
class Email(models.Model):
    subject = models.CharField(max_length=255)
    from_email = models.CharField(max_length=255)
    to_email = models.CharField(max_length=255, blank=True)
    template = models.CharField(max_length=255, choices=TEMPLATE_CHOICES, default='emails/default_email.html')

    class Meta:
        abstract = True

    def send(self, context):
        html = render_to_string(self.template, context)
        text = strip_tags(html)
        msg = EmailMultiAlternatives(self.subject, text, self.from_email, [self.to_email])
        msg.attach_alternative(html, "text/html")
        msg.send()
        return



class DefaultEmail(Email):
    from_email = "default@example.com"

    def save(self):
        context = {'text': 'HelloWorld'}
        self.send(context)
        super(DefaultEmail, self).save()

    def __str__(self):
        return self.to_email

# Create custom Email models here.

