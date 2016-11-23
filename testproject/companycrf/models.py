from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Company(models.Model):
    """

    """
    cname = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s %s' % (self.id, self.cname)
class Param(models.Model):
    """

    """
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    Param1 = models.FloatField(null=True, blank=True)
    Param2 = models.FloatField(null=True, blank=True)
    Param3 = models.FloatField(null=True, blank=True)
    Param4 = models.FloatField(null=True, blank=True)
    Param5 = models.FloatField(null=True, blank=True)
    Param6 = models.FloatField(null=True, blank=True)
    Param7 = models.FloatField(null=True, blank=True)
    Param8 = models.FloatField(null=True, blank=True)
    Param9 = models.FloatField(null=True, blank=True)
    Param10 = models.FloatField(null=True, blank=True)
    month_num = models.IntegerField()


    def __unicode__(self):
        return u'%s %s %s %s %s %s %s %s %s %s %s %s %s ' % (self.id, self.company, self.Param1, self.Param2,
                                   self.Param3, self.Param4, self.Param5, self.Param6, self.Param7, self.Param8,
                                   self.Param9, self.Param10, self.month_num)

