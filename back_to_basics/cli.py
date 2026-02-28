import pandas as pd
import argparse
from pathlib import Path

def export_to_csv(df: pd.DataFrame, 
                  output_dir: Path = Path("./output"),
                  file_name: str = "test.csv"):
    output_dir.mkdir(exist_ok = True)
    df.to_csv(output_dir.joinpath(file_name), index = False)
    
    print(f"Exported to {output_dir}/{file_name}!")

def main(args: argparse.Namespace) -> pd.DataFrame:
    '''
    Takes Chicago crimes table (args.f), then filters for args.crime_type.
    
    In the shell,
    1. Do python argparse.py --help to see the help messages.
    3. Do python argparse.py to run this code with the default values of the CLI args.
    2. Do python argparse.py -f /path/to/data --crime_type ${crime_type} to run this code with desired CLI args.
    '''
    df = pd.read_csv(args.f)
    
    print(f"Filtering for {args.crime_type}...")
    df_out = df.query(f"`Primary Type` == '{args.crime_type}'")
    df_out.reset_index(drop = True, inplace = True)
    
    print("Done.")
    return df_out

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = main.__doc__)
    parser.add_argument("-f",
                        help = "Path to Chicago crimes table (.csv).",
                        default = "./data/chicago_crimes.csv")
    
    parser.add_argument("--crime_type",
                        help = "value in Chicago crime table's Primary Type table to keep.",
                        choices = ["ASSAULT", "BATTERY", "ROBBERY"],
                        default = "ASSAULT")
    
    args = parser.parse_args()
    
    result = main(args)
    
    export_to_csv(df = result.head())
