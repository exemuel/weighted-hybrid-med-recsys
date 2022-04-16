import xml.etree.ElementTree as ET
import json
import pprint
import copy

def save_tags(path, text):
    with open(path, 'a') as f:
        f.write("\n"+text)

def get_recurse(root, indent, out_list, outfilepath):
    indent += 2

    save_tags(outfilepath, " "*indent+root.tag.split("}",1)[1])
    out_list.append(root.tag.split("}",1)[1])
    if len(root)>0:
        for child in root:
            get_recurse(child, indent, out_list, outfilepath)
    else:
        return
    
    return out_list

def parse_xml(path):
    tree = ET.parse(path)
    root = tree.getroot()
    out_path = "log-" + str(path.split("\\")[5].split(".")[0]) + ".txt"

    indent = 0
    tlist = []
    list_tag = get_recurse(root, indent, tlist, out_path)
    
    return list_tag

def compare_dict(dict1, dict2):
    print("Berkas XML ke-1 dan berkas XML ke-2", "sama" if dict1 == dict2 else "tidak sama")

filepaths = [".\\data\\dailymed\\prescription\\20060131_ABD6ECF0-DC8E-41DE-89F2-1E36ED9D6535\\ABD6ECF0-DC8E-41DE-89F2-1E36ED9D6535.xml",
             ".\\data\\dailymed\\prescription\\20070216_7C6CA6E4-BE08-4BEA-8553-6B3374991A9E\\7C6CA6E4-BE08-4BEA-8553-6B3374991A9E.xml"]

compare_dict(parse_xml(filepaths[0]), parse_xml(filepaths[1]))