from django.db import models

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    
class Order(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    service_name = models.ForeignKey(Service, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Service_description(models.Model):
    image = models.ImageField(upload_to = 'media/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    service_typ = models.ForeignKey(Service, on_delete = models.CASCADE)
    def __str__(self):
        return self.title


class Portfolio(models.Model):
    image = models.ImageField(upload_to = 'media/')
    url_link = models.URLField()
    service_name = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return self.service_name.title
