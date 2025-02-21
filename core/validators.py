from django.core.exceptions import ValidationError


def validate_length(value,length=11):
    if len(str(value)) != length:
        raise ValidationError(f"must be {length} character!")


