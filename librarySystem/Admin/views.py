from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,Group
from rest_framework.renderers import TemplateHTMLRenderer


class AdminObjectViewset(viewsets.ViewSet):
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'loginPage.html'

#login method for admin
    @action(methods=["post"], detail=False)
    def loginAdmin(self, request):
        dic={}
        dic['status'] = 200              #for Ui purpose to check if the api call is successful
        user = authenticate(username=request.data['email'], password=request.data['password'])   #for authentication
        print(user)
        if user is not None:
            print("inside if")
            try:
                login(request, user)
                userObj = User.objects.get(username=request.data['email'])
                sessionKey = request.session.session_key
                dic['data'] = {'userName': request.data['email'],'userEmail':userObj.email,'sessionKey':sessionKey}
            except Exception as e:
                print(e)
                dic['message'] = {"errorCode": "56", "description": "login failed"}
                return Response(data=dic)
            else:
                dic["message"] = "User logged in Successfully!!"
        else:
            dic['message'] = {"errorCode": "56", "description": "login failed"}
            #dic['data'] = {'username':request.data['username']}
        return Response(data=dic)

    @action(methods=["post"], detail=False)
    def signUpAdmin(self, request):
        dic = {}
        dic['status'] = 200
        rowJson = request.data
        try:
            #check if email already exists
            objmail = User.objects.filter(username=rowJson['email']).exists()
            if objmail == True:
                dic["message"] = "Email Already exists"
                return Response(data=dic)
            #create user in application
            user = User.objects.create_user(username=rowJson["email"], email=rowJson["email"], password=rowJson["password"],is_staff = True,is_superuser = True)
        except Exception as e:
            print(e)
            dic['message'] = {"errorCode": "56", "description": "login failed"}
        else:
            dic["message"] = "User sign up is successful!!"
        return Response(data=dic)

