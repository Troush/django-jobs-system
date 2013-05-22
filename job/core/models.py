# -*- coding: utf-8 -*-
from django.db import models

MALE = 'MAN'
FEMALE = 'FEMALE'
sex_type = (
    (MALE, u'Мужчина'),
    (FEMALE, u'Женщина')
    )
SMALL = 'S'
MEDIUM = 'M'
BIG = 'L'
CORP = 'XL'
experience_size =  (
    (SMALL,'<1'),
    (MEDIUM,'1-5'),
    (BIG,'5-10'),
    (CORP,'10<'),
    )
EDUCATION_PURE = 'S'
EDUCATION_MINOR = 'M'
EDUCATION_NORAML = 'L'
EDUCATION_MAJOR= 'XL'
education_type = (
    (EDUCATION_PURE, u'Неоконченное среднее'),
    (EDUCATION_MINOR,u'Среднее'),
    (EDUCATION_NORAML,u'Бакалавр'),
    (EDUCATION_MAJOR, u'Магистр')
    )
POSITION_PURE = 'S'
POSITION_MINOR = 'M'
POSITION_NORAML = 'L'
POSITION_MAJOR= 'XL'
position_type = (
(POSITION_PURE, u'Младший специалист'),
(POSITION_MINOR,u'Специалист'),
(POSITION_NORAML,u'Старший специалист'),
(POSITION_MAJOR, u'Начальник отдела')
)

# Create your models here.
class Company(models.Model):
    SMALL = 'S'
    MEDIUM = 'M'
    BIG = 'L'
    CORP = 'XL'
    company_size =  (
        (SMALL,'<20'),
        (MEDIUM,'20-50'),
        (BIG,'50-100'),
        (CORP,'100<'),
        )
    name = models.CharField(max_length=200,unique=True,db_index=True)
    email = models.EmailField(unique=True,db_index=True)
    size = models.CharField(max_length=10,choices=company_size,default=SMALL,db_index=True)
    about = models.TextField(blank=True)
    phone = models.CharField(max_length=24)
    site = models.CharField(max_length=128)
    create_date = models.DateTimeField('date created')
    class Meta:
        verbose_name = u'Компания'
        verbose_name_plural = u'Компании'

    def __unicode__(self):
        return self.name

    def get_name(self):
        return self.name


class JobsCategory(models.Model):
    name = models.CharField(max_length=250,unique=True,db_index=True)
    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'
    def __unicode__(self):
        return self.name

class Candidate(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=250,db_index=True)
    sex = models.CharField(max_length=12,db_index=True,choices=sex_type,default=MALE)
    create_date = models.DateTimeField('date created',auto_now_add=True, blank=True)
    experience = models.CharField(max_length=2,db_index=True, choices=experience_size)
    phone = models.CharField(max_length=24)
    education = models.CharField(max_length=2, db_index=True, choices=education_type)
    location = models.CharField(max_length=250)
    more_info = models.TextField(blank=True)
    position = models.CharField(max_length=250,db_index=True, choices=position_type)
    looking_for = models.ForeignKey('JobsCategory',default='1')
    class Meta:
        verbose_name=u'Кандидат'
        verbose_name_plural=u'Кандидаты'

    def __unicode__(self):
        return self.name

    def get_name(self):
        return self.name

class Vacancy(models.Model):
    title = models.CharField(max_length=250,db_index=True)
    company = models.ForeignKey('Company',default='1',db_index=True)
    jobs_category = models.ForeignKey('JobsCategory',default='1')
    location = models.CharField(max_length=250,db_index=True)
    keyword = models.CharField(max_length=250,db_index=True)
    is_checked = models.BooleanField()
    sex = models.CharField(max_length=12,db_index=True,choices=sex_type,default=MALE)
    education = models.CharField(max_length=2, db_index=True, choices=education_type)
    experience = models.CharField(max_length=2,db_index=True, choices=experience_size)
    position = models.CharField(max_length=250,db_index=True, choices=position_type)

    class Meta:
        verbose_name = u'Вакансия'
        verbose_name_plural = u'Вакансии'

    def get_name(self):
        return self.title
