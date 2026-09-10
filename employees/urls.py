from django.urls import path
from . import views
from .views import hello_api
from .views import employee_list
from .views import HelloApiView
from.views import create_employee
from .views import employee_detail
from .views import update_employee
from .views import partial_update_employee
from .views import delete_employee
from .filtering import EmployeeListView




urlpatterns = [
    path("hello/", views.hello),
    path("send/", views.send),
    path("employee/<int:id>", views.get_employee),
    path("hello-api/", hello_api),
    # path("employee-list/", employee_list),
    path("hello-api-view/", HelloApiView.as_view()),
    path("create/", create_employee),
    path("employee-detail/<int:id>/", employee_detail),
    path("update-employee/<int:id>/", update_employee),
    path("partial-update-employee/<int:id>/", partial_update_employee),
    path("delete-employee/<int:id>/", delete_employee),
    path("employee-list/", EmployeeListView.as_view()),
]