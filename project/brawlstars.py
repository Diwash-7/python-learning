#api part

import requests

op = {
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6Ijc4OTc2YWRmLTAxM2MtNDI3ZS1hODFjLWNmMWI2NTdkZjIzMyIsImlhdCI6MTc0Mzk1NDk5NCwic3ViIjoiZGV2ZWxvcGVyLzZhZTlmMjU4LWIxNWQtYmNiNS1mOTMyLTYxZTc3ZGZhYWEyOSIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMjcuMzQuNzMuMTUiXSwidHlwZSI6ImNsaWVudCJ9XX0.ieWAMtvE1lsZoE7Ku1A35zGBsYsQ59yXXVU8LXXJhUpzA1TBJWePl4WQaHGkg6vLfDgi1WMIHHSsKPqfxIricQ"
}
bUrl = "https://api.brawlstars.com/v1"

playerTag='%23P8Q2QJ8P8'
url=f"{bUrl}/players/{playerTag}"
r = requests.get(url, headers=op)


##fun part

if r.status_code==200:
    data= r.json()
    print("🔥 Profile Info:")
    print(f"Name: {data['name']}")
    print(f"Trophies: {data['trophies']}")
    print(f"Club: {data['club']['name'] if 'club' in data else 'No club'}")
    print(f"Exp Level: {data['expLevel']}")


else :
    print(f"connection failed!{r.status_code}")
    print(r.text)