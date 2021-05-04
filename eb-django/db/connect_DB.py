# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 15:37:02 2018

@author: LYJ
"""

import pandas as pd
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from django.db import connection as conn

def check_servercheck(channel) :

    sql = """SELECT count(*) cnt FROM table where type = 1 and now() >= start_time and now() <= end_time and (channel = '{}' or channel = 'all') order by id asc limit 1""".format(channel)
    cursor = conn.cursor()
    cursor.execute(sql)                 
    resdata = cursor.fetchall()
    
    #print(sql)
    for row in resdata:
        servertype = 0
        if row[0] > 0 :
            servertype = 1
        dic = {"time":0.001,"result":1,"code":1000,"data":{"server_check":servertype}}

    conn.close()
    return dic

def check_servercheck_withapp(channel, appname) :

    sql = """SELECT count(*) cnt FROM table where type = 1 and now() >= start_time and now() <= end_time and ((channel = '{}' and app_channel = '{}') or (channel = 'all' and app_channel = '{}') or (channel = '{}' and app_channel = 'all') or (channel = 'all' and app_channel = 'all')) order by id asc limit 1""".format(channel, appname, appname, channel)
    cursor = conn.cursor()
    cursor.execute(sql)                 
    resdata = cursor.fetchall()
    
    print(sql)
    for row in resdata:
        servertype = 0
        if row[0] > 0 :
            servertype = 1
        dic = {"time":0.001,"result":1,"code":1000,"data":{"server_check":servertype}}

    conn.close()
    return dic

def servercheck_list(channel) :

    sql = """SELECT title, content, date_format(start_time,'%Y년 %m월 %d일 %H시 %i분') start_time, date_format(end_time,'%m월 %d일 %H시 %i분') end_time, type, channel, id, date_format(end_time,'%Y년 %m월 %d일 %H시 %i분') end_time_main FROM table where (channel = '{}' or channel = 'all') order by id desc""".format(channel)
    cursor = conn.cursor()
    cursor.execute(sql)                 
    resdata = cursor.fetchall()
    posts =[]
    index = 1
    print(sql)
    for row in resdata:

        dic = {'index':index, 'title':row[0], 'content':row[1], 'start_time':row[2], 'end_time':row[3], "type":row[4], "channel":row[5], "id":row[6], "end_time_main":row[7]}
        posts.append(dic)
        index+=1

    conn.close()
    return posts 

def servercheck_list_withapp(channel, appname) :

    sql = """SELECT title, content, date_format(start_time,'%Y년 %m월 %d일 %H시 %i분') start_time, date_format(end_time,'%m월 %d일 %H시 %i분') end_time, type, channel, id, date_format(end_time,'%Y년 %m월 %d일 %H시 %i분') end_time_main  FROM table where ((channel = '{}' and app_channel = '{}') or (channel = 'all' and app_channel = '{}') or (channel = '{}' and app_channel = 'all') or (channel = 'all' and app_channel = 'all')) order by id desc""".format(channel, appname, appname, channel)
    cursor = conn.cursor()
    cursor.execute(sql)                 
    resdata = cursor.fetchall()
    posts =[]
    index = 1
    print(sql)
    for row in resdata:

        dic = {'index':index, 'title':row[0], 'content':row[1], 'start_time':row[2], 'end_time':row[3], "type":row[4], "channel":row[5], "id":row[6], "end_time_main":row[7]}
        posts.append(dic)
        index+=1

    conn.close()
    return posts

def servercheck_content(id) :

    sql = """SELECT title, content, date_format(start_time,'%Y년 %m월 %d일 %H시 %i분') start_time, date_format(end_time,'%m월 %d일 %H시 %i분') end_time, type, channel, id, created_time FROM table where id = '{}'  order by id desc""".format(id)
    cursor = conn.cursor()
    cursor.execute(sql)                 
    resdata = cursor.fetchall()
    posts =[]
    index = 1
    print(sql)
    for row in resdata:

        dic = {'index':index, 'title':row[0], 'content':row[1], 'start_time':row[2], 'end_time':row[3], "type":row[4], "channel":row[5], "id":row[6], "created_time":row[7]}
        posts.append(dic)
        index+=1

    conn.close()
    return posts 
