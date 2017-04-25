from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.db import models

from scout.users.models import User


TEMPLATE_CHOICES = (
    ('emails/generic_invite.html', 'Generic'),
)


# Create your models here.
class Email(models.Model):
    subject = models.CharField(max_length=255)
    from_email = models.CharField(max_length=255)
    to_email = models.CharField(max_length=255, blank=True)
    template = models.CharField(max_length=255, choices=TEMPLATE_CHOICES, default='emails/generic_invite.html')

    class Meta:
        abstract = True

    def send(self, context):
        html = render_to_string(self.template, context)
        text = strip_tags(html)
        msg = EmailMultiAlternatives(self.subject, text, self.from_email, [self.to_email])
        msg.attach_alternative(html, "text/html")
        msg.send()
        return


class InvitationEmail(Email):
    user = models.OneToOneField(User)
    from_email = "invitations@totallacrossenetwork.com"

    def send(self):
        password = User.objects.make_random_password()
        self.user.set_password(password)
        self.user.save()
        context = {'user': self.user, 'password': password}
        super(InvitationEmail, self).send(context)

    def save(self):
        print("Email save called")
        self.to_email = self.user.email
        self.send()
        super(InvitationEmail, self).save()

    def __str__(self):
        return self.user.username
