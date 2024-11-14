from marshmallow import fields, Schema

class CreateCategorySchema(Schema):
    name = fields.String(required=True)
    image_url = fields.String(required=True)
    price = fields.Float(required=True)
    category_id = fields.Integer(required=True)
    description = fields.String(required=True)