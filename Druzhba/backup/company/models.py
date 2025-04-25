from django.db import models
from common.models import BaseAbstractModel


class Company(BaseAbstractModel):
    owner = models.ForeignKey('user.User', verbose_name='Owner', related_name='companies', on_delete=models.CASCADE)

    title = models.CharField('Title', max_length=255)
    scope = models.CharField('Scope', max_length=255)
    phone = models.CharField('Phone', max_length=31)
    email = models.EmailField('Email')

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


class CompanyMember(BaseAbstractModel):
    company = models.ForeignKey('company.Company', verbose_name='Company',
                                related_name='company_members', on_delete=models.CASCADE)
    user = models.ForeignKey('user.User', verbose_name='User',
                             related_name='company_members', on_delete=models.CASCADE)

    is_admin = models.BooleanField('IsAdmin', default=False)

    class Meta:
        verbose_name = 'Company member'
        verbose_name_plural = 'Company members'
