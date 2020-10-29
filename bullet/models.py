from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name="name")
    phonenumber = models.CharField(
        max_length=20, blank=True, verbose_name="phonenumber")
    email = models.CharField(max_length=100, blank=True, verbose_name="email")
    address = models.CharField(
        max_length=200, verbose_name="address", blank=True)
    message = models.TextField(blank=True, verbose_name="message")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "customer"
        verbose_name_plural = "customers"


class Partner(models.Model):
    name = models.CharField(max_length=100, verbose_name="name")
    logo = models.ImageField(upload_to="logo", verbose_name="logo")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "partner"
        verbose_name_plural = "partners"


class Testimonial(models.Model):
    author = models.CharField(max_length=100, verbose_name="author")
    occupation = models.CharField(max_length=100, verbose_name="occupation")
    quote = models.TextField(verbose_name="quote")
    avatar = models.ImageField(upload_to="avatar", verbose_name="avatar")

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = "testimonial"
        verbose_name_plural = "testimonials"


class GalleryImageCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name="title of category")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"


class Gallery(models.Model):
    category = models.ForeignKey(
        GalleryImageCategory, on_delete=models.CASCADE,
        related_name="image", verbose_name="category")
    title = models.CharField(max_length=50, verbose_name="title")
    description = models.CharField(max_length=100, verbose_name="description")
    image = models.ImageField(upload_to="gallery", verbose_name="image")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "image"
        verbose_name_plural = "images"


class Service(models.Model):
    title = models.CharField(max_length=50, verbose_name="title")
    description = models.TextField(verbose_name="description")
    image = models.ImageField(upload_to="service", verbose_name="image")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "service"
        verbose_name_plural = "services"
