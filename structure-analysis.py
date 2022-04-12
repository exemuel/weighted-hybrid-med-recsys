import xml.etree.ElementTree as ET
import json

def parse_xml(path):
    # inisialisasi struktur data list
    list_tag = []

    tree = ET.parse(path)
    root = tree.getroot()
    out_path = "log_" + str(path.split("\\")[5].split(".")[0]) + ".txt"

    with open(out_path, 'w') as log:
        for nilai1 in root:
            log.write(nilai1.tag.split("}",1)[1] + '\n')
            list_tag.append(nilai1)
            for nilai2 in nilai1:
                log.write("\t"*1 + nilai2.tag.split("}",1)[1] + '\n')
                list_tag.append(nilai2)
                for nilai3 in nilai2:
                    log.write("\t"*2 + nilai3.tag.split("}",1)[1] + '\n')
                    list_tag.append(nilai3)
                    for nilai4 in nilai3:
                        log.write("\t"*3 + nilai4.tag.split("}",1)[1] + '\n')
                        list_tag.append(nilai4)
                        for nilai5 in nilai4:
                            log.write("\t"*4 + nilai5.tag.split("}",1)[1] + '\n')
                            list_tag.append(nilai5)
                            for nilai6 in nilai5:
                                log.write("\t"*5 + nilai6.tag.split("}",1)[1] + '\n')
                                list_tag.append(nilai6)
                                for nilai7 in nilai6:
                                    log.write("\t"*6 + nilai7.tag.split("}",1)[1] + '\n')
                                    list_tag.append(nilai7)
                                    for nilai8 in nilai7:
                                        log.write("\t"*7 + nilai8.tag.split("}",1)[1] + '\n')
                                        list_tag.append(nilai8)
                                        for nilai9 in nilai8:
                                            log.write("\t"*8 + nilai9.tag.split("}",1)[1] + '\n')
                                            list_tag.append(nilai9)
                                            for nilai10 in nilai9:
                                                log.write("\t"*9 + nilai10.tag.split("}",1)[1] + '\n')
                                                list_tag.append(nilai10)
                                                for nilai11 in nilai10:
                                                    log.write("\t"*10 + nilai11.tag.split("}",1)[1] + '\n')
                                                    list_tag.append(nilai11)
                                                    for nilai12 in nilai11:
                                                        log.write("\t"*11 + nilai12.tag.split("}",1)[1] + '\n')
                                                        list_tag.append(nilai12)
                                                        for nilai13 in nilai12:
                                                            log.write("\t"*12 + nilai13.tag.split("}",1)[1] + '\n')
                                                            list_tag.append(nilai13)

    print("Periksa " + out_path)
    return list_tag

def compare_list(list1, list2):
    print("Berkas XML ke-1 dan berkas XML ke-2", "sama" if list1 == list2 else "tidak sama")

filepaths = [".\\data\\dailymed\\prescription\\20060131_ABD6ECF0-DC8E-41DE-89F2-1E36ED9D6535\\ABD6ECF0-DC8E-41DE-89F2-1E36ED9D6535.xml",
             ".\\data\\dailymed\\prescription\\20070216_7C6CA6E4-BE08-4BEA-8553-6B3374991A9E\\7C6CA6E4-BE08-4BEA-8553-6B3374991A9E.xml"]

compare_list(parse_xml(filepaths[0]), parse_xml(filepaths[1]))