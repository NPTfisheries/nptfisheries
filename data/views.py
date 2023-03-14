# data/views.py
from django.shortcuts import render
import requests
import urllib
import pandas as pd
import json
from io import StringIO
import environ

# Create your views here.

def esu_status(request):
    env = environ.Env()
    environ.Env.read_env()
    username = env('CREDENTIALS')
    password = env('CREDENTIALS')
    host = 'https://npt-cdms.nezperce.org/services/api/v1/'
    login = 'account/login'
    creds = {'username':username, 'password':password}
    s = requests.Session()
    auth = s.post(url = host+login, data = creds)

    # spp = 'Summer Steelhead'
    url = 'npt/getlgrescapement'
    # payload = {'SpeciesRun':spp}
    # params = urllib.parse.urlencode(payload, quote_via=urllib.parse.quote)
    req = s.get(url = host+url)
    data = req.json()
    df = pd.DataFrame.from_dict(data)

    df_chn = df[df['SpeciesRun']=='Spring/Summer Chinook Salmon']
    df_chn_sub = df_chn[["SpeciesRun", "RunYear", "Total_Adults", "Count_WildAdults", "Count_HatcheryAdults"]]
    df_chn_sub['wfrac'] = (df_chn_sub['Count_WildAdults']/df_chn_sub['Total_Adults'])*100

    chn_json = df_chn_sub.to_json(orient='records')

    df_sth = df[df['SpeciesRun']=='Summer Steelhead']
    df_sth_sub = df_sth[["SpeciesRun", "RunYear", "Total_Adults"]]
    sth_json = df_sth_sub.to_json(orient='records')

    context = {'chn_data':chn_json, 'sth_data':sth_json}
    return render(request, "data/esu_status.html", context)

def window_counts(request):
    # get DART window counts
    url = 'https://www.cbr.washington.edu/dart/cs/php/rpt/adult_daily.php?sc=1&outputFormat=csv&year=2022&proj=LWG&span=no&startdate=1%2F1&enddate=12%2F31&run=&syear=2023&eyear=2022'
    response=requests.get(url)
    content = response.content
    parsed = content.decode()
    df = StringIO(parsed)
    full = pd.read_csv(df)
    data = full.drop(range(305,327))
    data['Chin'] = data['Chin'].fillna(0)
    dates = list(data["Date"])
    values = [float(i) for i in list(data["Chin"])]
    json_data = data.to_json()

    # login to CDMS
    env = environ.Env()
    environ.Env.read_env()
    username = env('CREDENTIALS')
    password = env('CREDENTIALS')
    host = 'https://npt-cdms.nezperce.org/services/api/v1/'
    login = 'account/login'
    creds = {'username':username, 'password':password}
    s = requests.Session()
    auth = s.post(url = host+login, data = creds)

    # get trap counts
    spp = 'Chinook'
    url = 'npt/gettrapcounts'
    payload = {'Species':spp, 'CalendarYear':2022}
    print(payload)
    params = urllib.parse.urlencode(payload, quote_via=urllib.parse.quote)
    print(params)
    req = s.get(url = host+url, params=params)
    trap_data = req.json()

    # get harvest data
    url = 'npt/getharvestests'
    req = s.get(url = host+url)
    harvest_data = req.json()

    context = {'data': json_data, 'dates':dates, 'values':values, 'trap_data': trap_data, 'harvest_data':harvest_data}
    return render(request, 'data/window_counts.html', context)

def weir_counts(request):
    env = environ.Env()
    environ.Env.read_env()
    username = env('CREDENTIALS')
    password = env('CREDENTIALS')
    host = 'https://npt-cdms.nezperce.org/services/api/v1/'
    login = 'account/login'
    creds = {'username':username, 'password':password}
    s = requests.Session()
    auth = s.post(url = host+login, data = creds)

    spp = 'Chinook'
    url = 'npt/gettrapcounts'
    payload = {'Species':spp, 'CalendarYear':2022}
    print(payload)
    params = urllib.parse.urlencode(payload, quote_via=urllib.parse.quote)
    print(params)
    req = s.get(url = host+url, params=params)
    data = req.json()
    context = {'data':data}
    return render(request, "data/weir_counts.html", context)

def harvest_counts(request):
    env = environ.Env()
    environ.Env.read_env()
    username = env('CREDENTIALS')
    password = env('CREDENTIALS')
    host = 'https://npt-cdms.nezperce.org/services/api/v1/'
    login = 'account/login'
    creds = {'username':username, 'password':password}
    s = requests.Session()
    auth = s.post(url = host+login, data = creds)

    url = 'npt/getharvestests'
    req = s.get(url = host+url)
    data = req.json()
    context = {'data':data}
    return render(request, 'data/harvest_counts.html', context)