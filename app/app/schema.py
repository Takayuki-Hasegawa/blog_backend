import graphene
import contents.schema


class Query(contents.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
