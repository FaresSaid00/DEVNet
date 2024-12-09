import yaml

with open('/Users/engfares/Desktop/DevNet/myfile.yaml', 'r') as yaml_file:  # استخدام المسار الصحيح
    data = yaml.safe_load(yaml_file)
    print(data)

