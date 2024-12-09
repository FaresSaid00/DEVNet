import json

with open('/Users/engfares/Desktop/DevNet/myfile.json', 'r') as json_file:  # استخدام المسار الصحيح
    data = json.load(json_file)
    print(data)
