from django.urls import path,include

from . import views


urlpatterns = [
    path('',views.BlogListView.as_view()),
    path('featured',views.BlogFeaturedView.as_view()),
    path('category',views.BlogCategoryView.as_view()),
    path('<slug>',views.BlogDetailView.as_view()),
]
