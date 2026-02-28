import json
import os

data_path: str = "data/"
json_path_in: str = data_path + "input.json"
json_path_out: str = data_path + "output.json"

# pratica di gestione delle eccezioni sarà quella di loggare tutto su un
# file di testo
log_dir: str = "logs/"
log_filename: str = "json-parser.log"

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

if os.path.exists(data_path):

    json_file: list = []
    try:
        with open(json_path_in) as f:
            json_file = json.load(f)

        filtered_json = [{**entry, "prezzo_scontato": round(entry["prezzo"] * 0.90, 2)} for entry in json_file if entry["disponibile"]]
        
        with open(json_path_out, "w") as write_json:
            write_json.write(json.dumps(filtered_json))

        print("JSON parsed successfully.")
    except FileNotFoundError as e:
        with open(log_dir + log_filename, "w") as write_file:
            write_file.write(f"Unable to parse: file not found.")    

        print("A catastrophy has occurred! Check your logs!!!!")

    except json.JSONDecodeError as json_e:
        with open(log_dir + log_filename, "w") as write_file:
            write_file.write(f"Unable to parse: invalid JSON.")    

        print("A catastrophy has occurred! Check your logs!!!!")

else:
    with open(log_dir + log_filename, "w") as write_file:
        write_file.write(f"Unable to parse: data directory not found.")

    print("A catastrophy has occurred! Check your logs!!!!")
