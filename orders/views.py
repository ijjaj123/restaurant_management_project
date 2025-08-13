from django.shortcuts import render

# Create your views here.
def menu_list(request):
    menu_items=[
        {"name":"Margerita pizza","price":8.99,"description":"classic pizza with fresh tomatoes,mozzaraella,and basil."}
        {"name": "veg Burger","price":5.49,"description":"A delicious vegetable patty with lettuce and tomato."},
        {"name":"pasta Alfredo","price":7.99,"description":"creamy Alfredo pasta with mushrooms and parmesan."},
    ]
