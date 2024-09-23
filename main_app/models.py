from django.db import models

class WhyUs(models.Model):
    title = models.CharField(max_length=125)
    description = models.TextField()

    def __str__(self):
        return self.title
    

class Partners(models.Model):
    image = models.ImageField(upload_to='partners')
   
    def __str__(self):
        return self.id
    

class Team(models.Model):
    name = models.CharField(max_length=125)
    image = models.ImageField(upload_to='team')
    profession = models.CharField(max_length=125)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Subscribe(models.Model):
    full_name = models.CharField(max_length=125)
    phone_number = models.CharField(max_length=125)
    is_checked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
    
class Certificate(models.Model):
    title = models.CharField(max_length=125)
    image = models.ImageField(upload_to='subscribe')
    description  = models.TextField()
   

    def __str__(self):
        return self.title
    
class FeedBack(models.Model):
    name = models.CharField(max_length=125)
    comment = models.TextField()
    image = models.ImageField(upload_to='feedback')
    profession = models.CharField(max_length=125)
    

    def __str__(self):
        return self.name
    

class FAQCategory(models.Model):
    title = models.CharField(max_length=125)

    def __str__(self):
        return self.title
    
class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()
    faq_page = models.ForeignKey(FAQCategory,on_delete=models.CASCADE)

    def __str__(self):
        return self.faq_page.title
    
class Feature(models.Model):
    title = models.CharField(max_length=125)
    tick = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class PricePlan(models.Model):
    title = models.CharField(max_length=125)
    price = models.IntegerField()
    limit_date = models.CharField(max_length=125)
    limit_user = models.CharField(max_length=125)
    features = models.ManyToManyField(Feature)

    def __str__(self):
        return self.title




    


    







