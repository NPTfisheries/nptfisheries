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
    url = 'https://www.cbr.washington.edu/dart/cs/php/rpt/adult_annual.php?sc=1&outputFormat=csv&proj=LWG&startdate=1%2F1&enddate=12%2F31&run='
    response=requests.get(url)
    content = response.content
    parsed = content.decode()
    df = StringIO(parsed)
    data = pd.read_csv(df, skipfooter=14)
    data.columns = data.columns.str.replace(' ','')
    json_df = data.reset_index().to_json(orient='records')
    json_data = []
    json_data = json.loads(json_df)
    context = {'data': json_data}
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