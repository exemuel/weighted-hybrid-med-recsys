import xml.etree.ElementTree as ET

def parse_xml(path):
    list_tag = []

    tree = ET.parse(path)
    root = tree.getroot()

    for i in root:
        list_tag.append(i.tag)
        # for j in i:
        #     list_tag.append(j)
        #     for k in j:
        #         list_tag.append(k)

    return list_tag

def compare_list(list1, list2):
    print(list1)
    print("\n")
    print(list2)
    print(list1 == list2)

source = ""
filepaths = [".\\data\\dailymed\\prescription\\20090520_aaeffe62-b538-43ca-a3b9-47e28b765d89\\f7d4e8ff-edb0-4e5c-a1b6-72635e9b2e3a.xml",
             ".\\data\\dailymed\\prescription\\20070216_7C6CA6E4-BE08-4BEA-8553-6B3374991A9E\\7C6CA6E4-BE08-4BEA-8553-6B3374991A9E.xml"]

compare_list(parse_xml(filepaths[0]), parse_xml(filepaths[0]))