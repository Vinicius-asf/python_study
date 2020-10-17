import xml.etree.ElementTree as ET

class Dog():
    def __init__(self, *args, **kwargs):
        self.name = args[0]
        self.size = args[1]
        self.data = args[2]

ann = ET.parse('C:/Annotation/n02085620-Chihuahua/n02085620_7')
root = ann.getroot()
print(root[5][0].text)
# print (ann)