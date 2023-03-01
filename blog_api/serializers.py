from rest_framework import serializers

from blog.models import Post


"""
	what serializer actually do?
	converting objects into different data types to frontend understand
"""
# get users here 

class PostSerializer(serializers.ModelSerializer):
	url = serializers.HyperlinkedIdentityField(
		view_name='blog_api:detailsdelete',
		lookup_field='pk'
		)

	class Meta:
		model = Post 
		fields = ('url','id', 'category', 'title', 'author', 'excerpt', 'content', 'status')