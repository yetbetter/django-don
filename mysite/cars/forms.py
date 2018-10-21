from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm

from cars.models import Car


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ('number', 'mark', 'model')
        error_messages = {
            'number': {
                'required': _('Поле обязательно для заполнения'),
                'max_length': _('Превышен лимит символов')
            },

            'mark': {
                'required': _('Поле обязательно для заполнения'),
                'max_length': _('Превышен лимит символов')
            },

            'model': {
                'required': _('Поле обязательно для заполнения'),
                'max_length': _('Превышен лимит символов')
            },
        }
