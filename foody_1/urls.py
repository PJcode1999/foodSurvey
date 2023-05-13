from django.urls import path 
from django.contrib.auth import views as auth_views
from . import views

app_name = 'foody_1'
 
urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="foody_1/login.html"),name='login'),
    path("northindian/", views.NorthIndianView.as_view(), name="northindian"),
    path("southindian/", views.SouthIndianView.as_view(), name="southindian"),
    path("italian/", views.ItalianView.as_view(), name="italian"),
    path("chinese/", views.ChineseView.as_view(), name="chinese"),
    path("continental/", views.ContinentalView.as_view(), name="continental"),
    path("fastfood/", views.FastFoodView.as_view(), name="fastfood"),
    path("beverages/", views.beveragesView.as_view(), name="bev"),
    path("deserts/", views.desView.as_view(), name="des"),
    path("confused/", views.ConfusedView.as_view(), name="confused"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("result/", views.resultpage, name="result"),
    path("feedback/", views.feedback, name="feedback"),


    path("confused/happy/", views.HappyView, name="happy"),
    path("confused/angry/", views.AngryView, name="angry"),
    path("confused/dehydrate/", views.DehydrateView, name="dehydrate"),
    path("confused/depress/", views.DepressiveView, name="depress"),
    path("confused/excite/", views.ExciteView, name="excite"),
    path("confused/unwell/", views.UnwellView, name="unwell"),


    path("chinese/noodles/", views.ChineseNoodlesView, name="noodles"),
    path("chinese/chillyPaneer/", views.ChineseChillyPaneerView, name="chillyPaneer"),


    path("continental/ham/", views.ContinentalHamView, name="ham"),
    path("continental/springroll/", views.ContinentalSpringRollView, name="springroll"),



    path("northindian/chollebature/", views.NorthIndianCholleView, name="cholle"),
    path("northindian/rajmachawal/", views.NorthIndianRajmaView, name="rajma"),


    path("southindian/dosa/", views.SouthIndianDosaView, name="dosa"),
    path("southindian/idli/", views.SouthIndianIdliView, name="idli"),


    path("italian/garlicbread/", views.ItalianGarlicView, name="garlic"),
    path("italian/pasta/", views.ItalianPastaView, name="pasta"),



    path("fastfood/aalootikki/", views.FastFoodAalooView, name="aalootikki"),
    path("fastfood/vadapao/", views.FastFoodPaoView, name="vadapao"),


    path("deserts/icecream/", views.IcecreamView, name="icecream"),
    path("deserts/pastries/", views.PastriesView, name="pastries"),
    path("deserts/chocolates/", views.ChocolatesView, name="chocolates"),

    path("beverages/tea/", views.TeaView, name="tea"),
    path("beverages/softdrinks/", views.softdrinksView, name="softdrinks"),
    path("beverages/juices/", views.juicesView, name="juices"),

    ]
