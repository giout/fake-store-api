from marshmallow import fields, Schema

class UrlSchema(Schema):
    id = fields.Int(required=True)