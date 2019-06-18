from django.urls import path
from .views import all_sch,sig_sch,b_index,search


urlpatterns = [
    path('', b_index, name='bind'),
    path('projects', all_sch, name='alschemes'),
    path('<int:sch_id>', sig_sch, name='sigsch'),
    path('search',search, name='srch'),

]
