import xml.etree.ElementTree as ET
import json

def parse_xml(path):
    # inisialisasi struktur data dictionary
    dict_tag = {}

    tree = ET.parse(path)
    root = tree.getroot()

    for nilai in root:
        dict_tag2 = {}
        for nilai2 in nilai: 
            dict_tag3 = {}
            for nilai3 in nilai2:
                dict_tag4 = {}
                for nilai4 in nilai3:
                    dict_tag5 = {}
                    for nilai5 in nilai4:
                        dict_tag6 = {}
                        for nilai6 in nilai5:
                            dict_tag7 = {}
                            for nilai7 in nilai6:
                                dict_tag8 = {}
                                for nilai8 in nilai7:
                                    dict_tag9 = {}
                                    for nilai9 in nilai8:
                                        dict_tag10 = {}
                                        for nilai10 in nilai9:
                                            dict_tag10[nilai10.tag.split("}",1)[1]] = nilai10.tag.split("}",1)[1]
                                        dict_tag9[nilai9.tag.split("}",1)[1]] = dict_tag10
                                    dict_tag8[nilai8.tag.split("}",1)[1]] = dict_tag9
                                dict_tag7[nilai7.tag.split("}",1)[1]] = dict_tag8
                            dict_tag6[nilai6.tag.split("}",1)[1]] = dict_tag7
                        dict_tag5[nilai5.tag.split("}",1)[1]] = dict_tag6
                    dict_tag4[nilai4.tag.split("}",1)[1]] = dict_tag5
                dict_tag3[nilai3.tag.split("}",1)[1]] = dict_tag4
            dict_tag2[nilai2.tag.split("}",1)[1]] = dict_tag3
        dict_tag[nilai.tag.split("}",1)[1]] = dict_tag2

    print(json.dumps(dict_tag, sort_keys=False, indent=4))
    return dict_tag

def compare_dict(dict1, dict2):
    print("Berkas XML ke-1 dan berkas XML ke-2", "sama" if dict1 == dict2 else "tidak sama")

source = ""
filepaths = [".\\data\\dailymed\\prescription\\20090520_aaeffe62-b538-43ca-a3b9-47e28b765d89\\f7d4e8ff-edb0-4e5c-a1b6-72635e9b2e3a.xml",
             ".\\data\\dailymed\\prescription\\20070216_7C6CA6E4-BE08-4BEA-8553-6B3374991A9E\\7C6CA6E4-BE08-4BEA-8553-6B3374991A9E.xml"]

compare_dict(parse_xml(filepaths[0]), parse_xml(filepaths[1]))