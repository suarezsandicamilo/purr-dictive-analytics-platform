from django.shortcuts import render

import os
import torch

from torch import nn
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import PokemonFeaturesSerializer

model = nn.Sequential(
  nn.Linear(6, 16),
  nn.ReLU(),
  nn.Linear(16, 2),
)

MODEL_PATH = os.path.join(settings.BASE_DIR, '../models/training/legendary_classifier.pth')
model.load_state_dict(torch.load(MODEL_PATH, map_location='cpu'))
model.eval()

class PredictLegendaryView(APIView):
  def post(self, request):
    serializer = PokemonFeaturesSerializer(data=request.data)

    if not serializer.is_valid():
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    data = serializer.validated_data

    x = torch.tensor([[
      data['hp'],
      data['attack'],
      data['defense'],
      data['sp_attack'],
      data['sp_defense'],
      data['speed']
    ]], dtype=torch.float32)

    with torch.no_grad():
      logits = model(x)
      probs = torch.softmax(logits, dim=1).numpy()[0].tolist()
      predicted = bool(torch.argmax(logits, dim=1).item())
    
    return Response({
      'is_legendary_probability': probs[1],
      'predicted_is_legendary': predicted
    })
