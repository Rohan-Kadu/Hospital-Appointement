from webbrowser import get
from django.urls import path,include,re_path
from .import views
#from django.conf.urls import url
urlpatterns = [
   path("",views.HomePageView,name="homepage"),
   path("insert/",views.InsertData,name="insert"),
   path("appointement/",views.AppointementPageView,name="appointement"),
   path("contactus/",views.ContactUsPageView,name="contactus"),
   path("adminHome/",views.AdminHomePageView,name="adminHome"),
   path("aboutus/",views.AboutPageView,name="aboutus"),
   path("loginadmin/",views.LoginAdmin,name="login"),
   path("alldata/",views.Table_all,name="all_data"),
   path("edit/<int:pk>",views.EditPage,name='edit'),
   path("update/<int:pk>",views.UpdateData,name="update"),
   path("sendemail/<int:pk>",views.sendMail,name="email"),
   path("admininsert/",views.AdminInsertData,name="adminInsert"),
   path("adminbook/",views.AdminAppointementPageView,name="adminbook"),
   path("approved/",views.ApprovedPageView,name='approved'),
  #  path('data/<int:pk>',views.getData,name="getdata"),
   #re_path(r'^pdf/$', views.GeneratePDF.as_view(),name="view"),
   #path("pdf/<int:pk>",views.pdf,name="view"),
  path("dynapdf/<int:pk>",views.GeneratePDF.as_view(),name="view"),
  path("approvedT/",views.ApprovedData , name="showtable"),
  path("pdf/<int:pk>",views.GeneratePDF1.as_view(),name="view1"),
   path("done/<int:pk>",views.Done,name="done"),
   path('avoid_colsn', views.avoid_colsn , name="avoid_colsn"),
   path('avoid_colsn1', views.avoid_colsn1 , name="avoid_colsn1"),
 ]#userRequest.objects.get(id=pk)