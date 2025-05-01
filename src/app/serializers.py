#

from rest_framework import serializers

class PokemonFeaturesSerializer(serializers.Serializer):
  hp = serializers.FloatField()
  attack = serializers.FloatField()
  defense = serializers.FloatField()
  sp_attack = serializers.FloatField()
  sp_defense = serializers.FloatField()
  speed = serializers.FloatField()
