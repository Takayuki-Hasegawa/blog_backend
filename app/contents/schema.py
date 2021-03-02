from django.db import models
import graphene
from graphene_django.types import DjangoObjectType
from .models import Comment, Post
from graphene_django.filter import DjangoFilterConnectionField
from graphene import relay
from graphql_relay import from_global_id


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        filter_fields = {
            'title': ['exact', 'icontains'],
            'context': ['exact', 'icontains']
            # created_atは必要？？
        }
        interfaces = (relay.Node,)


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
        filter_fields = {
            'user_name': ['exact', 'icontains'],
            'context': ['exact', 'icontains']
        }
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    post = graphene.Field(PostType, id=graphene.Int())
    comment = graphene.Field(CommentType, id=graphene.Int())
    posts = DjangoFilterConnectionField(PostType)
    commets = DjangoFilterConnectionField(CommentType)

    def resolve_post(self, info, **kwargs):
        id = kwargs.get('id')
        return Post.objects.get(pk=id)

    def resolve_comment(self, info, **kwargs):
        id = kwargs.get('id')
        return Comment.objects.get(pk=id)

    def resolve_posts(self, info, **kwargs):
        return Post.objects.all()

    def resolve_comments(self, info, **kwargs):
        return Comment.objects.all()
