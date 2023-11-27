"""
URL configuration for LensUp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from myapp import views



urlpatterns = [
    path('login/',views.login),
    path('login_Post/',views.login_Post),
    path('logout/', views.logout),

    path('forgotpassword/', views.forgotpassword),
    path('forgotpassword_post/', views.forgotpassword_post),


    path('admin_add_category/',views.admin_add_category),
    path('admin_add_category_post/',views.admin_add_category_post),
    path('admin_view_category/',views.admin_view_category),
    path('admin_view_category_post/',views.admin_view_category_post),
    path('delete_category/<id>',views.delete_category),
    path('view_pending_photographer/',views.view_pending_photographers),
    path('approve_photographer/<id>',views.approve_photographer),
    path('pending_post/',views.pending_post),
    path('view_approved_photographers/',views.view_approved_photographers),
    path('Search_Approved_pg_post/',views.Search_Approved_pg_post),
    path('view_rejected_photographers/',views.view_rejected_photographers),
    path('Search_rejected_pg_post/',views.Search_rejected_pg_post),
    path('reject_photographer/<id>',views.reject_photographer),
    path('view_content/',views.view_content),
    path('adm_view_blog/',views.adm_view_blog),
    path('adm_view_blog_post/',views.adm_view_blog_post),
    path('view_contents_post/',views.view_contents_post),
    path('admin_remove_content/<id>',views.admin_remove_content),
    path('adm_remove_blog/<id>',views.adm_remove_blog),
    path('view_feedback/',views.view_feedback),
    path('view_feedback_post/',views.view_feedback_post),
    path('view_users/',views.view_users),
    path('view_users_post/',views.view_users_post),
    path('Admin_change_password/',views.Admin_change_password),
    path('Admin_change_password_post/',views.Admin_change_password_post),
    path('Admin_home/',views.Admin_home),

#==photographer======

    path('photgrapher_Add_Blog/',views.photgrapher_Add_Blog),
    path('Add_Blog_post/',views.Add_Blog_post),
    path('photgrapher_View_Blog/', views.photgrapher_View_Blog),
    path('p_view_blog_Post/', views.p_view_blog_Post),
    path('photgrapher_Edit_Blog/<id>', views.photgrapher_Edit_Blog),
    path('Edit_Blog_post/', views.Edit_Blog_post),
    path('delete_blog/<id>', views.delete_blog),

    path('photographer_Add_Contents/', views.photographer_Add_Contents),
    path('view_others_blog/', views.view_others_blog),
    path('view_others_content/', views.view_others_content),
    path('Add_contents_post/', views.Add_contents_post),
    path('photgrapher_View_Contents/', views.photgrapher_View_Contents),
    path('P_View_content_Post/', views.P_View_content_Post),
    path('photgrapher_Edit_Contents/<id>', views.photgrapher_Edit_Contents),
    path('delete_content/<id>', views.delete_content),
    path('Edit_Content_Post/', views.Edit_Content_Post),

    path('photgrapher_Edit_Profile/', views.photgrapher_Edit_Profile),
    path('Photographer_Edit_Profile_Post/', views.Photographer_Edit_Profile_Post),
    path('photgrapher_Photographer_Registration/', views.photgrapher_Photographer_Registration),
    path('photgrapher_Photographer_Registration_post/', views.Photographer_Registration_Post),

    path('photgrapher_Send_Feedback/', views.photgrapher_Send_Feedback),
    path('P_Send_Feedback_Post/', views.P_Send_Feedback_Post),
    path('p_view_feedback/', views.p_view_feedback),
    path('p_view_feedback_post/', views.p_view_feedback_post),
    path('p_delete_feedback/<id>', views.p_delete_feedback),


    path('photgrapher_View_Order_More/', views.photgrapher_View_Order_More),
    path('photgrapher_View_Orders/', views.photgrapher_View_Orders),
    path('P_View_Order_Post/', views.P_View_Order_Post),
    path('photgrapher_View_Profile/', views.photgrapher_View_Profile),
    path('photgrapher_View_user_Booking/', views.photgrapher_View_user_Booking),
    path('photgrapher_View_user_Booking_post/', views.photgrapher_View_user_Booking_post),
    path('p_approve_booking/<id>', views.p_approve_booking),
    path('p_reject_booking/<id>', views.p_reject_booking),
    path('p_view_approved_booking/',views.p_view_approved_booking),
    path('p_view_approved_booking_post/',views.p_view_approved_booking_post),
    path('p_view_rejected_booking/',views.p_view_rejected_booking),
    path('p_view_rejected_booking_post/',views.p_view_rejected_booking_post),
    path('Photographer_Home/',views.Photographer_Home),


    path('User_Edit_profile/',views.User_Edit_profile),
    path('User_Edit_profile_post/',views.User_Edit_profile_post),
    path('User_Payment/<id>', views.User_Payment),
    path('User_Payment_post/', views.User_Payment_post),
    path('user_view_order/', views.user_view_order),
    path('user_view_order_post/', views.user_view_order_post),
    path('u_view_blog/', views.u_view_blog),
    path('u_view_blog_post/', views.u_view_blog_post),
    path('User_Purchase_Photos/<id>', views.User_Purchase_Photos),
    path('User_Search_Photographers/', views.User_Search_Photographers),
    path('User_Search_Photographers_post/', views.User_Search_Photographers_post),
    path('u_book_photographer/<id>', views.u_book_photographer),
    path('u_book_photographer_post/', views.u_book_photographer_post),
    path('u_view_booking/', views.u_view_booking),
    path('u_view_booking_post/', views.u_view_booking_post),
    path('u_delete_booking/<id>', views.u_delete_booking),
    path('u_view_approved_booking/', views.u_view_approved_booking),
    path('u_view_approved_booking_post/', views.u_view_approved_booking_post),
    path('u_view_rejected_booking/', views.u_view_rejected_booking),
    path('u_view_rejected_booking_post/', views.u_view_rejected_booking_post),

    path('User_Send_Feedback/', views.User_Send_Feedback),
    path('User_Send_Feedback_post/', views.User_Send_Feedback_post),
    path('u_view_feedback/', views.u_view_feedback),
    path('u_view_feedback_post/', views.u_view_feedback_post),
    path('u_delete_feedback/<id>', views.u_delete_feedback),

    path('User_Registration/', views.User_Registration),
    path('User_Registration_post/', views.User_Registration_post),
    path('User_View_Booked_Photographer/', views.User_View_Booked_Photographer),
    path('User_View_Profile/', views.User_View_Profile),
    path('User_Home/', views.User_Home),
]

