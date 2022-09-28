from efesto.functions import *

def home(request):   
    dataError = Error()     
    dataError.image = ERROR_IMAGE
    current_page = 'home'
    try:
        configData = getConfigData()
        navbar = getNavbar()

        swipers = getSwipers()
        company = getCompany()
        
        projects = getProjects()

        maps = getConfigMaps()        
        dataJSON = getDataDictionary(projects)
    except ObjectDoesNotExist:  
        dataError = getDataError(404)        
        return render(request, "error.html", {'dataError': dataError,'configData': configData,  'current_page': current_page, 'navbar': navbar,
                                         'company': company, 'STYLES_PATH': STYLES_PATH})  

    return render(request, "home.html", {'configData': configData, 'gmaps': maps.gmaps, 'marker': maps.marker,
                                         'current_page': current_page, 'navbar': navbar, 'swipers': swipers, 'projects': projects, 'company': company, 
                                         'dataJSON': dataJSON, 'cluster_path': maps.cluster_path, 'STYLES_PATH': STYLES_PATH})