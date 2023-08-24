from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.utils.text import slugify


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
    name = models.CharField(_("الأسم"), max_length=50, null= True, blank = True)
    subtitle = models.CharField(_("نبذة عنك"), max_length=50, null= True, blank = True)
    doctor = models.CharField(_("دكتور فى"), max_length=50, null= True, blank = True)
    specialist_at = models.CharField(_("متخصص فى"), max_length=50, null= True, blank = True)
    who_i = models.TextField(_("من انا"), max_length=250, null= True, blank = True)
    address = models.CharField(_("المحافظة"), max_length=50, null= True, blank = True)
    address_detail = models.CharField(_("العنوان بالتفصيل"), max_length=50, null= True, blank = True)
    price = models.IntegerField(_("سعر الكشف"),null= True, blank = True)
    working_hours = models.IntegerField(_("عدد ساعات العمل"), null= True, blank = True)
    waiting_time = models.IntegerField(_("وقت الانتظار بالدقائق"), null= True, blank = True)
    phone_number = models.CharField(_("رقم الموبيل"), max_length=50, null= True, blank = True)
    image = models.ImageField(_("الصورة الشخصية"), upload_to='Profile', null= True, blank = True)
    sluge = models.SlugField(_("slug"), null= True, blank = True)

    def save(self , *args, **kwargs):
        if not self.sluge:
            self.sluge = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user= kwargs['instance'])

post_save.connect(create_profile, sender= User)
