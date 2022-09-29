from efesto.functions import *

def news(request):
    dataError = Error()     
    dataError.image = ERROR_IMAGE
    current_page = 'news'
    try:
        configData = getConfigData()
        navbar = getNavbar()
        company = getCompany()    
        news = getNews()

    except ObjectDoesNotExist:  
        dataError = getDataError(404)    
        return render(request, "error.html", {'dataError': dataError,'configData': configData,  'current_page': current_page, 'navbar': navbar,
                                         'company': company, 'STYLES_PATH': STYLES_PATH})

    return render(request, "news.html", {'configData': configData, 'current_page': current_page, 'navbar': navbar,
                                         'news': news,
                                         'company': company, 'STYLES_PATH': STYLES_PATH})


def new(request, id):
    dataError = Error()     
    dataError.image = ERROR_IMAGE
    current_page = 'news'
    try:
        configData = getConfigData()
        navbar = getNavbar()
        company = getCompany()    
        new = getNew(id)

    except ObjectDoesNotExist:  
        dataError = getDataError(404)    
        return render(request, "error.html", {'dataError': dataError,'configData': configData,  'current_page': current_page, 'navbar': navbar,
                                         'company': company, 'STYLES_PATH': STYLES_PATH})

    return render(request, "new.html", {'configData': configData, 'current_page': current_page, 'navbar': navbar,
                                         'new': new,
                                         'company': company, 'STYLES_PATH': STYLES_PATH})
