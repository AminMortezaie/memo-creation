from rest_framework import serializers
from .models import Network, Wallet


class NetworkSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Network
        fields = '__all__'


class WalletSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='creator.username')
    user_id = serializers.ReadOnlyField(source='creator.id')

    class Meta:
        model = Wallet
        fields = '__all__'



