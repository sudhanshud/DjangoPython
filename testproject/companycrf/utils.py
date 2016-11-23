import models
import math
import numpy
import logging
import sys

logger = logging.getLogger(__name__)


def get_com_names():
    """
    This method is used to get the list of all companies.
    :return:
    """
    try:
        companies = models.Company.objects.all()
        company_tuples = [(company.id, company.cname) for company in companies] + [(0L, u'---Select Company---')]
        company_tuples = tuple(company_tuples[::-1])
        return company_tuples
    except:
        logger.error("Exception in Get Company Name.")
        exception = sys.exc_info()
        logger.error("Exception in Get Company Name {}".format(str(exception[0])))
        logger.error("Exception in Get Company Name {}".format(str(exception[1])))
        logger.error("Exception in Get Company Name {}".format(str(exception[2])))

def get_months():
    """
    This method is used to get the list of months

    :return:
    """
    months = (('0', '---Select Month---'),
             ('1', '1'),
             ('2', '2'),
             ('3', '3'),
             ('4', '4'),
             ('5', '5'),
             ('6', '6'),
              ('7', '7'),
              ('8', '8'),
              ('9', '9'),
              ('10', '10'),
              ('11', '11'),
              ('12', '12'))
    return months

def company_rating(company, month):
    """

    :param company:
    :param month:
    :return:
    """
    try:
        contt = {'a1':7.1,'a2':1.2,'a3':3.1,'a4':0.9,'a5':4.5,'a6':0.28,'a7':0.56,'a8':0.81,'a9':1.6,'a10':2}
        contt_sum = sum(contt.values())
        parms = models.Param.objects.filter(company=company, month_num=month)[0]
        company_rating = (parms.Param1*contt['a1']+parms.Param2*contt['a2']+parms.Param3*contt['a3']
                          +parms.Param4*contt['a4']+parms.Param5*contt['a5']+parms.Param6*contt['a6']
                          +parms.Param7*contt['a7']+parms.Param8*contt['a8']+parms.Param9*contt['a9']
                          +parms.Param10*contt['a10'])/contt_sum
        return company_rating
    except:
        logger.error("Exception in Company Rating.")
        exception = sys.exc_info()
        logger.error("Exception in Company Rating {}".format(str(exception[0])))
        logger.error("Exception in Company Rating {}".format(str(exception[1])))
        logger.error("Exception in Company Rating {}".format(str(exception[2])))


def company_ratings_per_months(month):
    """

    :param month:
    :return:
    """
    try:
        list_crt = []
        companies = models.Company.objects.all()
        for company in companies:
            crt = company_rating(company.id, month)
            list_crt.append(crt)
        return list_crt
    except:
        logger.error("Exception in Company Ratings Per Month.")
        raise


def crs(company, month):
    """

    :return:
    """
    try:
        x = company_rating(company, month)
        crt_list_per_month = company_ratings_per_months(month)
        mu = numpy.average(crt_list_per_month)
        sigma = numpy.std(crt_list_per_month)
        y = cdf(x, mu, sigma)
        if y > 1:
            y=1
        return y*100
    except:
        logger.error("Exception in Company Relative Score Per Month.")
        raise

def cdf(x, mu, sigma):
    """

    :param x:
    :param mu:
    :param sigma:
    :return:
    """
    try:
        t = x - mu
        cdf = 0.5 * math.erf(-t/(sigma*math.sqrt(2.0)))
        return cdf
    except:
        logger.error("Exception in CDF.")
        raise

def crs_data(company):
    """

    :param month:
    :return:
    """
    try:
        dic_crsdata = {}
        for month in range(1, 13):
            com_crs = crs(company, month)
            dic_crsdata[month] = com_crs
        return dic_crsdata
    except:
        logger.error("Exception in CRS DATA.")
        raise




