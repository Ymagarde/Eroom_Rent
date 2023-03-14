from django.urls import path
from. import views
urlpatterns=[
     path('login',views.login,name='login'),
     path('Logout',views.Logout,name='Logout'),
     path('brokerlogin',views.brokerlogin,name='brokerlogin'),
     path('owenerlogin',views.owenerlogin,name='owenerlogin'),
     path("customerreg",views.customerreg,name="customerreg"),
     path("brokerreg",views.brokerreg,name="brokerreg"),
     path("owenerreg",views.owenerreg,name="owenerreg"),
     path("insertProperty",views.insertProperty,name="insertProperty"),
     path("editprorety",views.editprorety,name="editprorety"),
     path("deleteproperty",views.deleteproperty,name="deleteproperty"),
     path("showproperty",views.showproperty,name="showproperty"),
     path("booking",views.booking,name="booking"),
     path("customer",views.customer,name="customer"),
     path('dash',views.dash,name='dash'),
     path('sbp',views.sbp,name='sbp'),
]