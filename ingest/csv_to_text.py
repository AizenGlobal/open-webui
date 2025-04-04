import pandas as pd
import argparse
import os
from formatters import get_formatter

def convert_csv_to_text(input_csv, output_txt, data_type, lang):
    formatter = get_formatter(data_type, lang)
    df = pd.read_csv(input_csv, sep=",", encoding="utf-8")

    with open(output_txt, "w", encoding="utf-8") as f:
        for _, row in df.iterrows():
            f.write(formatter.format_row(row, lang) + "\n")

    print(f"✅ [{lang.upper()}] {len(df)} rows processed from type '{data_type}' → saved to '{output_txt}'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert structured CSV data to readable text.")
    parser.add_argument("input_csv", help="Input CSV or TSV file path")
    parser.add_argument("output_txt", help="Output TXT file path")
    parser.add_argument("--type", required=True, help="Data type: loan, borrower, collateral, etc.")
    parser.add_argument("--lang", choices=["en", "ko"], default="en", help="Output language")
    args = parser.parse_args()

    if not os.path.exists(args.input_csv):
        print("❌ Input file does not exist.")
    else:
        convert_csv_to_text(args.input_csv, args.output_txt, args.type, args.lang)
