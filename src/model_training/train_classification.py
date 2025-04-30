#

import torch
import os
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from torch import nn

df = pd.read_csv('data/processed/pokemon.csv')

features = df[['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']].values
labels_legendary = df['is_legendary'].values

X_train, X_test, y_train, y_test = train_test_split(
  features, labels_legendary, test_size=0.2, random_state=42
)

X_train = torch.tensor(X_train, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.long)
X_test = torch.tensor(X_test, dtype=torch.float32)
y_test = torch.tensor(y_test, dtype=torch.long)

model_legend = nn.Sequential(
  nn.Linear(6, 16),
  nn.ReLU(),
  nn.Linear(16, 2),
)

loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model_legend.parameters(), lr=0.001)

for epoch in range(10000):
  optimizer.zero_grad()
  outputs = model_legend(X_train)
  loss = loss_fn(outputs, y_train)
  loss.backward()
  optimizer.step()

os.makedirs("models/training", exist_ok=True)
torch.save(model_legend.state_dict(), 'models/training/legendary_classifier.pth')
