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
    list_out = []
    
    # Packager
    packager = soup.find("representedOrganization").getText().strip()
    
    # Category
    category =  soup.find("code")["displayName"]
    
    drugs = soup.find_all("manufacturedProduct")
    for i in drugs:
        # Name
        name = i.find("name").getText().strip()
        
        # Item Code (Source)
        item_code = i.find("code")["displayName"] + ":" + i.find("code")["code"]
        numerator_unit = i.find("numerator")["unit"]
        numerator_value = i.find("numerator")["value"]

        # Route of Administration
        administration = i.find("consumedIn").find("routeCode")["displayName"]

        # Active Ingredient/Active Moiety
        list_activeIngredient = [e.find("name").getText().strip() for e in i.find_all("activeIngredientSubstance")]
        
        # Inactive Ingredient
        list_inactiveIngredient = [e.getText().strip() for e in i.find_all("inactiveIngredientSubstance")]
        
        # Color
        color = [e.getText().strip() for e in i.find_all("characteristic") if "SPLCOLOR" in str(e)]

        # Score
        score = [e.find("value")["value"]  for e in i.find_all("characteristic") if "SPLSCORE" in str(e)]

        # Shape
        shape = [e.getText().strip() for e in i.find_all("characteristic") if "SPLSHAPE" in str(e)]

        # Size
        size = [e.find("value")["value"] + " " + e.find("value")["unit"] for e in i.find_all("characteristic") if "SPLSIZE" in str(e)][0]

        # Imprint Code
        imprint = [e.getText().strip() for e in i.find_all("characteristic") if "SPLIMPRINT" in str(e)][0]
        
        # Coating
        coating = [e.find("value")["value"] for e in i.find_all("characteristic") if "SPLCOATING" in str(e)][0]

        # Symbol
        symbol = [e.find("value")["value"] for e in i.find_all("characteristic") if "SPLSYMBOL" in str(e)][0]

        # Packaging Item Code
        pack_item_code = i.find("containerPackagedMedicine").find("code")["code"] + ":" + i.find("containerPackagedMedicine").find("code")["displayName"]

        # Packaging Package Description
        p_amt = i.find("asContent").find("translation")["value"] + " " + i.find("asContent").find("translation")["displayName"]
        p_frm = i.find("containerPackagedMedicine").find("formCode")["displayName"]
        pack_description = p_amt + " in " + p_frm

        list_tmp = [packager, category, name, numerator_unit, numerator_value, 
                    item_code, administration, list_activeIngredient, 
                    list_inactiveIngredient, color, score, shape, size, 
                    imprint, coating, symbol,  pack_item_code, pack_description]
        list_out.append(list_tmp)

    return list_out

def main():
    # # path to folder which needs to be zipped
    # directory = '.\\data\\dailymed\\prescription'

    # # calling function to get all file paths in the directory
    # file_paths = get_all_file_paths(directory)

    # demo
    # x = "data\\dailymed\\prescription\\20060131_dffb4544-0e47-40cd-9baa-d622075838cc\\dffb4544-0e47-40cd-9baa-d622075838cc.xml"
    x = "data\\dailymed\\prescription\\20060131_ABD6ECF0-DC8E-41DE-89F2-1E36ED9D6535\\ABD6ECF0-DC8E-41DE-89F2-1E36ED9D6535.xml"
    
    columns = ["packager", "category", "name", "numerator_unit", "numerator_value", 
                    "item_code", "administration", "active_ingredient", 
                    "inactive_ingredient", "color", "score", "shape", "size", 
                    "imprint", "coating", "symbol",  "pack_item_code", "pack_description"]
    df_drugs = pd.DataFrame(columns=columns)

    lt = read_xml_file(x)
    for i in lt:
        df_drugs.loc[len(df_drugs)] = i
    print(df_drugs)
    
if __name__ == "__main__":
    main()