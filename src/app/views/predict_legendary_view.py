#

import os
import torch

from app.serializers import PokemonFeaturesSerializer
from django.conf import settings
from django.http import HttpRequest
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from torch import nn
from typing import Dict, List, Union

def load_model(path: str) -> nn.Module:
  model = nn.Sequential(
    nn.Linear(6, 16),
    nn.ReLU(),
    nn.Linear(16, 2),
  )

  model.load_state_dict(torch.load(path, map_location='cpu'))
  model.eval()

  return model

MODEL_PATH = os.path.join(settings.BASE_DIR, '../models/training/legendary_classifier.pth')

model = load_model(MODEL_PATH)

class PredictLegendaryView(APIView):
  def post(self, request: HttpRequest) -> Response:
    serializer = PokemonFeaturesSerializer(data=request.data)

    if not serializer.is_valid():
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    data: Dict[str, float] = serializer.validated_data
    features = torch.tensor([list(data.values())], dtype=torch.float32)

    with torch.no_grad():
      logits = model(features)
      probabilities: List[float] = torch.softmax(logits, dim=1).numpy()[0].tolist()
      prediction = bool(torch.argmax(logits, dim=1).item())

    response_data: Dict[str, Union[float, bool]] = {
      'probability': probabilities[1],
      'prediction': prediction
    }

    return Response(response_data)
