from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from builder import convert_query
from models import BatchRequestSchema

main_bp = Blueprint('main', __name__)


@main_bp.route('/perform_query', methods=['POST'])
def perform_query():
    data = request.json
    try:
        validated_data = BatchRequestSchema().load(data)
    except ValidationError as e:
        return jsonify(e.messages), 400
    result = None

    for i in validated_data['queries']:
        result = convert_query(
            cmd=i['cmd'],
            value=i['value'],
            file=validated_data['file_name'],
            data=result,
        )

    return jsonify(result)


