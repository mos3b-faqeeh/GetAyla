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




def pic_link(data):
    try:
        num1=0
        Req_json_Data = json.loads(data)
        num1=Req_json_Data['data']['shortcode_media']['owner']['profile_pic_url']
        #print(num1)
    except Exception as e:
        print(e)
    return num1



def followed_by(data):
    try:
        num1=0
        Req_json_Data = json.loads(data)
        num1=Req_json_Data['data']['shortcode_media']['owner']['edge_followed_by']['count']
        #print(num1)
    except Exception as e:
        print(e)
    return num1

def TotalPosts(data):
    try:
        num1=0
        Req_json_Data = json.loads(data)
        num1=Req_json_Data['data']['shortcode_media']['owner']['edge_owner_to_timeline_media']['count']
        #print(num1)
    except Exception as e:
        print(e)
    return num1

def likesAnalyzer(data):

    try:
        num1=0
        Req_json_Data = json.loads(data)

        num1=Req_json_Data['data']['shortcode_media']['edge_media_preview_like']['count']
        #print(num1)


    except Exception as e:
        print(e)
    return num1



def commentsAnalyzer(data):

    try:
        num2=0
        Req_json_Data = json.loads(data)
        num2=Req_json_Data['data']['shortcode_media']['edge_media_to_parent_comment']['count']
        #print(num2)


    except Exception as e:
        print(e)
    return num2













def dashboard (request):
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'jinkstattoosandcoffee.har')  # full path to text.
    data_file = open(file_path , 'r')
    har_parser = HarParser(json.loads(data_file.read()))

    results = []
    counter = 0
    NumComm1 = 0
    NumComm = 0

    NumLikes = 0
    NumLikes1 = 0

    try:
        if har_parser:
            for har in har_parser.har_data['entries']:
                url = har["request"]["url"]
                if "https://www.instagram.com/graphql/query/" in url:
                    print("**************************** NEW DATA***************************")

                    print(har["request"]["url"], "\n")

                    responseData = har["response"]["content"]["text"]
                    # print(NumComm, "\n")
                    NumComm = commentsAnalyzer(responseData)
                    NumLikes = likesAnalyzer(responseData)
                    NumComm1 = NumComm1 + NumComm
                    NumLikes1 = NumLikes1 + NumLikes

                    NumFollowers = followed_by(responseData)
                    NumPosts = TotalPosts(responseData)
                    Pic = pic_link(responseData)

                    # NumComm1=NumComm+NumComm1
                    # NumLikes=likesAnalyzer(responseData)+NumLikes

                    counter = counter + 1

                    results.append(har["request"]["url"])

    except Exception as e:
        print(e)

    print(NumComm1, "\n")
    print(NumLikes1, "\n")

    print(NumFollowers, "\n")
    print(NumPosts, "\n")

    print(Pic, "\n")
    TotalInteraction=NumComm1 + NumLikes1

    return render(request, 'dashboard.html', {'NumComm1':NumComm1,'NumLikes1':NumLikes1,'NumFollowers':NumFollowers,'NumPosts':NumPosts,'Pic':Pic,'TotalInteraction':TotalInteraction})




def targeting (request):
    return render(request, 'targeting.html', {})