from django.utils.translation import get_language, activate, gettext
from django.core.exceptions import *
from django.http import HttpResponse
from home.models import TypeProject, Project, SwiperHomepage, Company, ConfigData, Maps, Error
from navbar.models import Navbar
from team.models import Team, Role
from services.models import Service, Subservice
from news.models import News
from efesto.settings import IMAGES_PATH, STYLES_PATH, MARKERS_PATH, PROJECTS_PATH, TYPEPROJECT_PATH, ERROR_IMAGE, GMAPS_LINK, TEAM_PATH, SERVICES_PATH, NEWS_PATH, PROJECT_GALLERY_PATH
from django.shortcuts import render
from json import dumps
from efesto.translation import *

def getConfigData():
    configData = ConfigData.objects.get(id=1)
    configData.title = translate_string(configData.title)
    configData.favicon = IMAGES_PATH+configData.favicon
    configData.icon = IMAGES_PATH+configData.icon
    configData.icon_footer = IMAGES_PATH+configData.icon_footer
    return configData

def getConfigMaps():
    maps = Maps.objects.get(id=1)
    maps.gmaps = maps.gmaps+''+maps.gmaps_api_key+'&language='+get_language()+'&callback=initMap'#&libraries=&v=weekly
    maps.marker = MARKERS_PATH+maps.marker
    maps.cluster_path = IMAGES_PATH+maps.cluster_path
    return maps

def getNavbar():
    navbar = Navbar.objects.all().order_by('orderId')
    for block in navbar:
        block = translate_string(block.name)
    return navbar

def getSwipers():
    swipers = SwiperHomepage.objects.all()
    for swiper in swipers:
        swiper.image = swiper.image.url
    return swipers

def getProject(id):
    project = Project.objects.get(id=id)
    project.type_name = project.type.name
    project.type_name_en = project.type.name_en
    project.image = project.image.url
    return project

def getProjects():
    projects = Project.objects.all()
    for project in projects:
        project.type_name = project.type.name
        project.type_name_en = project.type.name_en
        project.image = project.image.url
    return projects

def getProjectGallery(id):
    project_gallery = Project.objects.raw(
        "SELECT home_projectgallery.* "+
            "FROM home_project "+
            "INNER JOIN home_projectgallery ON home_projectgallery.project_id = home_project.id "+
            "WHERE home_project.id = "+ str(id) + " "+
            "ORDER BY home_projectgallery.id;")
    for project_photo in project_gallery:
        project_photo.image = project_photo.image.url
    return project_gallery

def getTypeProjects():
    typeProjects = TypeProject.objects.raw(
        "SELECT home_typeproject.* "+
            "FROM home_project "+
            "INNER JOIN home_typeproject ON home_typeproject.id = home_project.type_id "+
            "GROUP BY home_project.type_id "+
            "ORDER BY home_typeproject.name;")
    return typeProjects

def getAllTypeProjects():
    typeProjects = TypeProject.objects.all()
    return typeProjects

def getCompany():
    company = Company.objects.get(id=1)
    company.address_maps = GMAPS_LINK+company.address.replace(" ", "+")
    return company

def getCompanyAsProject():
    company = getCompany()    
    project = Project()
    project.title = company.sitename
    project.lat = company.lat
    project.lng = company.lng
    project.type_id = 1
    project.type_name = "efesto"
    project.type_name_en = "efesto"
    project.type_name_it = "efesto"
    project.location = company.address
    return project

def getAllRoles():
    roles = Role.objects.all()
    return roles

def getRoles():
    roles = Role.objects.raw(
            "SELECT COUNT(*) AS `all`, team_role.* "+
                "FROM team_team "+
                "INNER JOIN team_role ON team_role.id = team_team.role_id "+
                "WHERE team_role.display = 1 "+
                "GROUP BY team_team.role_id "+
                "ORDER BY team_role.order;")
    return roles

def getTeam():
    team = Team.objects.raw(
            "SELECT team_team.* "+
                "FROM team_team "+
                "INNER JOIN team_role ON team_role.id = team_team.role_id "+
                "WHERE team_role.display = 1;")
    i = 0
    for member in team:
        member.delay = i
        i = i + 1
        member.image = member.image.url
    return team

def getMember(id):
    member = Team.objects.get(id=id)
    member.delay = 0
    member.image = member.image.url    
    member.qualifications = member.qualifications.split('#')
    return member

def getService(id):
    service = Service.objects.get(id=id)
    service.delay = (service.order * 1) - 1
    service.image = service.image.url
    return service

def getServices():
    services = Service.objects.all()
    i = 0
    for service in services:
        service.delay = i
        i = i + 1
        service.image = service.image.url    
    return services

def getSubservices():
    subservices = Subservice.objects.all()
    for subservice in subservices:
        subservice.delay = getService(subservice.service_id).delay + 2
        subservice.delay = 0
    return subservices

def getNews():
    news = News.objects.all()
    i = 0
    for new in news:
        new.delay = i
        i = i + 1
        new.image = new.image.url
    return news

def getNew(id):
    new = News.objects.get(id=id)
    new.delay = 0
    new.image = new.image.url
    return new

def getDataError(codeError):
    dataError = Error.objects.get(code=codeError)
    dataError.image = ERROR_IMAGE
    return dataError

def getDataDictionary(projects):
    # dump data:
    dataDictionary = []
    i = 0
    for project in projects:
        dataDictionary.insert(i, {
            'link': '/'+get_language()+'/project/'+str(project.id),
            'title': project.title,
            'type': project.type_name,
            'image': TYPEPROJECT_PATH+project.type_name_en+'.png',
            'description': project.description,
            'lat': project.lat,
            'lng': project.lng,
            'marker': MARKERS_PATH+project.type_name_en+'.png',
        })
        i+=1
    dataJSON = dumps(dataDictionary)
    return dataJSON

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
