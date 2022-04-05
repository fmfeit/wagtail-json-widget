import json
from builtins import super

from django import forms
from django.conf import settings

from wagtail.core.telepath import register
from wagtail.core.widget_adapters import WidgetAdapter


class JsonWidgetAdapter(WidgetAdapter):
    js_constructor = 'wagtail_json_widget.json_widget'

    def js_args(self, widget):
        return [
            widget.render('__NAME__', None, attrs={'id': '__ID__'}),
            widget.id_for_label('__ID__'),
            # widget.extra_options, 
        ]
    class Media:
        js = ['wagtail_json_widget/js/json_widget.js']

class JsonEditorWidget(forms.Widget):
    class Media:
        js = (
            getattr(settings, "JSON_EDITOR_JS", 'dist/jsoneditor.min.js'),
        )
        css = {
            'all': (
                getattr(settings, "JSON_EDITOR_CSS", 'dist/jsoneditor.min.css'),
            )
        }

    template_name = 'wagtail_json_widget.html'

    def __init__(self, attrs=None, mode='code', options=None, width=None, height=None):
        default_options = {
            'modes': ['text', 'code', 'tree', 'form', 'view'],
            'mode': mode,
            'search': True,
        }
        if options:
            default_options.update(options)

        self.options = default_options

        super(JsonEditorWidget, self).__init__(attrs=attrs)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['options'] = json.dumps(self.options)
        return context

register(JsonWidgetAdapter(), JsonEditorWidget)
