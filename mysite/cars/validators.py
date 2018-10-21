import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


def validate_number_car(value):
    result = re.search('^[A-Z]\d\d\d[A-Z][A-Z](\d\d|\d\d\d)', value)

    if not result:
        raise ValidationError(_(
            "Номер автомобиля должен состоять из английских букв и быть в формате A343BC161"
        ))
