from marshmallow import Schema, fields


class AcckermanInputSchema(Schema):
    start = fields.Int(required=True)
    end = fields.Int(required=True)
