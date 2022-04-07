# standard libraries
import os

# 3rd party libraries
from zipfile import ZipFile
import pandas as pd
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

def get_all_file_paths(directory):
    # initializing empty file paths list
    file_paths = []

    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # keep xml files
            if filename.endswith(".xml"):
                # join the two strings in order to form the full filepath
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)

    # returning all file paths
    return file_paths

def read_xml_file(file):
    infile = open(file, "r")
    contents = infile.read()
    soup = BeautifulSoup(contents, "xml")
    
    # Packager
    packager = soup.find("representedOrganization").getText().strip()
    
    # Category
    category =  soup.find("code")["displayName"]
    
    drugs = soup.find_all("manufacturedProduct")
    for i in drugs:
        name = i.find("name").getText().strip()
        code1 = i.find("code")["displayName"]
        code2 = i.find("code")["code"]
        item_code = code1+":"+code2
        numerator_unit = i.find("numerator")["unit"]
        numerator_value = i.find("numerator")["value"]

        administration = i.find("consumedIn").find("routeCode")["displayName"]
        print(name, numerator_unit, numerator_value, item_code, administration)

def main():
    # # path to folder which needs to be zipped
    # directory = '.\\data\\dailymed\\prescription'

    # # calling function to get all file paths in the directory
    # file_paths = get_all_file_paths(directory)

    # print(file_paths[1])
    # x = "data\\dailymed\\prescription\\20060131_dffb4544-0e47-40cd-9baa-d622075838cc\\dffb4544-0e47-40cd-9baa-d622075838cc.xml"
    x = "data\\dailymed\\prescription\\20060131_ABD6ECF0-DC8E-41DE-89F2-1E36ED9D6535\\ABD6ECF0-DC8E-41DE-89F2-1E36ED9D6535.xml"
    
    read_xml_file(x)
    
if __name__ == "__main__":
    main()