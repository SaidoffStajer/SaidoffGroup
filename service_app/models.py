from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=125)

    def __str__(self):
        return self.title
    

class ServiceDescription(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='descriptions')  
    image = models.ImageField(upload_to='service_desc')
    title = models.CharField(max_length=125)
    description = models.TextField()

    def __str__(self):
        return self.service.title
    

class Order(models.Model):
    name = models.CharField(max_length=125)
    phone_number = models.CharField(max_length=125)
    service_name= models.ForeignKey(Service,on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio')
    url_link = models.URLField()
    service_name = models.ForeignKey(Service,on_delete=models.CASCADE)

    def __str__(self):
        return f'Project for {self.service_name.title}'
    
    
