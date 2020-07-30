from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from restaurants.models import Item, Location, Menu, Restaurant, SubMenu
from users.permission import IsRestaurantAdmin
from users.serializers.restaurantadmin.restaurantadmin_restaurant_serializers \
    import RestaurantSerializer, MenuSerializer, LocationSerializer, SubMenuSerializer, \
    ItemSerializer


@api_view(['GET'])
@permission_classes([IsRestaurantAdmin])
def restaurantadmin_restaurants(request):

    if request.method == "GET":
        restaurants = Restaurant.objects.filter(user=request.user)
        print(restaurants)
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsRestaurantAdmin])
def restaurantadmin_restaurant(request, id):

    if request.method == "GET":
        restaurant = Restaurant.objects.filter(id=id, user=request.user)
        serializer = RestaurantSerializer(restaurant, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "PUT":
        request.data["restaurant"]["id"] = id
        serializer = RestaurantSerializer(data=request.data["restaurant"])
        if serializer.is_valid(raise_exception=ValueError) or serializer.is_valid(raise_exception=Exception):
            restaurant = Restaurant.objects.get(user=request.user, id=id)
            restaurant.name = serializer.validated_data["name"]
            restaurant.description = serializer.validated_data["description"]
            restaurant.save()
            serializer = RestaurantSerializer(restaurant)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        restaurant = Restaurant.objects.get(user=request.user, id=id)
        if restaurant:
            restaurant.delete()
            return Response("Restaurant deleted.", status=status.HTTP_200_OK)
        else:
            return Response("Restaurant object doesn't exist.", status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsRestaurantAdmin])
def restaurantadmin_restaurant_create(request):

    if request.method == "POST":
        serializer = RestaurantSerializer(data=request.data["restaurant"])
        if serializer.is_valid(raise_exception=ValueError) or serializer.is_valid(raise_exception=Exception):

            if len(Restaurant.objects.filter(name=serializer.validated_data["name"])) != 0:
                return Response("Restaurant with this name exists.", status.HTTP_400_BAD_REQUEST)

            restaurant = Restaurant.objects.create(name=serializer.validated_data["name"],
                                                   description=serializer.validated_data["description"])
            restaurant.user.add(request.user)
            restaurant.save()
            serializer = RestaurantSerializer(restaurant)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsRestaurantAdmin])
def restaurantadmin_menu(request, menu_id):

    if request.method == "GET":
        menu = Menu.objects.filter(id=menu_id)

        if len(menu) == 0:
            return Response("No menu with this ID.", status=status.HTTP_400_BAD_REQUEST)

        if Restaurant.objects.get(id=menu[0].restaurant_id, user=request.user) is None:
            return Response("You don't have the right permission to view this menu.", status=status.HTTP_400_BAD_REQUEST)

        serializer = MenuSerializer(menu[0])
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "PUT":
        request.data["menu"]["id"] = menu_id
        serializer = MenuSerializer(data=request.data["menu"])
        if serializer.is_valid(raise_exception=ValueError) or serializer.is_valid(raise_exception=Exception):
            menu = Menu.objects.filter(id=menu_id)

            if len(menu) == 0:
                return Response("No menu with this ID.", status=status.HTTP_400_BAD_REQUEST)

            if Restaurant.objects.get(id=menu[0].restaurant_id, user=request.user) is None:
                return Response("You don't have the right permission to view this menu.",
                                status=status.HTTP_400_BAD_REQUEST)
            if len(Restaurant.objects.filter(id=serializer.validated_data["restaurant_id"], user=request.user)) == 0:
                return Response("No Restaurant with this ID for this restaurant.", status=status.HTTP_400_BAD_REQUEST)
            if len(Location.objects.filter(restaurant=menu[0].restaurant, id=serializer.validated_data["location_id"])) == 0:
                return Response("No location with this ID for this restaurant.", status=status.HTTP_400_BAD_REQUEST)

            menu = menu[0]
            menu.name = serializer.validated_data["name"]
            menu.description = serializer.validated_data["description"]
            menu.location_id = serializer.validated_data["location_id"]
            menu.available = serializer.validated_data["available"]
            menu.available_start_date = serializer.validated_data["available_start_date"]
            menu.available_end_date = serializer.validated_data["available_end_date"]
            menu.save()

            serializer = MenuSerializer(menu)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        menu = Menu.objects.filter(id=menu_id)

        if len(menu) == 0:
            return Response("No menu with this ID.", status=status.HTTP_400_BAD_REQUEST)

        if Restaurant.objects.get(id=menu[0].restaurant_id, user=request.user) is None:
            return Response("You don't have the right permission to view this menu.", status=status.HTTP_400_BAD_REQUEST)

        if menu[0]:
            menu.delete()
            return Response("Restaurant deleted.", status=status.HTTP_200_OK)
        else:
            return Response("Restaurant object doesn't exist.", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsRestaurantAdmin])
def restaurantadmin_menus(request, restaurant_id):

    if request.method == "GET":
        if len(Restaurant.objects.filter(id=restaurant_id, user=request.user)) == 0:
            return Response("No restaurant with this ID.", status=status.HTTP_400_BAD_REQUEST)

        menus = Menu.objects.filter(restaurant_id=restaurant_id)
        serializer = MenuSerializer(menus, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsRestaurantAdmin])
def restaurantadmin_menu_create(request):

    if request.method == "POST":
        serializer = MenuSerializer(data=request.data["menu"])
        if serializer.is_valid(raise_exception=ValueError) or serializer.is_valid(raise_exception=Exception):
            if len(Restaurant.objects.filter(id=serializer.validated_data["restaurant_id"], user=request.user)) == 0:
                return Response("No restaurant with this ID.", status=status.HTTP_400_BAD_REQUEST)
            if len(Location.objects.filter(restaurant_id=serializer.validated_data["restaurant_id"],
                                           id=serializer.validated_data["location_id"])) == 0:
                return Response("No location with this ID.", status=status.HTTP_400_BAD_REQUEST)

            menu = Menu.objects.create(restaurant_id=serializer.validated_data["restaurant_id"], name=serializer.validated_data["name"]
                                       ,description=serializer.validated_data["description"], location_id=
                                       serializer.validated_data["location_id"], available=serializer.
                                       validated_data["available"], available_start_date=serializer.
                                       validated_data["available_start_date"], available_end_date=serializer.validated_data["available_end_date"])
            menu.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsRestaurantAdmin])
def restaurantadmin_locations(request, restaurant_id):

    if request.method == "GET":
        if len(Restaurant.objects.filter(id=restaurant_id, user=request.user)) == 0:
            return Response("No restaurant with this ID.", status=status.HTTP_400_BAD_REQUEST)

        locations = Location.objects.filter(restaurant_id=restaurant_id)
        serializer =  LocationSerializer(locations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', "PUT", "DELETE"])
@permission_classes([IsRestaurantAdmin])
def restaurantadmin_location(request, restaurant_id, location_id):

    if request.method == "GET":
        if len(Restaurant.objects.filter(id=restaurant_id, user=request.user)) == 0:
            return Response("No restaurant with this ID.", status=status.HTTP_400_BAD_REQUEST)

        location = Location.objects.filter(id=location_id, restaurant_id=restaurant_id)
        if len(location) == 0:
            return Response("No location with this ID.", status=status.HTTP_400_BAD_REQUEST)
        location = location[0]
        serializer = LocationSerializer(location)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "PUT":
        request.data["location"]["restaurant_id"] = restaurant_id
        serializer = Location(data=request.data["location"])

        if serializer.is_valid(raise_exception=ValueError) or serializer.is_valid(raise_exception=Exception):
            if len(Restaurant.objects.filter(id=serializer.validated_data["restaurant_id"], user=request.user)) == 0:
                return Response("No restaurant with this ID.", status=status.HTTP_400_BAD_REQUEST)

            location = Location.objects.filter(restaurant_id=serializer.validated_data["restaurant_id"],
                                           id=serializer.validated_data["id"])
            if len(location) == 0:
                return Response("No location with this ID.", status=status.HTTP_400_BAD_REQUEST)

            location = location[0]
            location.longitude = serializer.validated_data["longitude"]
            location.latitude = serializer.validated_data["latitude"]
            # location.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":

        if len(Restaurant.objects.filter(id=restaurant_id, user=request.user)) == 0:
            return Response("No restaurant with this ID.", status=status.HTTP_400_BAD_REQUEST)

        location = Location.objects.filter(restaurant_id=restaurant_id,
                                       id=location_id)
        if len(location) == 0:
            return Response("No location with this ID.", status=status.HTTP_400_BAD_REQUEST)

        location.delete()
        return Response("Location deleted.", status=200)


@api_view(['POST'])
@permission_classes([IsRestaurantAdmin])
def restaurantadmin_location_create(request):

    if request.method == "POST":
        serializer = LocationSerializer(data=request.data["location"])
        if serializer.is_valid(raise_exception=ValueError) or serializer.is_valid(raise_exception=Exception):
            restaurant = Restaurant.objects.filter(id=serializer.validated_data["restaurant_id"])
            if len(restaurant) == 0:
                return Response("Restaurant doesn't exist.", status=status.HTTP_400_BAD_REQUEST)
            restaurant = restaurant[0]
            location = Location.objects.create(restaurant=restaurant, latitude=serializer.validated_data["longitude"],
                                               longitude=serializer.validated_data["latitude"])

            location.save()
            serializer = LocationSerializer(location)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsRestaurantAdmin])
def restaurantadmin_submenu_create(request):
    if request.method == "POST":
        serializer = SubMenuSerializer(data=request.data["submenu"])
        if serializer.is_valid(raise_exception=ValueError) or serializer.is_valid(raise_exception=Exception):
            restaurant = Restaurant.objects.filter(id=serializer.validated_data["restaurant_id"])
            if len(restaurant) == 0:
                return Response("Restaurant doesn't exist.", status=status.HTTP_400_BAD_REQUEST)
            restaurant = restaurant[0]
            if request.user not in restaurant.user.all():
                return Response("Unauthorized.", status=status.HTTP_403_FORBIDDEN)

            menu = Menu.objects.filter(id=serializer.validated_data["menu_id"])
            if len(menu) == 0:
                return Response("Menu doesn't exist.", status=status.HTTP_400_BAD_REQUEST)

            submenu = SubMenu(restaurant_id=serializer.validated_data["restaurant_id"],
                              menu_id=serializer.validated_data["menu_id"],
                              meal_type=serializer.validated_data["meal_type"],
                              description=serializer.validated_data["description"],
                              available=serializer.validated_data["available"])
            submenu.save()
            serializer = SubMenuSerializer(submenu)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsRestaurantAdmin])
def restaurantadmin_submenus(request, restaurant_id, menu_id):
    if request.method == "GET":
        if len(Restaurant.objects.filter(id=restaurant_id, user=request.user)) == 0:
            return Response("No Restaurant with this ID for this restaurant.", status=status.HTTP_400_BAD_REQUEST)
        submenu = SubMenu.objects.filter(restaurant_id=restaurant_id, menu_id=menu_id)
        serializer = SubMenuSerializer(submenu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsRestaurantAdmin])
def restaurantadmin_item_create(request):
    if request.method == "POST":
        serializer = ItemSerializer(data=request.data["item"])
        if serializer.is_valid(raise_exception=ValueError) or serializer.is_valid(raise_exception=Exception):
            restaurant = Restaurant.objects.filter(id=serializer.validated_data["restaurant_id"])
            if len(restaurant) == 0:
                return Response("Restaurant doesn't exist.", status=status.HTTP_400_BAD_REQUEST)
            restaurant = restaurant[0]
            if request.user not in restaurant.user.all():
                return Response("Unauthorized.", status=status.HTTP_403_FORBIDDEN)
            if len(SubMenu.objects.filter(id=serializer.validated_data["submenu_id"], restaurant_id=restaurant.id)) == 0:
                return Response("Submenu doesn't exist.", status=status.HTTP_400_BAD_REQUEST)
            item = Item.objects.create(restaurant_id=serializer.validated_data["restaurant_id"],
                                       submenu_id=serializer.validated_data["submenu_id"],
                                       name=serializer.validated_data["name"],
                                       description=serializer.validated_data["description"],
                                       price=serializer.validated_data["price"])
            item.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "DELETE"])
@permission_classes([IsRestaurantAdmin])
def restaurantadmin_item(request, id):
    item = Item.objects.filter(id=id)
    if len(item) == 0:
        return Response("No Item with this id.", status=status.HTTP_400_BAD_REQUEST)
    item = item[0]
    if request.user not in item.restaurant.user.all():
        return Response("Unauthorized.", status=status.HTTP_403_FORBIDDEN)
    if request.method == "GET":
        serializer = ItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "DELETE":
        item.delete()
        return Response(status=status.HTTP_200_OK)
