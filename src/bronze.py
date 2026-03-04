#According to the PRD, the Bronze layer:

#1. Reads raw files from /data
#2. Stores exact copies in /bronze
#3. No transformations applied 
#So this layer simply copies raw data into the pipeline.

import pandas as pd
from pathlib import Path

def run_bronze():
    data_path = Path("data")
    bronze_path = Path("bronze")
    files = ["ehr.csv", "vitals.csv", "labs.csv"]
    for file in files:
        df = pd.read_csv(data_path / file)
        df.to_csv(bronze_path / file, index=False)
    print("[INFO] Bronze layer completed")