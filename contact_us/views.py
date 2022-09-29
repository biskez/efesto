from efesto.functions import *

def contact_us(request):
    dataError = Error()     
    dataError.image = ERROR_IMAGE
    current_page = 'contact_us'
    try:
        configData = getConfigData()
        navbar = getNavbar()
        company = getCompany()    
        maps = getConfigMaps()
        project = getCompanyAsProject()

        dataJSON = getDataDictionary([project])

    except ObjectDoesNotExist:  
        dataError = getDataError(404)    
        return render(request, "error.html", {'dataError': dataError,'configData': configData,  'current_page': current_page, 'navbar': navbar,
                                         'company': company, 'STYLES_PATH': STYLES_PATH})

    return render(request, "contact_us.html", {'configData': configData, 'current_page': current_page, 'navbar': navbar,
                                         'gmaps': maps.gmaps, 'marker': maps.marker, 'dataJSON': dataJSON, 'cluster_path': maps.cluster_path, 
                                         'company': company, 'STYLES_PATH': STYLES_PATH})
