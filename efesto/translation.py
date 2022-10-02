# Model Translation
#from modeltranslation.translator import translator, TranslationOptions
from translation import translator, TranslationOptions
from home.models import *
from navbar.models import *
from team.models import *
from services.models import *
from contact_us.models import *
from news.models import *

class TypeProjectTranslationOptions(TranslationOptions):
    fields = ('name',)
translator.register(TypeProject,TypeProjectTranslationOptions)

class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'begin', 'end', 'location', 'owner', 'partners')
translator.register(Project, ProjectTranslationOptions)

class SwiperTranslationOptions(TranslationOptions):
    fields = ('h1', 'h4')
translator.register(SwiperHomepage, SwiperTranslationOptions)

class CompanyTranslationOptions(TranslationOptions):
    fields = ('address', 'open', 'closed')
translator.register(Company, CompanyTranslationOptions)

class ErrorTranslationOptions(TranslationOptions):
    fields = ('error',)
translator.register(Error, ErrorTranslationOptions)

class NavbarTranslationOptions(TranslationOptions):
    fields = ('name','route')
translator.register(Navbar, NavbarTranslationOptions)

class RoleTranslationOptions(TranslationOptions):
    fields = ('name',)
translator.register(Role, RoleTranslationOptions)

class TeamTranslationOptions(TranslationOptions):
    fields = ('grade', 'qualifications', 'description')
translator.register(Team, TeamTranslationOptions)

class ServiceTranslationOptions(TranslationOptions):
    fields = ('name',)
translator.register(Service, ServiceTranslationOptions)

class SubserviceTranslationOptions(TranslationOptions):
    fields = ('name',)
translator.register(Subservice, SubserviceTranslationOptions)

class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'description', 'date',)
translator.register(News, NewsTranslationOptions)
