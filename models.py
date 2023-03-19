from marshmallow import Schema, ValidationError, fields, validates_schema, validate

VALID_CMD_COMMANDS = {'filter', 'unique', 'map', 'limit', 'sort', 'regex'}

class RequestSchema(Schema):
    cmd = fields.Str(required=True, validate=validate.OneOf(VALID_CMD_COMMANDS))
    value = fields.Str(required=True)

    @validates_schema
    def check_all_cmd_valid(self, values, *args, **kwargs):
        if values['cmd'] not in VALID_CMD_COMMANDS:
            raise ValidationError('cmd is not valid')

class BatchRequestSchema(Schema):
    queries = fields.Nested(RequestSchema, many=True)
    file_name = fields.Str(required=True)