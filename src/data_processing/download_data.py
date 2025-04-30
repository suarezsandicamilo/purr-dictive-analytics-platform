#

import kagglehub
import os
import pandas as pd

def download_pokemon_data():
  os.makedirs('data/raw', exist_ok=True)
  path = kagglehub.dataset_download("rounakbanik/pokemon")
  path = os.path.join(path, "pokemon.csv")
  df = pd.read_csv(path)
  df.to_csv('data/raw/pokemon.csv', index=False)

if __name__ == "__main__":
  download_pokemon_data()
