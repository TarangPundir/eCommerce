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
    path("product_save/", views.save_product, name="product_save"),

    path('review_get/', views.review_list, name='review_get'),
    path('review_store/', views.review_create, name='review_store'),
    path('review_view/<int:id>', views.review_view, name='review_view'),
    path('review_delete/<int:id>', views.review_delete, name='review_delete'),
    path('category_child/<int:id>', views.category_child, name='category_child'),
    path('category_parent/<int:child_id>/', views.parent_model_by_child_id, name='parent_model_by_child_id'),
    
    
    path('cart_list/', views.cart_list, name='cart_list'),
    path('cart_store/', views.cart_store, name='cart_store'),
    path('cart_view/<int:id>/', views.cart_view, name='cart_view'),
    path('cart_delete/<int:id>/', views.cart_delete, name='cart_delete'),
    path('cart_update/<int:id>/', views.cart_update, name='cart_update'),
    
    path('contact_list/', views.contact_list, name='contact_list'),
    path('contact_view/<int:id>/', views.contact_view, name='contact_view'),
    path('contact_store/', views.contact_store, name='contact_store'),
    path('contact_delete/<int:id>/', views.contact_delete, name='contact_delete'),
    path('contact_update/<int:id>/', views.contact_update, name='contact_update'),
    
    path('filter_product/', views.product_search, name='filter_product'),
    path('filter_category/', views.category_search, name='category_search'),
    path('category_product_search/', views.category_product, name='category'),
    path('product_less_price/', views.product_under_price, name='product_under_price'),

]