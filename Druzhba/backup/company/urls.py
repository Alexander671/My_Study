from django.urls import path
from company.views import CompanyViewSet, CompanyMemberViewSet

company_list = CompanyViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

company_detail = CompanyViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy'
})

company_member_list = CompanyMemberViewSet.as_view({
    'get': 'list'
})

company_member_detail = CompanyMemberViewSet.as_view({
    'patch': 'partial_update',
    'delete': 'destroy',
    'post': 'create'
})


urlpatterns = [
    path('<str:pk>/members/', company_member_list),
    path('member/', company_member_detail),
    path('<str:pk>/', company_detail),
    path('', company_list),
]
