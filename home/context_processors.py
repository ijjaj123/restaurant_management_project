from django.conf import settings

def restaurant_info(request):
    return{
        "restaurant_name":getattr(settings,"RESTAURANT_NAME","Restaurant"),
        "opening_hours":getattr(settings,"OPENING_HOURS","Hours not avaliable"),
    }