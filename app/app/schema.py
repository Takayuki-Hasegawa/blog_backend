import graphene
from app.contents import schema


class Query(schema.PostNode.schema.Query, schema.CommentNode.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
