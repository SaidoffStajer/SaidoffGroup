from django.db import models


# Create your models here.

class Faq_category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Faq(models.Model):
    questions = models.TextField()
    answers = models.TextField()
    faq_page = models.CharField(max_length=50)
    faq = models.ForeignKey(Faq_category, on_delete = models.CASCADE)

    def __str__(self):
        return self.questions

class Feedback(models.Model):
    name = models.CharField(max_length=50)
    comment = models.TextField()
    profession = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name

class WhyUs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Partners(models.Model):
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.image

class Team(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/')
    profession = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self):
        return self.name

class Subscribe(models.Model):
    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    is_checked = models.BooleanField(default=False)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.full_name

class Certificate(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.title







