#

import os
import pandas as pd

def clean_pokemon_data(input_csv, output_csv):
  df = pd.read_csv(input_csv)

  df = df.drop(columns=["abilities"])
  df = df.rename(columns={"classfication": "classification"})

  df["height_m"] = df["height_m"].fillna(0.0)
  df["weight_kg"] = df["weight_kg"].fillna(0.0)
  df["percentage_male"] = df["percentage_male"].fillna(50.0)
  df["type2"] = df["type2"].fillna("None")
  df["capture_rate"] = pd.to_numeric(df["capture_rate"], errors="coerce")

  df["capture_rate"] = df["capture_rate"].where(df["name"] != "Minior", 30.0)

  os.makedirs(os.path.dirname(output_csv), exist_ok=True)
  df.to_csv(output_csv, index=False)

if __name__ == "__main__":
  clean_pokemon_data("data/raw/pokemon.csv", "data/processed/pokemon.csv")
