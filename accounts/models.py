from email import utils
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Profile(models.Model):
    user = models.OneToOneField(
        User, verbose_name=_(""), on_delete=models.CASCADE)
    name = models.CharField(_("الأسم: "), max_length=50)
    who_i = models.TextField(_("من انا: "))
    price = models.IntegerField(_("سعر الكشف: "))

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return self.name
