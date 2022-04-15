import xml.etree.ElementTree as ET
import json
import pprint

def get_recurse(root, indent, list):
    indent += 1

    list.append((indent, root.tag.split("}",1)[1]))
    if len(root)>0:
        for child in root:
            get_recurse(child, indent, list)
    else:
        return
    return list

def split(data):
    dictt = {}
    dict_tmp = {}
    list_tmp = []
    list_subtmp = []
    idt = 0

    for id, val in enumerate(data):
        print(val)
        # print(val)
        if id == 0:
            dict_tmp[val] = {}
        else:
            if val[0] - data[id-1][0] == 1:
                if len(dict_tmp) < 0:
                    dictt = dict_tmp
                    dict_tmp = {}
                    dict_tmp[val] = {}
                else:

            elif val[0] - data[id-1][0] == 0:
                dict_tmp[val] = {}
            else:
                dictt[list(dictt.keys())[0]] = dict_tmp
            
            # dictt[val[0], val[1]] = dictt
        # if id == 0:
        #     dictt[idt, val[1]] = {}
        
        if id == 4:
            break
        
        # if id == 1:
        #     break
        # if id < len(data)-1:
        #     if val[0] == data[id+1][0]:
        #         list_tmp.append(list_subtmp)
        #         list_subtmp = []
        #     elif val[0] - data[id+1][0] == -1:
        #         list_tmp.append(list_subtmp)
        # else:
        #     list_tmp.append(list_subtmp)
    print(dictt)

    d = {}
    # for path in list_tmp:
    #     current_level = d
    #     for part in path:
    #         if part not in current_level:
    #             current_level[part] = {}
    #         current_level = current_level[part]        
    return d

def parse_xml(path):
    # inisialisasi struktur data dict
    dict_tag = {}

    tree = ET.parse(path)
    root = tree.getroot()
    out_path = "log_" + str(path.split("\\")[5].split(".")[0]) + ".txt"

    list=[]
    indent = 0
    list_tag = get_recurse(root, indent, list)

    pp = pprint.PrettyPrinter(depth=4)
    pp.pprint(split(list_tag))

    # list_tmp = [(1,"set"), (2,"set"), (1,"uni")]
    # dict_tmp = {}
    # vt = 0
    # for id, val in enumerate(list_tmp):
    #     if id > 0:
    #         if list_tmp[id][0] - list_tmp[id-1][0] == 1:
    #             vt=0
    #             dict_tmp[(vt,val[1])] = val[1]
    #         elif list_tmp[id][0] - list_tmp[id-1][0] == -1:
    #             vt+=1
    #             dict_tmp[(vt,val[1])] = val[1]
    #     else:
    #         dict_tmp[(vt,val[1])] = val[1]
    # print(dict_tmp)

    # for id1, nilai1 in enumerate(root):
    #     dict_tag2 = {}
    #     for id2, nilai2 in enumerate(nilai1):
    #         dict_tag3 = {}
    #         for id3, nilai3 in enumerate(nilai2):
    #             dict_tag3[id3] = nilai3.tag.split("}",1)[1]
    #         dict_tag2[(id2, nilai2.tag.split("}",1)[1])] = dict_tag3
    #     dict_tag[(id1, nilai1.tag.split("}",1)[1])] = dict_tag2
    
    # pp = pprint.PrettyPrinter(depth=4)
    # pp.pprint(dict_tag)

    # # dict_norm = json.dumps({k: v for k, v in dict_tag.items()})
    # dict_norm = {k[1]: v for k, v in dict_tag.items()}

    # # Serializing json
    # json_object = json.dumps(dict_norm, sort_keys=False, indent=4)
    
    # # Writing to json file
    # with open(out_path, "w") as outfile:
    #     outfile.write(json_object)
    # print("Periksa " + out_path)
    # return dict_norm

def compare_dict(dict1, dict2):
    print("Berkas XML ke-1 dan berkas XML ke-2", "sama" if dict1 == dict2 else "tidak sama")

filepaths = [".\\data\\dailymed\\prescription\\20060131_ABD6ECF0-DC8E-41DE-89F2-1E36ED9D6535\\ABD6ECF0-DC8E-41DE-89F2-1E36ED9D6535.xml",
             ".\\data\\dailymed\\prescription\\20070216_7C6CA6E4-BE08-4BEA-8553-6B3374991A9E\\7C6CA6E4-BE08-4BEA-8553-6B3374991A9E.xml"]

# print(parse_xml(filepaths[0]))
parse_xml(filepaths[0])

# compare_dict(parse_xml(filepaths[0]), parse_xml(filepaths[1]))