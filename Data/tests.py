from django.test import TestCase

# Create your tests here.

from Data.models import Weibo

class WeiboTestCase(TestCase):
    def setUp(self) -> None:
        pass
    def test_weibo_loc(self):
        locs = Weibo.loc
        self.assertLogs(logger=locs)
