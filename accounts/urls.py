from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views

urlpatterns = [
    path('intro/', views.introduction, name="intro"),
    path('store/', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('help/', views.help, name="help"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),












    path('chat/', views.chat, name="chat"),
    path('menu/', views.menu, name="menu"),
    path('normal_diet/', views.normal_diet, name="normal_diet"),
    path('weight_reduce/', views.weight_reduce, name="weight_reduce"),

    path('weight_gain/', views.weight_gain, name="weight_gain"),
    path('food_chart/', views.food_chart, name="food_chart"),

    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.introduction),
    path('home/', views.home, name="home"),

    path('calorie/', views.Calorie, name="calorie"),
    path('policy/', views.policy, name="policy"),
    path('contact/', views.contact, name="contact"),

    path('terms&conditions/', views.terms_conditions, name="terms&conditions"),

    path('about_us/', views.About, name="about_us"),

    path('account/', views.accountSettings, name="account"),
    path('edit/', views.profile_edit, name="edit"),

    path('nutrition/', views.Nutrition, name="nutrition"),
    path('brain/', views.Brain, name="brain"),
    path('eyes/', views.Eyes, name="eyes"),
    path('heart/', views.Heart, name="heart"),
    path('kidney/', views.Kidney, name="kidney"),
    path('bones/', views.Bones, name="bones"),
    path('muscles/', views.Muscles, name="muscles"),
    path('skin/', views.Skin, name="skin"),
    path('hair/', views.Hair, name="hair"),
    path('liver/', views.Liver, name="liver"),
    path('lungs/', views.Lungs, name="lungs"),
    path('shop/', views.shop, name="shop"),

    path('workout/', views.Workout, name="workout"),
    path('beginner/', views.beginner, name="beginner"),
    path('intermediate/', views.intermediate, name="intermediate"),
    path('advance/', views.advance, name="advance"),


    path('products/', views.products, name="products"),

    path('bmi/', views.bmi, name="bmi"),



    path('create_order/<str:pk_test>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk_test>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk_test>/', views.deleteOrder, name="delete_order"),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
         name="reset_password"),
    path('reset/<uidb64><token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),
         name="password_reset_confirm"),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),
         name="password_reset_done"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),
         name="password_reset_complete"),

]
