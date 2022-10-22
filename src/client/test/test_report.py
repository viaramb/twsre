import platform
from unittest import TestCase
from client.api.report import Report


class TestReport(TestCase):
    def setUp(self) -> None:
        if platform.system() == 'Windows':
            self.output = 'data/output_test.json'
        else:
            self.output = '/app/src/client/test/data/output_test.json'
        self.r = Report(self.output)

    def test_aggregate_df(self):
        expected = """  application version  success_rate
0      Cache1   0.2.3     79.925810
1      Cache1   1.2.2     79.925810
2   Database0   0.1.0     79.925804
3   Database1   0.2.2     79.925824
4     Webapp0   1.0.2     79.925806"""
        self.r.aggregate_df()
        self.assertEqual(self.r.__repr__(), expected)
