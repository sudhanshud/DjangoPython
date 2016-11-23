from django.shortcuts import render
from django.http import *
from django.template import RequestContext
from django.shortcuts import render_to_response
import forms
import models
import utils
import sys
import logging

logger = logging.getLogger(__name__)

def home(request):
    """
    View to handle Pushnotification home page request.
    :param request:
    :return:
    """
    try:
        logger.info("In Home View.")
        return render_to_response('home.html', context_instance=RequestContext(request))
    except:
        logger.error("Exception in home.")
        exception = sys.exc_info()
        logger.error("Exception in home {}".format(str(exception[0])))
        logger.error("Exception in home {}".format(str(exception[1])))
        logger.error("Exception in home {}".format(str(exception[2])))

def companyrating(request):
    """

    :param request:
    :return:
    """
    try:
        logger.info("In Company Rating View.")
        if request.method == 'GET':
            form = forms.CompanyRating()
            return render(request, 'companyrating.html', {'form': form})
        if request.method == 'POST':
            form = forms.CompanyRating(request.POST)
            if form.is_valid():
                form_data = form.cleaned_data
                companyrating = utils.company_rating(form_data['Company_name'], form_data['Month'])
                company = models.Company.objects.filter(id=int(form_data['Company_name']))[0]
                return HttpResponse('Company Rating of {} for month {} is {}'.format(company.cname,
                                                                                        form_data['Month'], str(companyrating)))
            else:
                return HttpResponse('Not Valid Form Data')

    except:
        logger.error("Exception in home.")
        exception = sys.exc_info()
        logger.error("Exception in home {}".format(str(exception[0])))
        logger.error("Exception in home {}".format(str(exception[1])))
        logger.error("Exception in home {}".format(str(exception[2])))

def companycrs(request):
    """

    :param request:
    :return:
    """
    try:
        logger.info("In Company Rating View.")
        if request.method == 'GET':
            form = forms.CompanyRating()
            return render(request, 'companyralative.html', {'form': form})
        if request.method == 'POST':
            form = forms.CompanyRating(request.POST)
            if form.is_valid():
                form_data = form.cleaned_data
                crs = utils.crs(form_data['Company_name'], form_data['Month'])
                company = models.Company.objects.filter(id=int(form_data['Company_name']))[0]
                return HttpResponse('CRS of {} for month {} is {}'.format(company.cname,
                                                                                     form_data['Month'],
                                                                                     str(crs)))
            else:
                return HttpResponse('Not Valid Form Data')


    except:
        logger.error("Exception in home.")
        exception = sys.exc_info()
        logger.error("Exception in home {}".format(str(exception[0])))
        logger.error("Exception in home {}".format(str(exception[1])))
        logger.error("Exception in home {}".format(str(exception[2])))

def companycrsgraph(request):
    """

    :param request:
    :return:
    """
    try:
        logger.info("In Company Rating View.")
        if request.method == 'GET':
            form = forms.CrsData()
            return render(request, 'crsdata.html', {'form': form})
        if request.method == 'POST':
            form = forms.CrsData(request.POST)
            if form.is_valid():
                form_data = form.cleaned_data
                crs_data = utils.crs_data(form_data['Company_name'])
                company_name = models.Company.objects.filter(id=int(form_data['Company_name']))[0].cname
                return render_to_response('company_crs_data.html',
                                          {'crs_data': crs_data, 'company_name': company_name,},
                                          context_instance=RequestContext(request))
            else:
                return HttpResponse('Not Valid Form Data')
    except:
        logger.error("Exception in home.")
        exception = sys.exc_info()
        logger.error("Exception in home {}".format(str(exception[0])))
        logger.error("Exception in home {}".format(str(exception[1])))
        logger.error("Exception in home {}".format(str(exception[2])))