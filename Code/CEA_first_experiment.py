import csv
import requests
import pandas as pd
import time

WIKIDATA_API_ENDPOINT = "https://www.wikidata.org/w/api.php"

def get_wikidata_entity(table_name, row_index, column_index):
    print(table_name)
    
    df_target = pd.read_csv(f"DataSets/Valid/tables/{table_name}.csv", header=None)    
    cell_value = df_target.iloc[row_index, column_index]
    print(cell_value)
    # No preprocessing, request the API with the same given cell input
    params = {
        "action": "wbsearchentities",
        "format": "json",
        "language": "en",
        "search": cell_value
    }

    try:
        response = requests.get(WIKIDATA_API_ENDPOINT, params=params)
        data = response.json()

        if "search" in data:
            # If the API find an associated entity for the input
            if len(data["search"]) != 0:
                return data["search"][0]["concepturi"]
        return ""
    
    except requests.exceptions.RequestException as e:
        print("An error occurred while connecting to the Wikidata API:", str(e))
    
    return None

# Add annotation to the csv files
def annotate_cells():
    df_cea_targets = pd.read_csv("DataSets/Valid/targets/cea_targets.csv", header=None)
    df_annotated = df_cea_targets.copy()

    # Create Annotation column    
    df_annotated[3] = df_annotated.apply(lambda row: get_wikidata_entity(row[0], row[1], row[2]), axis=1)
    
    # Save the annotated df
    df_annotated.to_csv('DataSets/Valid/cea annotation/output_baseline.csv', index=False)


if __name__ == "__main__":
    # Start the timer
    start_time = time.time()
    annotate_cells()

    # End the timer
    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = end_time - start_time

    # Print the elapsed time
    print(f"Elapsed time: {elapsed_time} seconds")