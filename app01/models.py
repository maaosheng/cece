from django.db import models

# Create your models here.
class Userinfo(models.Model):
       name = models.CharField(max_length=36,verbose_name='姓名')
       age = models.IntegerField(verbose_name='年龄')
       email = models.EmailField(max_length=36,verbose_name='邮件')
       address = models.CharField(max_length=128,verbose_name='地址')

       def __str__(self):
              return self.name
       class Meta:
              unique_together=(
                     ('name','email')
              )
              verbose_name = '用户表'
              verbose_name_plural = verbose_name
# class (models):
# # #