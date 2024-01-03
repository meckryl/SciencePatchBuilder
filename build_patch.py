import os
import json

def formatDictionary(d):
    out = "{"
    first = True
    for key, value in d.items():
        if not first:
            out+=", "
        first = False
        out+="\""+key+"\""+": "
        out+= "\""+value+"\"" if isinstance(value, str) else str(value)
    out+= "}"
    return out

default_files = os.listdir("./science_region_default")
updated_files = os.listdir("./science_region_updated")

with open("patches/Science.patch", 'w') as patch_file:
    patch_file.write("@use \"builtin:dictionary\";\n")
    patch_file.write("@use \"builtin:list\";\n")
    patch_file.write("@patch science_region;\n\n")
    patch_file.write(":json science_region {\n")

    for default_file, updated_file in zip(default_files, updated_files):
        default_data = None
        updated_data = None
        with open("./science_region_default/" + default_file, "r") as json_file:
            default_data = json.load(json_file)
        with open("./science_region_updated/" + updated_file, "r") as json_file:
            updated_data = json.load(json_file)

        if default_data != updated_data:
            patch_file.write(f"\t@if $$BodyName == {default_data['BodyName']} "+"{\n")
            for default_situation, updated_situation in zip(default_data["SituationData"], updated_data["SituationData"]):
                if default_data["SituationData"][default_situation] != updated_data["SituationData"][updated_situation]:
                    patch_file.write(f"\t\tSituationData[\"{default_situation}\"]: {updated_data['SituationData'][updated_situation]};\n")

            for index, (default_region, updated_region) in enumerate(zip(default_data["Regions"],updated_data["Regions"])):
                if default_region != updated_region:
                    patch_file.write(f"\t\tRegions[{index}]: {formatDictionary(updated_region)};\n")
            patch_file.write("\t}\n")

    patch_file.write("}")



