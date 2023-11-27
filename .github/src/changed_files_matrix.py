import os
import json

bash_output = os.environ.get('CHANGED_FILES')

changed_files = list(bash_output.upper().split(" "))

include_dictionary = { "include": [] }

db_schema_set = set()
for item in changed_files:
    if 'MIGRATIONS/' in item:
        db_name = item.split("/")[-3]
        schema_name = item.split("/")[-2]
        # file_name = item.split("/")[-1]
        add_item = f"{db_name}/{schema_name}"
        db_schema_set.add(add_item)

db_schema_list = list(db_schema_set)

for item in db_schema_list:
    folder_location = item
    db_name = item.split("/")[0]
    schema_name = item.split("/")[1]
    add_dict = {
        "folder_location": folder_location
    }

    include_dictionary["include"].append(add_dict)
    
include_dictionary_string = json.dumps(include_dictionary)
print(include_dictionary_string)