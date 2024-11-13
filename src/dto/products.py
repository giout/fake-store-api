from marshmallow import fields, Schema

class CreateProductSchema(Schema):
    name = fields.String(required=True)
    image_url = fields.String(required=True)
    price = fields.Float(required=True)
    category = fields.Integer(required=True)
    description = fields.String(required=True)