# standard libraries
import os
import re

# 3rd party libraries
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from tqdm import tqdm

# function to clean string
def cleaning_string(string):
    # mengganti \n menjadi empty string
    string = string.strip().replace('\n', '')
    # mengganti sekuens whitespace menjadi empty string
    string = re.sub(r"\s\s+" , "", string)
    return string

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

def read_xml_file(filepath):
    infile = open(filepath, "r", encoding="utf8")
    contents = infile.read()
    soup = BeautifulSoup(contents, "xml")
    list_out = []
    
    # Name
    name = "" if soup.find("title") == None else cleaning_string(soup.find("title").getText())
    
    # Packager
    packager = "" if soup.find("representedOrganization") == None else cleaning_string(soup.find("representedOrganization").getText())
    
    # Category
    category =  "" if soup.find("code")["displayName"] == None else soup.find("code")["displayName"]
    
    drugs = soup.find_all("manufacturedProduct")
    for i in drugs:
        # Sub Name
        sub_name = "" if i.find("name") == None else cleaning_string(i.find("name").getText())
        if sub_name is "":
            break
        
        # Item Code (Source)
        item_code = ""
        tmp = i.find("code")
        if tmp.has_attr("displayName"):
            item_code_src = i.find("code")["displayName"] + ":"
        item_code = item_code_src + "" if i.find("code") == None else i.find("code")["code"]
        if item_code is "":
            break

        # Route of Administration
        administration = []
        tmp_a = i.find_all("consumedIn")
        if tmp_a is not None:
            for j in tmp_a:
                tmp_b = j.find("routeCode")
                if tmp_b.has_attr("displayName"):
                    administration.append(tmp_b["displayName"])
        if len(administration) == 0:
            break

        # Active Ingredient/Active Moiety
        list_activeIngredient = []
        tmp_a = i.find_all("activeIngredient")
        if len(tmp_a) is 0:
            tmp_a = i.find_all("ingredient")
            for j in tmp_a:
                if "ACTIB" in str(j):
                    list_tmp = []
                    list_tmp.append(j.find("activeMoiety").getText().strip())
                    list_tmp.append(j.find("numerator")["value"])
                    list_tmp.append(j.find("numerator")["unit"])
                    list_tmp.append(j.find("denominator")["value"])
                    list_tmp.append(j.find("denominator")["unit"])
                    list_activeIngredient.append(list_tmp)
        else:
            for j in tmp_a:
                list_tmp = []
                list_tmp.append(j.find("activeMoiety").getText().strip())
                list_tmp.append("" if j.find("numerator") == None else j.find("numerator")["value"])
                list_tmp.append("" if j.find("numerator") == None else j.find("numerator")["unit"])
                list_tmp.append("" if j.find("denominator") == None else j.find("numerator")["value"])
                list_tmp.append("" if j.find("denominator") == None else j.find("numerator")["unit"])
                list_activeIngredient.append(list_tmp)
        if len(list_activeIngredient) == 0:
            break

        # Inactive Ingredient
        list_inactiveIngredient = []
        tmp_a = "" if i.find_all("ingredient", attrs={"classCode": "IACT"}) == None else i.find_all("ingredient", attrs={"classCode": "IACT"})
        if len(tmp_a) != 0:
            for j in tmp_a:
                list_tmp = []
                list_tmp.append(cleaning_string(j.find("ingredientSubstance").getText()))
                list_tmp.append("" if j.find("numerator") == None else j.find("numerator")["value"])
                list_tmp.append("" if j.find("numerator") == None else j.find("numerator")["unit"])
                list_tmp.append("" if j.find("denominator") == None else j.find("denominator")["value"])
                list_tmp.append("" if j.find("denominator") == None else j.find("denominator")["unit"])
                list_inactiveIngredient.append(list_tmp)
        else:
            tmp_a = "" if i.find_all("inactiveIngredient") == None else i.find_all("inactiveIngredient")
            if len(tmp_a) != 0:
                for j in tmp_a:
                    list_tmp = []
                    list_tmp.append(cleaning_string(j.find("inactiveIngredientSubstance").getText()))
                    list_tmp.append("" if j.find("numerator") == None else j.find("numerator")["value"])
                    list_tmp.append("" if j.find("numerator") == None else j.find("numerator")["unit"])
                    list_tmp.append("" if j.find("denominator") == None else j.find("denominator")["value"])
                    list_tmp.append("" if j.find("denominator") == None else j.find("denominator")["unit"])
                    list_inactiveIngredient.append(list_tmp)
        
        color = ""
        score = ""
        shape = ""
        size = ""
        imprint = ""
        coating = ""
        symbol = ""
        for j in i.find_all("characteristic"):
            list_tmp = []
            # Color
            if "SPLCOLOR" in str(j):
                color = cleaning_string(j.getText())
            
            # Score
            elif "SPLSCORE" in str(j):
                score = j.find("value")["value"]
            
            # Shape
            elif "SPLSHAPE" in str(j):
                shape = cleaning_string(j.getText())

            # Size
            elif "SPLSIZE" in str(j):
                size = j.find("value")["value"]
            
            # Imprint Code
            elif "SPLIMPRINT" in str(j):
                imprint = cleaning_string(j.getText())
            
            # Coating
            elif "SPLCOATING" in str(j):
                coating = j.find("value")["value"]
            
            # Symbol
            elif "SPLSYMBOL" in str(j):
                symbol = j.find("value")["value"]

        # Packaging Item Code
        pack_item_code = ""
        tmp_a = i.find("asContent").find("code")
        if tmp_a != None:
            if tmp_a.has_attr("code"):
                pack_item_code = i.find("asContent").find("code")["code"]

        # Packaging Package Description
        pack_quantity = ""
        pack_unit = ""
        if i.find("asContent").find("quantity") != None:
            pack_quantity = "" if i.find("asContent").find("quantity").find("translation") == None else i.find("asContent").find("quantity").find("translation")["value"]
            pack_unit = "" if i.find("asContent").find("quantity").find("translation") == None else i.find("asContent").find("quantity").find("translation")["displayName"]
        
        pack_container = ""
        if i.find("asContent").find("containerPackagedMedicine") != None:
            pack_container = "" if i.find("containerPackagedMedicine").find("formCode") == None else i.find("containerPackagedMedicine").find("formCode")["displayName"]

        list_tmp = [name, packager, category, sub_name,  
                    item_code, administration, list_activeIngredient, 
                    list_inactiveIngredient, color, score, shape, size, 
                    imprint, coating, symbol, pack_item_code, pack_quantity, pack_unit, pack_container]
        list_out.append(list_tmp)

    return list_out

def make_df_drugs(paths):
    columns = ["name", "packager", "category", "sub_name",  
               "item_code", "administration", "list_activeIngredient", 
               "list_inactiveIngredient", "color", "score", "shape", "size", 
               "imprint", "coating", "symbol", "pack_item_code", "pack_quantity", "pack_unit", "pack_container"]
    df_drugs = pd.DataFrame(columns=columns)

    print("\nMaking Drugs DataFrame in progress...")
    for i in tqdm(paths):
        try:
            list_drug = read_xml_file(i)
        except:
            m = np.empty((1,19,))
            m[:] = np.nan
            list_drug = m.tolist()
        for i in list_drug:
            df_drugs.loc[len(df_drugs)] = i
    return df_drugs

def main():
    # path to folder which needs to be zipped
    directory = '.\\data\\dailymed\\prescription'

    # for debug
    # x =".\\data\\dailymed\\prescription\\20090520_aaeffe62-b538-43ca-a3b9-47e28b765d89\\f7d4e8ff-edb0-4e5c-a1b6-72635e9b2e3a.xml"
    # x = ".\\data\\dailymed\\prescription\\20070216_7C6CA6E4-BE08-4BEA-8553-6B3374991A9E\\7C6CA6E4-BE08-4BEA-8553-6B3374991A9E.xml"
    # x = ".\\data\\dailymed\\prescription\\20090701_89245260-c470-4a4c-8ef6-12598dc28e4c\\279b92ac-8e31-4b04-8983-6f161f5b709c.xml"
    # x = ".\\data\\dailymed\\prescription\\20060131_dffb4544-0e47-40cd-9baa-d622075838cc\\dffb4544-0e47-40cd-9baa-d622075838cc.xml"
    # list_d = read_xml_file(x)
    # print(list_d)

    # calling function to get all file paths in the directory
    file_paths = get_all_file_paths(directory)

    df_drugs = make_df_drugs(file_paths)
    print(df_drugs.head())
    print(df_drugs.tail())

    
if __name__ == "__main__":
    main()