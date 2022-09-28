from efesto.functions import *

def team(request):
    dataError = Error()     
    dataError.image = ERROR_IMAGE
    current_page = 'team'
    line_length = 4
    try:
        configData = getConfigData()
        navbar = getNavbar()

        company = getCompany()    

        roles = getRoles()
        team = getTeam()
        
        for role in roles:
            role.lines = []
            role.line_length = line_length
            i=0
            while(role.all >= role.line_length):
                role.all -= 4
                role.lines.insert(i,'line1')
                i+=1
            if(role.all > 0):
                role.lines.insert(i,'line1')

    except ObjectDoesNotExist:  
        dataError = getDataError(404)    
        return render(request, "error.html", {'dataError': dataError,'configData': configData,  'current_page': current_page, 'navbar': navbar,
                                         'company': company, 'STYLES_PATH': STYLES_PATH})

    return render(request, "team.html", {'configData': configData, 'current_page': current_page, 'navbar': navbar, 'roles': roles, 'team': team,
                                         'company': company, 'STYLES_PATH': STYLES_PATH})


def member(request, id):
    dataError = Error()     
    dataError.image = ERROR_IMAGE
    current_page = 'team'
    try:
        configData = getConfigData()
        navbar = getNavbar()

        company = getCompany()    

        member = getMember(id)

    except ObjectDoesNotExist:  
        dataError = getDataError(404)    
        return render(request, "error.html", {'dataError': dataError,'configData': configData,  'current_page': current_page, 'navbar': navbar,
                                         'company': company, 'STYLES_PATH': STYLES_PATH})

    return render(request, "member.html", {'configData': configData, 'current_page': current_page, 'navbar': navbar, 'member': member,
                                         'company': company, 'STYLES_PATH': STYLES_PATH})
