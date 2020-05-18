from marshmallow import Schema, fields
from marshmallow.validate import Range


class FactorialInputSchema(Schema):
    target = fields.Int(required=True, validate=Range(min=0))
