#

import kagglehub
import pandas as pd

from pathlib import Path

OUTPUT_CSV = Path("data/raw/pokemon.csv")

def download_pokemon_data(output_path: Path) -> None:
  """Downloads the Pokemon dataset from Kaggle and saves it."""

  output_path.parent.mkdir(parents=True, exist_ok=True)

  print(f"Downloading data...")

  try:
    # dataset_download returns the path to the downloaded directory/archive
    download_dir = kagglehub.dataset_download("rounakbanik/pokemon")

    # Construct the expected path to the CSV within the downloaded structure
    source_csv_path = Path(download_dir) / "pokemon.csv"

    if not source_csv_path.exists():
      raise FileNotFoundError(f"pokemon.csv not found in {download_dir}")

    print(f"Reading data from: {source_csv_path}")

    df = pd.read_csv(source_csv_path)
    df.to_csv(output_path, index=False)

    print(f"Saved data to: {output_path}")
  except Exception as e:
    print(f"An error occurred: {e}")

if __name__ == "__main__":
  download_pokemon_data(OUTPUT_CSV)
