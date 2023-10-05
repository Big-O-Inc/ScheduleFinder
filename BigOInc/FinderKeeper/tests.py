from django.test import TestCase, RequestFactory
from . import views

# Create your tests here.
class TestCalls(TestCase):
    #Creating a request factory to mimic HTTP requests
    def setUp(self):
        self.factory = RequestFactory()

    #Test to see how /FinderKeeper/map handles get requests
    def test_map_get(self):
        request = self.factory.get("/FinderKeeper/map")
        response = views.get_map(request)
        self.assertEqual(response.status_code, 200)

    #Test to see how the endpoint handles post requests.
    #Since function was not designed to handle post requests, it should result in a fail.
    def test_map_post(self):
        request = self.factory.post("/FinderKeeper/map")
        response = views.get_map(request)
        self.assertEqual(response.status_code, 200)

    #Test to see how /FinderKeeper/buildings handles get requests
    def test_building_data_get(self):    
        request = self.factory.get("/FinderKeeper/buildings")
        response = views.get_map(request)
        self.assertEqual(response.status_code, 200)