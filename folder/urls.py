from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ManagementSearchViewSet, QuizViewSet, WrongnoteViewSet, ManagementViewSet, QuizSelectViewSet, \
    OriginQuizViewSet, QuizDetailViewSet, WrongnotDetailViewSet

router = DefaultRouter()
router.register('problem', OriginQuizViewSet)

select_list = QuizSelectViewSet.as_view({
    'get': 'list',

})
quiz_manage_list = QuizViewSet.as_view({
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

quiz_detail = QuizDetailViewSet.as_view({'get' : 'list'})

wrong_d_list = WrongnotDetailViewSet.as_view({'get' : 'list'})


urlpatterns = [
    path('', include(router.urls)),
    path('manage',quiz_manage_list),
    path('list', Management_list),
    path('list/<int:pk>', Management_detail),
    path('wrong', wrong_list),
    path('wrong/<int:pk>', wrong_detail),
    path('select',select_list),
    path('search',search_list),
    path('detail_quiz', quiz_detail),
    path('detail_wrong', wrong_d_list),
]
