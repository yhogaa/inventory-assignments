from django.test import TestCase, Client

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

     # Test if 'name' exists in context
    def test_name_is_exist(self):
        response = Client().get('/main/')
        self.assertIn('name', response.context)

    # Test if 'class' exists in context
    def test_class_is_exist(self):
        response = Client().get('/main/')
        self.assertIn('class', response.context)