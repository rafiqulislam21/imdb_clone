from rest_framework import serializers
from watchlist_app.models import Movie

# model based serializers----------------
class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = "__all__"
        # fields = ['id', 'name', 'description', 'active']
        # exclude = ['active']
        
    #object level valication
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Title and description should  not be same")
        return data
    
    # field level validation
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short")
        return value



# class based serializers-------------------
#custom validation
# def validate_custom_name(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short")
#     return value
    
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[validate_custom_name])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     #object level valication
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Title and description should  not be same")
#         return data
    
    
    #field level validation
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short")
    #     return value