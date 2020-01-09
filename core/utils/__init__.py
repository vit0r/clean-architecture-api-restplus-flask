"""Func utils for app and namespaces
"""

from flask_restplus import fields


def get_namespace_model(schema_name, api_ns, model):
    """Create swagger data model"""
    declared_fields = model._declared_fields
    model_fields = {
        field_name: getattr(fields, type(field_type).__name__)(
            required=field_type.required, description=field_name
        )
        for field_name, field_type in declared_fields.items()
    }
    assert isinstance(schema_name, str)
    assert isinstance(model_fields, dict)
    api_model = api_ns.model(schema_name, model_fields)
    return api_model
