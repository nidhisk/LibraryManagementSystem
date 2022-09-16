from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.contrib.sessions.models import Session
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import Http404, HttpResponse
# from Thermax.Thermaxbsc.models import Infrastructure
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from bookManagement.models import book
from django.http import HttpResponse
from django.template import loader


# from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. Welcome to the book management system.")

class bookViewset(viewsets.ViewSet):

#to save the book details
    @action(methods=["post"], detail=False)
    def saveBook(self, request):
        dic = {}
        dic['status'] = 200
        rowJson = request.data
        try :
             bookObj = book.objects.create(book_name = rowJson['book_name'],
                                        author = rowJson['author'],
                                        category = rowJson['category'])
        except Exception as e:
            print(e)
            dic['message'] = {"errorCode": "12", "description": "Failed to save book"}
        return Response(data=dic)

#list of books
    @action(methods=["get"], detail=False)
    def listBook(self, request):
        dic = {}
        dic['status'] = 200
        rowJson = request.data
        try :
            bookObj = list(book.objects.filter().values())
            print(bookObj)
            dic["dataList"] = bookObj
        except Exception as e:
            print(e)
            dic['message'] = {"errorCode": "12", "description": "list error for book"}
        return Response(data=dic)
        
#get book datails using book_code
    @action(methods=["post"], detail=False)
    def getBook(self, request):
        dic = {}
        dic['status'] = 200
        rowJson = request.data
        print("rowJson")
        try :
            data = list(book.objects.filter(book_id=rowJson['book_id']).values())
            print(data)
            dic = data
        except Exception as e:
            print(e)
            dic['message'] = {"errorCode": "12", "description": "list error for book"}
        return Response(data=dic)
        
#update book code using book code
    @action(methods=["post"], detail=False)
    def updateBook(self, request):
        dic = {}
        dic['status'] = 200
        rowJson = request.data
        try :
            bookObj = book.objects.get(book_id = rowJson["book_id"])
            bookObj.book_name = rowJson["book_name"]
            bookObj.author = rowJson["author"]
            bookObj.category = rowJson["category"]
            bookObj.save()
        except Exception as e:
            print(e)
            dic['message'] = {"errorCode": "12", "description": "Failed to update book"}
        return Response(data=dic)

#delete bokk
    @action(methods=["post"], detail=False)
    def deleteBook(self, request):
        dic = {}
        dic['status'] = 200
        rowJson = request.data
        try:
            bookObj =book.objects.filter(book_id=rowJson['book_id']).delete()
        except Exception as e:
            print(e)
            dic['message'] = {"errorCode": "12", "description": "Failed to delete book"}
        return Response(data=dic)



