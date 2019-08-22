from django.http import HttpResponse
import requests
import json

res = requests.get("https://api.spacexdata.com/v3/launches")
ls=[]
data = res.json()

for i in data:
    d={}
    fn=i['flight_number']
    rn=i['rocket']['rocket_name']
    mpl=i['links']['mission_patch']
    t=i['launch_date_utc']
    d["flight_number"]=fn
    d["rocket_name"]=rn
    d["mission_patch_link"]=mpl
    d["Launch Date and Time"]=t
    d["Launch Date and Time"]=d["Launch Date and Time"].split("T")
    ls.append(d)



def index(request):
    return HttpResponse(ls)





