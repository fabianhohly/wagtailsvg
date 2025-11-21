from wagtail.admin.panels import FieldPanel

from wagtailsvg.widgets import AdminSvgChooser


class SvgChooserPanel(FieldPanel):
    """
    Correct Panel for Wagtail 7.0+.
    We leverage the 'base_form_class_attrs' property of FieldPanel
    to pass the widget override directly to the form class.
    """

    @property
    def base_form_class_attrs(self):
        return {"widgets": {self.field_name: AdminSvgChooser}}

    pass
