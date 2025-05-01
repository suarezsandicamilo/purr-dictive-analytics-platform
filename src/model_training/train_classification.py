#

import os
import pandas as pd
import torch

from sklearn.model_selection import train_test_split
from torch import nn
from typing import Tuple

TEST_SIZE = 0.2
RANDOM_STATE = 42

def load_and_prepare_data(
  csv_path: str,
  feature_cols: list[str],
  label_col: str,
) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
  """Loads data, splits it, and converts to PyTorch tensors."""

  df = pd.read_csv(csv_path)

  features = df[feature_cols].values
  labels = df[label_col].values

  X_train, X_test, y_train, y_test = train_test_split(
    features, labels, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=labels
  )

  # Convert to tensors
  X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
  y_train_tensor = torch.tensor(y_train, dtype=torch.long)
  X_test_tensor = torch.tensor(X_test, dtype=torch.float32)
  y_test_tensor = torch.tensor(y_test, dtype=torch.long)

  return X_train_tensor, X_test_tensor, y_train_tensor, y_test_tensor

def build_classifier(input_features: int, hidden_units: int, output_classes: int) -> nn.Sequential:
  """Builds the neural network model."""

  model = nn.Sequential(
    nn.Linear(input_features, hidden_units),
    nn.ReLU(),
    nn.Linear(hidden_units, output_classes),
  )

  return model

LEARNING_RATE = 0.001
EPOCHS = 10000

def train_model(
  model: nn.Module,
  X_train: torch.Tensor,
  y_train: torch.Tensor,
  loss_fn: nn.Module,
  print_interval: int = 1000
):
  """Trains the PyTorch model."""

  optimizer = torch.optim.Adam(model.parameters(), lr=LEARNING_RATE)

  print("Starting training...")

  for epoch in range(EPOCHS):
    model.train()

    # Forward pass
    outputs = model(X_train)
    loss = loss_fn(outputs, y_train)

    # Backward pass and optimize
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    # Print loss periodically
    if (epoch + 1) % print_interval == 0:
      print(f'Epoch ({epoch + 1} / {EPOCHS}), Loss: {loss.item():.3f}')

  print("Training finished.")

if __name__ == "__main__":
  # Load and prepare data
  DATA_PATH = 'data/processed/pokemon.csv'
  FEATURES_COLS = ['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']
  LABEL_COL = 'is_legendary'

  X_train, X_test, y_train, y_test = load_and_prepare_data(
    DATA_PATH, FEATURES_COLS, LABEL_COL
  )

  print(f"Train shape: {X_train.shape}, Test shape: {X_test.shape}")

  # Build the model
  INPUT_FEATURES = len(FEATURES_COLS)
  HIDDEN_UNITS = 16
  OUTPUT_CLASSES = 2

  model_legend = build_classifier(INPUT_FEATURES, HIDDEN_UNITS, OUTPUT_CLASSES)

  print(f"Model legend: {model_legend}")

  # Define loss function
  loss_fn = nn.CrossEntropyLoss()

  # Train the model
  train_model(model_legend, X_train, y_train, loss_fn)

  # Save the trained model
  MODEL_SAVE_DIR = "models/training"
  MODEL_SAVE_PATH = os.path.join(MODEL_SAVE_DIR, 'legendary_classifier.pth')

  os.makedirs(MODEL_SAVE_DIR, exist_ok=True)

  try:
    torch.save(model_legend.state_dict(), MODEL_SAVE_PATH)

    print(f"Model saved to {MODEL_SAVE_PATH}")
  except Exception as e:
    print(f"An error occurred: {e}")
