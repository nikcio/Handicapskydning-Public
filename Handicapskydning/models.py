from django.db import models
from django.utils.timezone import now
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.


class News(models.Model):
    title = models.CharField(verbose_name="Nyhed", max_length=255)
    date = models.DateField(verbose_name="Dato", default=now())

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Nyhed"
        verbose_name_plural = "Nyheder"


class Activity(models.Model):
    region = models.CharField(verbose_name="Region", max_length=255)
    city = models.CharField(verbose_name="By", max_length=255)
    rank = models.CharField(verbose_name="Klasse", max_length=255)
    date = models.DateField(verbose_name="Dato", default=now())

    def __str__(self):
        return F"{self.region}, {self.city}, {self.rank}, {self.date}"

    class Meta:
        verbose_name = "Aktivitet"
        verbose_name_plural = "Aktiviteter"


def get_file_results(instance, filename):
    return 'static/Results/{0}'.format(filename)


class Results(models.Model):
    competition = models.CharField(verbose_name="Konkurrance", max_length=255)
    file = models.FileField(upload_to=get_file_results, verbose_name="fil")

    def __str__(self):
        return self.competition

    class Meta:
        verbose_name = "Resultat"
        verbose_name_plural = "Resultater"


@receiver(post_delete, sender=Results)
def results_file_delete(sender, instance, **kwargs):
    instance.file.delete(False)


class Department(models.Model):
    name = models.CharField(verbose_name="Afdeling", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Bestyrelse"
        verbose_name_plural = "Bestyrelser"


def get_profile_picture(instance, filename):
    return 'static/Pictures/{0}/{1}'.format(instance.name, filename)


class StaffMember(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="Afdeling")
    name = models.CharField(verbose_name="Navn", max_length=255)
    email = models.EmailField(verbose_name="Email", max_length=255)
    phone = models.PositiveIntegerField(verbose_name="Tlf")
    address = models.CharField(verbose_name="Adresse", max_length=255)
    city = models.CharField(verbose_name="By", max_length=255)
    postal_code = models.PositiveSmallIntegerField(verbose_name="Post nummer")
    title = models.CharField(verbose_name="Titel", max_length=510)
    profile_image = models.ImageField(upload_to=get_profile_picture, default='static/assets/images/mbr-510x510.jpg')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Bestyrelses medlem"
        verbose_name_plural = "Bestyrelses medlemmer"


@receiver(post_delete, sender=StaffMember)
def picture_delete(sender, instance, **kwargs):
    if instance.profile_image != 'static/assets/images/mbr-510x510.jpg':
        instance.profile_image.delete(False)


class Club(models.Model):
    name = models.CharField(verbose_name="Navn", max_length=255)
    city = models.CharField(verbose_name="By", max_length=255)
    link = models.URLField(verbose_name="Hjemmeside", max_length=2083)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Klub"
        verbose_name_plural = "Klubber"


def get_file(instance, filename):
    return 'static/Dokuments/{0}/{1}'.format(instance.name, filename)


class Documents(models.Model):
    name = models.CharField(max_length=255, verbose_name="Navn")
    file = models.FileField(upload_to=get_file)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Dokument"
        verbose_name_plural = "Dokumenter"


@receiver(post_delete, sender=Documents)
def dokument_file_delete(sender, instance, **kwargs):
    instance.file.delete(False)


def get_lane_picture(instance, filename):
    return 'static/Pictures/Lanes/{0}'.format(filename)


class Lane(models.Model):
    picture = models.ImageField(upload_to=get_lane_picture)

    def __str__(self):
        return F"Billede {self.id}"

    class Meta:
        verbose_name = "Bane billede"
        verbose_name_plural = "Bane billeder"


@receiver(post_delete, sender=Lane)
def lane_picture_delete(sender, instance, **kwargs):
    instance.picture.delete(False)


def get_link_picture(instance, filename):
    return 'static/Pictures/Links/{0}'.format(filename)


class Link(models.Model):
    name = models.CharField(max_length=255, verbose_name="Navn")
    picture = models.ImageField(upload_to=get_link_picture)
    link = models.URLField(max_length=2083, verbose_name="Link")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Links"


@receiver(post_delete, sender=Link)
def lane_picture_delete(sender, instance, **kwargs):
    instance.picture.delete(False)


class Collections(models.Model):
    name = models.CharField(max_length=255, verbose_name="Samling")
    year = models.PositiveSmallIntegerField(verbose_name="Årstal")

    def __str__(self):
        return F"{self.name} - {self.year}"

    class Meta:
        verbose_name = "Samling"
        verbose_name_plural = "Samlinger"


def get_collection_image(instance, filename):
    return 'static/Pictures/collcetions/{0}/{1}'.format(instance.collection.name, filename)


class CPictures(models.Model):
    collection = models.ForeignKey(Collections, on_delete=models.CASCADE, verbose_name="Samling")
    picture = models.ImageField(upload_to=get_collection_image, verbose_name="Billede")

    class Meta:
        verbose_name = "Billede"
        verbose_name_plural = "Billeder"


@receiver(post_delete, sender=CPictures)
def lane_picture_delete(sender, instance, **kwargs):
    instance.picture.delete(False)
