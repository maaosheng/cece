from django import forms
from django.forms import ModelForm
from django.forms import widgets
from app01.models import  *

# class UserForm(forms.Form):
#     name = forms.CharField(
#         label='姓名',
#         max_length=8,
#         error_messages={
#             'required':'内容不能为空',
#             'max_length':'最长不能超过7位',
#             'min_length':'最短不能少于2位'
#         },
#         widget=widgets.TextInput(
#             attrs={'class':'form-control'}
#         )
#     )
#
#     age = forms.IntegerField(
#         label='年宁',
#         max_value=1000,
#         error_messages={
#             'required': '内容不能为空',
#             'max_value':'不能大于1000',
#             'min_avalue':'不能小于0'
#         },
#         widget=widgets.TextInput(
#             attrs={'class': 'form-control'}
#         )
#     )
#     email = forms.EmailField(
#         label='邮箱',
#         max_length=36,
#         error_messages={
#             'required': '内容不能为空',
#             'max_length': '最长不能超过36位',
#             'min_length': '最短不能少于2位',
#             'invalid':'格式错误'
#         },
#         widget=widgets.TextInput(
#             attrs={'class': 'form-control'}
#         )
#     )
#     address= forms.CharField(
#         label='地址',
#         max_length=36,
#         error_messages={
#             'required': '内容不能为空',
#             'max_length': '最长不能超过36位',
#             'min_length': '最短不能少于2位'
#         },
#         widget=widgets.TextInput(
#             attrs={'class': 'form-control'}
#         )
#     )
class UserForm(ModelForm):
    class Meta:
        model=Userinfo
        fields='__all__'
        error_messages ={
               'name':{
                   'required': '内容不能为空',
                   'max_length':'最长不能超过7位',
                    'min_length':'最短不能少于2位'
               },
               'age':{
                   'required':'内容不能为空',
                   'invalid':'格式错误',
                   'max_value':'最大不能超过1000',
               },
               'email':{
                   'required':'内容不能为空',
                   'invalid':'格式错误',
                   'max_length':'长度不能超过18'
               }
           }
        labels={
            'name':'SB1234555'
        },
        widgets={
            'name':widgets.TextInput(
                # attrs={
                #     'class':'form-control'
                # }
            )
        }
