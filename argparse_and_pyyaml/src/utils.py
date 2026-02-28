import yaml
import pandas as pd
from pathlib import Path

def load_yaml(yaml_file: Path) -> dict:
    try:
        with open(yaml_file, "r") as file:
            config = yaml.safe_load(file)
        return config
    except FileNotFoundError:
        raise FileNotFoundError(f"No {yaml_file} found.")
    
def get_violent_crimes_df(crimes: pd.DataFrame,
                          columns_mapping: dict,
                          violent_crimes: list) -> pd.DataFrame:
    '''
    crimes: Table of Chicago crimes.
    columns_mapping: {k, v} where k and v are the old and new column names, respectively.
    violent_crimes: List of violent crimes in `Primary Type` column.
    '''
    df_out = crimes[columns_mapping.keys()]
    df_out.query("`Primary Type` in @violent_crimes", inplace = True)
    df_out.reset_index(drop = True, inplace = True)
    df_out.rename(columns = columns_mapping, inplace = True)
    
    return df_out
