from marshmallow import Schema, fields
from marshmallow.validate import Range


class FibonacciInputSchema(Schema):
    target = fields.Int(required=True, validate=Range(min=1))
