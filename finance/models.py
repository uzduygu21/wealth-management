from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    pass

class Contact(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    question = models.TextField()
    contactdate = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "question": self.question,
            "contactdate": self.contactdate.strftime("%b %-d %Y, %-I:%M %p")
        }

class Account(models.Model):
    accountnum = models.CharField(max_length=64)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    bank = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="accountowner")
    linkdate = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        return {
            "id": self.id,
            "accountnum": self.accountnum,
            "amount": self.amount,
            "bank": self.bank,
            "user": self.user,
            "linkdate": self.linkdate.strftime("%b %-d %Y, %-I:%M %p")
        }

class Quiz(models.Model):
    score = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="quiztaker")
    quizdate = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        return {
            "id": self.id,
            "score": self.score,
            "user": self.user,
            "quizdate": self.quizdate.strftime("%b %-d %Y, %-I:%M %p")
        }
