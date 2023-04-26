# data/views.py
from django.shortcuts import render
import requests
import urllib
import pandas as pd
import json
from io import StringIO
import environ

# Create your views here.

# def spsm_status(request):
#     env = environ.Env()
#     environ.Env.read_env()
#     username = env('CREDENTIALS')
#     password = env('CREDENTIALS')
#     host = 'https://npt-cdms.nezperce.org/services/api/v1/'
#     login = 'account/login'
#     creds = {'username':username, 'password':password}
#     s = requests.Session()
#     auth = s.post(url = host+login, data = creds)

#     # spp = 'Summer Steelhead'
#     url = 'npt/getlgrescapement'
#     # payload = {'SpeciesRun':spp}
#     # params = urllib.parse.urlencode(payload, quote_via=urllib.parse.quote)
#     req = s.get(url = host+url)
#     data = req.json()
#     df = pd.DataFrame.from_dict(data)

#     df_chn = df[df['SpeciesRun']=='Spring/Summer Chinook Salmon']
#     df_chn_sub = df_chn[["SpeciesRun", "RunYear", "Total_Adults", "Count_WildAdults", "Count_HatcheryAdults"]]
#     df_chn_sub['wfrac'] = (df_chn_sub['Count_WildAdults']/df_chn_sub['Total_Adults'])*100

#     chn_json = df_chn_sub.to_json(orient='records')

#     df_sth = df[df['SpeciesRun']=='Summer Steelhead']
#     df_sth_sub = df_sth[["SpeciesRun", "RunYear", "Total_Adults"]]
#     sth_json = df_sth_sub.to_json(orient='records')

#     context = {'chn_data':chn_json, 'sth_data':sth_json}
#     return render(request, "data/spsm_status.html", context)

def spsm_inseason(request):
    CY = '2022'
    spp = 'Chinook'

    # get DART window counts
    #url = 'https://www.cbr.washington.edu/dart/cs/php/rpt/adult_daily.php?sc=1&outputFormat=csv&year=2023&proj=LWG&span=no&startdate=1%2F1&enddate=12%2F31&run=&syear=2023&eyear=2023'
    url = 'https://www.cbr.washington.edu/dart/cs/php/rpt/adult_daily.php?sc=1&outputFormat=csv&year='+CY+'&proj=LWG&span=no&startdate=1%2F1&enddate=12%2F31&run=&syear='+CY+'&eyear='+CY
    response=requests.get(url)
    content = response.content
    parsed = content.decode()
    df = StringIO(parsed)
    full = pd.read_csv(df)
    data = full.drop(full.tail(23).index)
    #nrows = full.shape[0]-23
    #data = full.iloc[:nrows]
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
    url = 'npt/gettrapcounts'
    payload = {'Species':spp, 'CalendarYear':CY}
    print(payload)
    params = urllib.parse.urlencode(payload, quote_via=urllib.parse.quote)
    print(params)
    req = s.get(url = host+url, params=params)
    data_dict= json.loads(req.text)
    
    if data_dict is not None:
        df = pd.DataFrame(data_dict)
        df['WeekStart'] = pd.to_datetime(df['WeekStart'])
        df['WeekStart'] = df['WeekStart'].dt.strftime('%m/%d').astype(str)
    
        df['WeekEnd'] = pd.to_datetime(df['WeekEnd'])
        df['WeekEnd'] = df['WeekEnd'].dt.strftime('%m/%d').astype(str)
        df['TrapDates'] = df['WeekStart'] + ' - ' + df['WeekEnd']
        
        group_name = ('Rapid River Fish Trap', 'South Fork Salmon River')
        rapid_df = df.loc[df['Trap'].isin(group_name)]
        trap_rapid = rapid_df.to_dict(orient='records')

        summary = df.groupby(['Facility', 'Trap', 'Species', 'Run', 'Origin']).agg({'TotalCount': 'sum'}).reset_index()
        trap_data = summary.to_dict(orient='records')
    else:
        trap_rapid = []
        trap_data = []
    
    # get harvest data
    url = 'npt/getharvestests'
    #payload = {'Species':spp, 'CalendarYear':CY}
    payload = {'StatYear':CY}
    print(payload)
    params = urllib.parse.urlencode(payload, quote_via=urllib.parse.quote)
    req = s.get(url = host+url, params=params)
    harvest_data = req.json()

    context = {'year':CY, 'data': json_data, 'dates':dates, 'values':values, 'trap_data': trap_data, 'trap_rapid':trap_rapid, 'harvest_data':harvest_data}
    return render(request, 'data/spsm_inseason.html', context)