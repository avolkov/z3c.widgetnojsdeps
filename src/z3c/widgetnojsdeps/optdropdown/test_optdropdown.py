import unittest2 as unittest
import zope.schema
from zope.publisher.browser import TestRequest
from z3c.form import field
from z3c.schema.optchoice import OptionalChoice
from z3c.widgetnojsdeps.optdropdown import OptionalDropdownWidgetFactory,\
    OptionalDropdownWidget

class Content(object):
    occupation = None

class TestFieldIntegration(unittest.TestCase):
    def setUp(self):
        self.request = TestRequest()
        self.content = Content()
    def test_optional_widget_factory(self):
        optchoice = OptionalChoice(
            __name__='occupation',
            title=u'Occupation',
            description=u'The Occupation',
            values=(u'Programmer', u'Designer', u'Project Manager'),
            value_type=zope.schema.TextLine())
        form.widget(optchoice='z3c.widgetnojsdeps.optdropdown.OptionalDropdownWidget')
        field_manager = field.Fields(optchoice)
        #field_manager['occupation'] = OptionalDropdownWidgetFactory
        #widgetFactory=OptionalDropdownWidgetFactory
        import pdb; pdb.set_trace()