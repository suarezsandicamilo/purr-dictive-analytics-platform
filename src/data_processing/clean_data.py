#

import pandas as pd

from pathlib import Path

RAW_DATA_PATH = Path("data/raw/pokemon.csv")
PROCESSED_DATA_PATH = Path("data/processed/pokemon.csv")

def clean_pokemon_data(input_path: Path, output_path: Path) -> None:
  """Cleans the raw Pokemon data and saves the processed version."""

  print(f"Reading raw data from: {input_path}")

  df = pd.read_csv(input_path)

  # Drop unnecessary columns
  df = df.drop(columns=["abilities"], errors='ignore')

  # Correct typo
  df = df.rename(columns={"classfication": "classification"}) 

  # Assign missing numerical values with median
  df["height_m"] = df["height_m"].fillna(df["height_m"].median())
  df["weight_kg"] = df["weight_kg"].fillna(df["weight_kg"].median())
  # Assuming 50% if unknown
  df["percentage_male"] = df["percentage_male"].fillna(50.0) 

  # Assign missing categorical values
  df["type2"] = df["type2"].fillna("None")

  # Convert to numeric, coercing errors to NaN
  df["capture_rate"] = pd.to_numeric(df["capture_rate"], errors="coerce")
  # Assign general NaNs with median
  df["capture_rate"] = df["capture_rate"].fillna(df["capture_rate"].median())

  # Ensure output directory exists
  output_path.parent.mkdir(parents=True, exist_ok=True)

  # Save cleaned data
  df.to_csv(output_path, index=False)

  print(f"Saved cleaned data to: {output_path}")

if __name__ == "__main__":
  clean_pokemon_data(RAW_DATA_PATH, PROCESSED_DATA_PATH)
