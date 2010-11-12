from montserrat.tests import *

class TestScholarController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='scholar', action='index'))
        # Test response...
