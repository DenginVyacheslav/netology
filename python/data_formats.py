import json
import xml.etree.ElementTree as ET


def rating(file):
    word_rating = {}
    for w in tuple(file):
        word_rating[w] = file.count(w)
    return dict(sorted(word_rating.items(), reverse=True, key=lambda item: item[1]))


with open('newsafr.json', encoding='utf-8') as fj:
    data = json.load(fj)

word_json = []
for n in range(0, len(data['rss']['channel']['items'])):
    for i in data['rss']['channel']['items'][n]['description'].split(' '):
        if len(i) > 6:
            word_json.append(i)

word_rat_json = rating(word_json)

for num, k in enumerate(word_rat_json.items()):
    if num == 10:
        break
    else:
        print(num+1, *k)

print("\n====================================\n")

parser = ET.XMLParser(encoding='utf-8')
tree = ET.parse('newsafr.xml', parser)
root = tree.getroot()
xml_title = root.findall('channel/item')

word_xml = []
for xml in xml_title:
    for i in xml.find('description').text.split(' '):
        if len(i) > 6:
            word_xml.append(i)

word_rat_xml = rating(word_xml)

for num, k in enumerate(word_rat_xml.items()):
    if num == 10:
        break
    else:
        print(num+1, *k)
