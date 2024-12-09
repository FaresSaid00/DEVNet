import xml.etree.ElementTree as ET

xml = ET.parse('/Users/engfares/Desktop/DevNet/myfile.xml')  # استخدام المسار الصحيح
root = xml.getroot()
print(root.tag, root.attrib)
