# from django.test import TestCase

# # Create your tests here.
# from django.test import Client, TestCase
# from django.contrib.auth.models import User
# from tracker.models import LeadSource
# from utmtracker import utm_values_in_session
# from . import settings

# class MyTestCase(TestCase):
#     def test_lead_source_creation(self):
#         client = Client()
# # first request stashes values, but does not create a LeadSource as user is anonymous
#         client.get("/?utm_medium=medium&utm_source=source...")
#         assert utm_values_in_session
#         assert LeadSource.objects.count() == 0

#         # subsequent request, with authenticated user, extracts values and stores LeadSource
#         user = User.objects.create(username="fred")
#         client.force_login(user, backend=settings.FORCED_AUTH_BACKEND)
#         client.get("/")
#         assert not utm_values_in_session
#         assert LeadSource.objects.count() == 1