from . import views
from django.urls import path

urlpatterns = [
    # Banner Urls Start
    path('get_banner/', views.baneer_list, name='get_banner'),
    path('store_banner/', views.banner_create, name='store_banner'),
    path('delete_banner/<int:id>', views.banner_delete, name='delete_banner'),
    path('view_banner/<int:id>', views.banner_view, name='view_banner'),
    path('update_banner/<int:id>', views.banner_update, name='update_banner'),
    # Banner Urls End
    
    # category Urls Start
    path('get_category/', views.category_list, name='category_list'),
    path('store_category/', views.category_create, name='category_create'),
    path('delete_category/<int:id>', views.category_delete, name='delete_category'),
    path('view_category/<int:id>', views.category_view, name='view_category'),
    path('update_category/<int:id>', views.category_update, name='update_category'),
    # category Urls End
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    path('product_list/', views.product_list, name='product_list'),
    path('product_view/<int:id>/', views.product_view, name='product_view'),
    path('delete_product/<int:id>/', views.product_delete, name='delete_product'),

]