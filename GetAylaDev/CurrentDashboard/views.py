from django.shortcuts import render

# Create your views here.
import json
from haralyzer import HarParser, HarPage
import pdb;
import requests
import urllib, json
from urllib.request import urlopen
from urllib.request import urlopen, Request
from django.core.files import File
import os
from django.contrib.auth.decorators import login_required
from .models import *
from django.utils import timezone
from datetime import timedelta
from django.db.models import Sum

from django.http import JsonResponse, HttpResponse
from instagram_private_api import Client, ClientCompatPatch

@login_required(login_url='login')
def dashboard (request):
    current_user=request.user
    userId=current_user.id
    ProfileInfo =profileDesc.objects.filter(owner=userId).order_by('-id')[:1]
    NewFolowersCountSet =Newfollowers.objects.filter(owner=userId)
    InteractionsOnFollowersCountSet =CustomerInteractionsOnFollowers.objects.filter(owner=userId)
    InteractionsOnOnTargetCountSet =CustomerInteractionsOnTarget.objects.filter(owner=userId)
    InteractionsYouGotCountSet =profileDesc.objects.filter(owner=userId)



    CountOfFollowers=0
    CountOfFollowing=0
    InteractionsyouGot=0

    for list in ProfileInfo:
        CountOfFollowers=list.totalFollowers
        CountOfFollowing=list.totalFollowing
        InteractionsyouGot=list.totalInteractionsyouGot
        #print(list.totalFollowers, "\n")

        #count=list.totalFollowers+count


    print(CountOfFollowers, "\n")
    print(current_user.id, "\n")
    print(CountOfFollowing, "\n")
    print(InteractionsyouGot, "\n")

    #now = timezone.now()

    now = timezone.now()
    NewFolowersCount = NewFolowersCountSet.aggregate(
        total=models.Count('id'),
        today=models.Count('id', filter=models.Q(created__date=now.date())),
        yesterday=models.Count('id', filter=models.Q(created__date__gte=(now - timedelta(hours=24)).date())),
        last_7_day=models.Count('id', filter=models.Q(created__date__gte=(now - timedelta(days=7)).date())),
    )

    InteractionsOnFollowersCount = InteractionsOnFollowersCountSet.aggregate(
        total=models.Count('id'),
        today=models.Count('id', filter=models.Q(created__date=now.date())),
        yesterday=models.Count('id', filter=models.Q(created__date__gte=(now - timedelta(hours=24)).date())),
        last_7_day=models.Count('id', filter=models.Q(created__date__gte=(now - timedelta(days=7)).date())),
    )
    InteractionsOnOnTargetCount = InteractionsOnOnTargetCountSet.aggregate(
        total=models.Count('id'),
        today=models.Count('id', filter=models.Q(created__date=now.date())),
        yesterday=models.Count('id', filter=models.Q(created__date__gte=(now - timedelta(hours=24)).date())),
        last_7_day=models.Count('id', filter=models.Q(created__date__gte=(now - timedelta(days=7)).date())),

    )

    interestFollower=' '
    NewFolowersList = NewFolowersCountSet.filter(created__date__gte=(now - timedelta(days=7)).date())
    for list in NewFolowersList:
        interestFollower=list.interest+' '+interestFollower
        print(interestFollower, "\n")

    number=1
    YourInteractionsOnMonths=[]
    while number <= 12:
        data=InteractionsOnOnTargetCountSet.filter(created__month=number).count()
        data1=InteractionsOnFollowersCountSet.filter(created__month=number).count()
        data3=data+data1
        #print("month= ",number,data, "\n")
        YourInteractionsOnMonths.append(data3)
        number = number + 1


    number=1
    InteractionsYouGotOnMonth=[]
    while number <= 12:
        data=InteractionsYouGotCountSet.filter(created__month=number).aggregate(Sum('totalInteractionsyouGot'))
        if data['totalInteractionsyouGot__sum'] is None:
            InteractionsYouGotOnMonth.append(0)
        else :
            InteractionsYouGotOnMonth.append(data['totalInteractionsyouGot__sum'])
        number = number + 1
    #print(YourInteractionsOnMonths, "\n")

    #print(InteractionsYouGotOnMonth, "\n")

    #print(ProfileInfo, "\n")






    return render(request, 'dashboard.html', {'InteractionsyouGot':InteractionsyouGot,
                                              'YourInteractionsOnMonths':YourInteractionsOnMonths,'InteractionsYouGotOnMonth':InteractionsYouGotOnMonth,
                                              'NewFolowersCount': NewFolowersCount,'InteractionsOnFollowersCount':InteractionsOnFollowersCount,
                                              'InteractionsOnOnTargetCount':InteractionsOnOnTargetCount,'NewFolowersList':NewFolowersList,
                                              'ProfileInfo':ProfileInfo,'interestFollower':interestFollower})



@login_required(login_url='login')
def targeting (request):
    now = timezone.now()
    current_user=request.user
    userId=current_user.id

    InteractionsOnOnTargetCountSet =CustomerInteractionsOnTarget.objects.filter(owner=userId)
    TargetCountSet =targets.objects.filter(owner=userId)

    TargetList = TargetCountSet.filter(created__date__gte=(now - timedelta(days=7)).date())
    InteractionsOnOnTargetUsers = InteractionsOnOnTargetCountSet.filter(
        created__date__gte=(now - timedelta(days=7)).date())



    InteractionsYouGotCountSet =profileDesc.objects.filter(owner=userId)
    number=1
    InteractionsYouGotOnMonth=[]
    while number <= 12:
        data=InteractionsYouGotCountSet.filter(created__month=number).aggregate(Sum('totalInteractionsyouGot'))
        if data['totalInteractionsyouGot__sum'] is None:
            InteractionsYouGotOnMonth.append(0)
        else :
            InteractionsYouGotOnMonth.append(data['totalInteractionsyouGot__sum'])
        number = number + 1


    viewsCount = [element * 2 for element in InteractionsYouGotOnMonth]

    return render(request, 'targeting.html', {'TargetList':TargetList,
                                              'InteractionsOnOnTargetUsers':InteractionsOnOnTargetUsers,
                                              'InteractionsYouGotOnMonth':InteractionsYouGotOnMonth,
                                              'viewsCount':viewsCount})



@login_required(login_url='login')
def engagement (request):
    now = timezone.now()
    current_user=request.user
    userId=current_user.id

    InteractionsOnFollowersCountSet =CustomerInteractionsOnFollowers.objects.filter(owner=userId)
    FollowersCountSet =followers.objects.filter(owner=userId)

    FollowersList = FollowersCountSet.filter(created__date__gte=(now - timedelta(days=7)).date())
    InteractionsOnFollowersCount = InteractionsOnFollowersCountSet.filter(
        created__date__gte=(now - timedelta(days=7)).date())

    InteractionsYouGotCountSet = profileDesc.objects.filter(owner=userId)
    number = 1
    InteractionsYouGotOnMonth = []
    while number <= 12:
        data = InteractionsYouGotCountSet.filter(created__month=number).aggregate(Sum('totalInteractionsyouGot'))
        if data['totalInteractionsyouGot__sum'] is None:
            InteractionsYouGotOnMonth.append(0)
        else:
            InteractionsYouGotOnMonth.append(data['totalInteractionsyouGot__sum'])
        number = number + 1

    viewsCount = [element * 2 for element in InteractionsYouGotOnMonth]

    return render(request, 'engagement.html', {'FollowersList': FollowersList,
                                              'InteractionsOnFollowersCount': InteractionsOnFollowersCount,
                                              'InteractionsYouGotOnMonth': InteractionsYouGotOnMonth,
                                              'viewsCount': viewsCount})


@login_required(login_url='login')
def instaConn (request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        print(user_name, password)
        try:
            api = Client(user_name, password)
            user_info = api.user_info(api.authenticated_user_id)["user"]
            postal_code = ""
            city = ""
            address = ""
            username = user_info["username"]
            full_name = user_info["full_name"]

            if "zip" in user_info :
                postal_code = user_info["zip"]
            if "city_name" in user_info:
                city = user_info["city_name"]
            if "address_street" in user_info:
                address = user_info["address_street"]

            print(username, full_name, city, address, postal_code)
            if InstaProfiles.objects.filter(owner_id=request.user.id).count() >0 :
                insta = InstaProfiles.objects.get(owner_id=request.user.id)
                insta.InstagramUserNameCustomer = user_name
                insta.BusinessName = full_name
                insta.InstagramPassword = password
                insta.City = city
                insta.PostalCode= postal_code
                insta.save()
                print("update")
            else:
                insta = InstaProfiles(
                    InstagramUserNameCustomer = user_name,
                    BusinessName = full_name,
                    InstagramPassword = password,
                    City = city,
                    PostalCode= postal_code,
                    owner = request.user
                )
                insta.save()
                print("added")
            return JsonResponse({'err_code': '2', 'description': username})
        except Exception as e:
            if str(e) == 'invalid_user' :
                return JsonResponse({'err_code': '1', 'description': '''<div class="alert alert-warning alert-dismissible fade show" role="alert" style="background-image: none">
                    <strong>Oops!!! </strong><br>Invalid Username. Please provide correct username! 
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                  </div>'''})
                
            elif str(e) == 'bad_password' :
                return JsonResponse({'err_code': '1', 'description': '''<div class="alert alert-warning alert-dismissible fade show" role="alert" style="background-image: none">
                    <strong>Oops!!! </strong><br>Bad Password. Please provide correct password! 
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                  </div>'''})
            else:
                return JsonResponse({'err_code': '1', 'description': '''<div class="alert alert-warning alert-dismissible fade show" role="alert" style="background-image: none">
                    <strong>Oops!!! </strong><br>''' + str(e) + 
                    '''<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                  </div>'''})
    else:
        return render(request, 'instaConn.html', {})

