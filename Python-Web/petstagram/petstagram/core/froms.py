class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_fields()

    def _init_bootstrap_fields(self):
        for field in self.fields.values():
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''

            field.widget.attrs['class'] += 'form-control'
