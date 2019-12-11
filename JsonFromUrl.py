import urllib.request
import json

    #https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=RS&Season=2018-19&SeasonType=Regular%20Season&StatCategory=blk
    #https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=RS&Season=2018-19&SeasonType=Regular%20Season&StatCategory=stl
    #https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=RS&Season=2018-19&SeasonType=Regular%20Season&StatCategory=tov
    #https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=RS&Season=2018-19&SeasonType=Regular%20Season&StatCategory=fg3m
    #https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=RS&Season=2018-19&SeasonType=Regular%20Season&StatCategory=ftm

def getPointLeaders():
        url = "https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=RS&Season=2019-20&SeasonType=Regular%20Season&StatCategory=pts"
        hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' }
        req = urllib.request.Request(url, headers=hdr)
        response = urllib.request.urlopen(req)
        data = json.loads(response.read())
        print("-----Point Leaders-----")
        for i in range(0,5):
            print (data["resultSet"]["rowSet"][i][2] + ' ' + data["resultSet"]["rowSet"][i][3] + ' ' + str(data["resultSet"]["rowSet"][i][22]))

def getReboundLeaders():
        url = "https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=RS&Season=2019-20&SeasonType=Regular%20Season&StatCategory=reb"
        hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' }
        req = urllib.request.Request(url, headers=hdr)
        response = urllib.request.urlopen(req)
        data = json.loads(response.read())
        print("-----Rebound Leaders-----")
        for i in range(0,5):         
            print (data["resultSet"]["rowSet"][i][2] + ' ' + data["resultSet"]["rowSet"][i][3] + ' ' + str(data["resultSet"]["rowSet"][i][17]))

def getAssistLeaders():
        url = "https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=RS&Season=2019-20&SeasonType=Regular%20Season&StatCategory=ast"
        hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' }
        req = urllib.request.Request(url, headers=hdr)
        response = urllib.request.urlopen(req)
        data = json.loads(response.read())
        print("-----Assist Leaders-----")
        for i in range(0,5):         
            print (data["resultSet"]["rowSet"][i][2] + ' ' + data["resultSet"]["rowSet"][i][3] + ' ' + str(data["resultSet"]["rowSet"][i][18]))


getPointLeaders()
getReboundLeaders()
getAssistLeaders()