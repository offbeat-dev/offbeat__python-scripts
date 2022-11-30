import json

newLines = []

# Read Existing JSON File
with open('data.json') as f:
    lines = f.readlines()
# Modify JSON File
    for line in lines:
        data = json.loads(line)
        print(data)
        geolocObj = {'lat': data['latitude'], 'lng': data['longitude']}
        data['_geoloc'] = geolocObj
        if 'latitude' in data: 
          del data['latitude']
        if 'longitude' in data: 
          del data['longitude']
        newLines.append(data)
with open('datanew.json', 'w') as f:
     json.dump(newLines, f, indent=2)

f.close()