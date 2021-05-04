from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
import db.connect_DB as connect_DB
#import db.connect_DB_local as connect_DB
import json as json

class Index(View):

    def get(self, request):
     
        return HttpResponse("<h1>서버 점검 중입니다.</h1><br><h2>잠시 후 다시 진행해 주세요</h2> ")
 
class IndexView(View):

    def get(self, request, channel):
        page_title = '서버 점검'
        resdata = connect_DB.servercheck_list(channel)
        return render(request, 'main_template/checkingserver.html',{'title':page_title,'channel':channel, 'maindata':resdata[0], 'listdata':resdata})
    
class IndexViewwithapp(View):

    def get(self, request, channel, appname):
        page_title = '서버 점검'
        resdata = connect_DB.servercheck_list_withapp(channel, appname)
        return render(request, 'main_template/checkingserver.html',{'title':page_title,'channel':channel, 'maindata':resdata[0], 'listdata':resdata})

class CheckSeverAPI(View):

    def get(self, request, channel):
        
        checkdata = connect_DB.check_servercheck(channel)
        print(json.dumps(checkdata))
        return HttpResponse(json.dumps(checkdata))

class CheckSeverAPIwithapp(View):

    def get(self, request, channel, appname):
        
        print(channel)
        print(appname)
        checkdata = connect_DB.check_servercheck_withapp(channel, appname)
        print(json.dumps(checkdata))
        return HttpResponse(json.dumps(checkdata))

class ContentView(View):

    def get(self, request, channel, id):
        page_title = '서버 점검 테스트'
        resdata = connect_DB.servercheck_content(id)
        resdata[0]['content'] = resdata[0]['content'].replace("\n", "<br>")
        return render(request, 'main_template/content.html',{'title':page_title,'channel':channel, 'maindata':resdata[0]})
