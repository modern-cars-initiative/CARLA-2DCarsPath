"""Unit test"""
# pylint: disable=line-too-long
import unittest
from dre2 import verifyfiles

class TestDic(unittest.TestCase):
    """Test"""

    def setUp(self) -> None:
        self.data1input, self.data2input = verifyfiles(['filestotest/DadosCarro86_2022-07-15_09:41:32.xlsx', 'filestotest/DadosCarro87_2022-07-15_09:41:32.xlsx'])

    def testdic1(self):
        """Test"""
        if len(self.data1input) == 0:
            resultdic = False
        else:
            resultdic = True
        self.assertEqual(resultdic, True)

    def testdic2(self):
        """Test"""
        if len(self.data2input) == 0:
            resultdic = False
        else:
            resultdic = True
        self.assertEqual(resultdic, True)

    def testlendic(self):
        """Test"""
        if len(self.data1input) and len(self.data2input) == 8:
            resultdic = True
        else:
            resultdic = False
        self.assertEqual(resultdic, True)

    def testsamelendic(self):
        """Test"""
        if len(self.data1input) != len(self.data2input):
            resultdic = False
        else:
            resultdic = True
        self.assertEqual(resultdic, True)
