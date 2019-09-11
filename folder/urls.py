from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ManagementSearchViewSet,QuizViewSet, WrongnoteViewSet, ManagementViewSet,QuizSelectViewSet

router = DefaultRouter()
router.register('problem', QuizViewSet)

select_list = QuizSelectViewSet.as_view({
    'get': 'list',

})
search_list = ManagementSearchViewSet.as_view({
    'get': 'list',

})
Management_list = ManagementViewSet.as_view({
    'get': 'list',
    'post': 'create',

})

Management_detail = ManagementViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

wrong_list = WrongnoteViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
wrong_detail = WrongnoteViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


urlpatterns = [
    path('', include(router.urls)),
    path('list', Management_list),
    path('list/<int:pk>', Management_detail),
    path('wrong', wrong_list),
    path('wrong/<int:pk>', wrong_detail),
    path('select',select_list),
    path('search',search_list),
]
