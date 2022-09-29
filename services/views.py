from efesto.functions import *

def services(request):
    dataError = Error()     
    dataError.image = ERROR_IMAGE
    current_page = 'services'
    try:
        configData = getConfigData()
        navbar = getNavbar()
        company = getCompany()    
        services = getServices()
        subservices = getSubservices()

    except ObjectDoesNotExist:  
        dataError = getDataError(404)    
        return render(request, "error.html", {'dataError': dataError,'configData': configData,  'current_page': current_page, 'navbar': navbar,
                                         'company': company, 'STYLES_PATH': STYLES_PATH})

    return render(request, "services.html", {'configData': configData, 'current_page': current_page, 'navbar': navbar,
                                        'services': services, 'subservices': subservices, 
                                         'company': company, 'STYLES_PATH': STYLES_PATH})
