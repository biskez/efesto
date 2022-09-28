from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import *
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext
from django.conf.urls.static import static
from home.models import TypeProject, Project, SwiperHomepage, Company, ConfigData, Maps, Error
from navbar.models import Navbar
from json import dumps
from efesto.settings import IMAGES_PATH
from efesto.settings import STYLES_PATH
from efesto.settings import ERROR_IMAGE
from efesto.functions import *

def gallery(request):
    dataError = Error()     
    current_page = 'gallery'
    try:
        configData = getConfigData()
        navbar = getNavbar()

        company = getCompany()
        
        projects = getProjects()

        typeProjects = getTypeProjects()

    except ObjectDoesNotExist:  
        dataError = getDataError(404)
        return render(request, "error.html", {'dataError': dataError,'configData': configData,  'current_page': current_page, 'navbar': navbar,
                                         'company': company, 'STYLES_PATH': STYLES_PATH})

    return render(request, "gallery.html", {'configData': configData, 'current_page': current_page, 'navbar': navbar, 'typeProjects': typeProjects, 'projects': projects,
                                         'company': company, 'STYLES_PATH': STYLES_PATH})

def translate_array(array):
    for index in range(len(array)):
        array[index] = translate_string(array[index])
    return array

def translate_string(string):
    cur_language = get_language()
    try:
        activate(get_language())
        text = gettext(string)
    finally:
        activate(cur_language)
    return text