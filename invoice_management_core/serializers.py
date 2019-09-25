from rest_framework import serializers
from .models import User
import base64

# Create your serializers here.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    def to_internal_value(self, data):
        modifiedData = super().to_internal_value(data)
        encodedPwdBytes = base64.b64encode(modifiedData['password'].encode('utf-8'))
        modifiedData['password'] = str(encodedPwdBytes, 'utf-8')
        return modifiedData