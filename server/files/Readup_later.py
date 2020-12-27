# from django.db import models,signals
# from django.contrib.auth.models import User

# class Vault(models.Model):
#     salon = models.ForeignKey(Salon,  on_delete=models.CASCADE, null=False, unique=False)
#     cash = models.PositiveIntegerField()

# class Salon(models.Model):
#     salon_ismi = models.CharField(max_length=25,unique=False)
#     adres = models.CharField(max_length=255, unique=False)
#     ulke = models.CharField(max_length=25, unique=False)
#     sehir = models.CharField(max_length=24, unique=False)
#     kasa = models.PositiveIntegerField(blank=True, unique=False)
#     class Meta:
#         ordering = ('-pk',)
#         verbose_name_plural = "Salonlar"

#     def __unicode__(self):
#         return u'%s' % self.pk
#     def __str__(self):
#         return self.salon_ismi
#     def get_absolute_url(self):
#         return reverse('kentyonetim_salon_detail', args=(self.pk,))

#     def create_vault(self, sender, instance, created, **kwargs):
#         """Create Vault Model for every new Salon Model."""
#         if created:
#             Vault.objects.create(salon=self.salon_ismi,)

# signals.post_save.connect(Salon.create_vault, sender=Salon, weak=False,
#                               dispatch_uid='models.create_Vault')