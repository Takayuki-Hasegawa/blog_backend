from django.db import models
import graphene
from graphene_django.types import DjangoObjectType
from .models import Comment, Post
from graphene_django.filter import DjangoFilterConnectionField
from graphene import relay
from graphql_relay import from_global_id


class PostNode(DjangoObjectType):
    class Meta:
        model = Post
        filter_fields = {
            'title': ['exact', 'icontains'],
            'context': ['exact', 'icontains']
            # created_atは必要？？
        }
        interfaces = (relay.Node,)


class CommentNode(DjangoObjectType):
    class Meta:
        model = Comment
        filter_fields = {
            'user_name': ['exact', 'icontains'],
            'context': ['exact', 'icontains']
        }
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    post = graphene.Field(PostNode, id=graphene.NonNull(graphene.ID))
    comment = graphene.Field(CommentNode, id=graphene.NonNull(graphene.ID))
    posts = DjangoFilterConnectionField(PostNode)
    commets = DjangoFilterConnectionField(CommentNode)

    def resolve_post(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Post.objects.get(id=from_global_id(id)[1])

    def resolve_post(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Comment.objects.get(id=from_global_id(id)[1])

    def resolve_posts(self, info, **kwargs):
        return Post.objects.all()

    def resolve_comments(self, info, **kwargs):
        return Comment.objects.all()
