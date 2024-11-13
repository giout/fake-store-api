from marshmallow import fields, Schema

class CreateCategorySchema(Schema):
    name = fields.String(required=True)
    image_url = fields.String(required=True)