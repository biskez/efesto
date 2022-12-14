from efesto.functions import *

def project(request, id):
    dataError = Error()     
    dataError.image = ERROR_IMAGE
    current_page = 'gallery'
    try:
        configData = getConfigData()
        navbar = getNavbar()

        company = getCompany()
        
        project = getProject(id)        
        project_gallery = getProjectGallery(id)

        typeProjects = getTypeProjects()

        maps = getConfigMaps()
        dataJSON = getDataDictionary([project])

    except ObjectDoesNotExist:  
        dataError = getDataError(404)    
        return render(request, "error.html", {'dataError': dataError,'configData': configData,  'current_page': current_page, 'navbar': navbar,
                                         'company': company, 'STYLES_PATH': STYLES_PATH})

    return render(request, "project.html", {'configData': configData, 'current_page': current_page, 'navbar': navbar, 'typeProjects': typeProjects,
                                         'project': project, 'project_gallery': project_gallery, 'gmaps': maps.gmaps, 'marker': maps.marker,
                                         'dataJSON': dataJSON, 'cluster_path': maps.cluster_path, 'company': company, 'STYLES_PATH': STYLES_PATH})
