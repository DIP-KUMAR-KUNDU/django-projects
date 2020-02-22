from django.urls import path
from . import views
urlpatterns = [
    path('', views.Index, name= 'index'),
    path('stocks', views.Stocks, name= 'stocks'),
    path('details_transaction', views.DetailsTransaction, name= 'details_transaction'),
    path('DetailsTransaction', views.DetailsTransaction, name= 'details_transaction'),
    path('export', views.export1, name= 'export1'),
    path('import', views.import1, name= 'import1'),
    path('test', views.Test, name= 'test'),
    path('exporting', views.exporting, name= 'exporting'),
    path('importing', views.importing, name= 'importing'),
    path('testing', views.Testing, name= 'testing'),
    
]
