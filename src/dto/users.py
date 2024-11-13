from marshmallow import fields, Schema

class CreateUserSchema(Schema):
    name = fields.String(required=True)
    image_url = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)