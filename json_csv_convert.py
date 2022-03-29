import json
import csv
import pandas


def j2c(fileinput: str, newnameinput: str) -> object:
    json_df = pandas.read_json(f"{fileinput}")
    json_df.to_csv(f"{newnameinput}")
    return json_df


def j2c_nested(fileinput: str, newnameinput: str, key_to_extract: str) -> object:
    with open(fileinput, encoding="utf-8") as file_:
        json_object = json.load(file_)
        extracted_results_of_key = json_object[key_to_extract]
    with open(newnameinput, "w", encoding="utf-8",newline="\n") as out:
        keys_header = extracted_results_of_key[0].keys()
        dict_writer = csv.DictWriter(out, keys_header)
        dict_writer.writeheader()
        dict_writer.writerows(extracted_results_of_key)
    return dict_writer


def c2j(
    fileinput: str,
    newnameinput: str,
    fieldname1: str = "hs_code",
    fieldname2: str = "description",
    fieldname3: str = "group",
) -> object:
    with open(fileinput, "r", encoding="utf-8") as file_:
        fieldnames = (fieldname1, fieldname2, fieldname3)
        csvreader = csv.DictReader(file_, fieldnames)
        with open(newnameinput, "w", encoding="utf-8") as jsonfile:
            jsonfile.write("[")
            for row in csvreader:
                json.dump(row, jsonfile)
                jsonfile.write(",\n")
                jsonfile.write("]")
    return jsonfile


def main():
    input_file_name = input("enter input file: ")
    new_name = input("enter output file name: ")
    option_ = input(
        "do you want to:\n1) convert json to csv\n2) convert a nested json to csv\n3) convert a csv to json\nEnter option: "
    )
    if option_ == "1":
        j2c(input_file_name, new_name)
    elif option_ == "2":
        key_name = input("Enter key name: ")
        j2c_nested(input_file_name, new_name, key_name)
    else:
        c2j(input_file_name, new_name)


if __name__ == "__main__":
    main()
