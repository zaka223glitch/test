import unittest
from app import add
class TestApp(unittest.Testcase):
  def test_add(self):
    self.assertEqual(add(2,3),5)
    self.assertEqual(add(-1,1),0)

if _name_ == "_main_":
unittest.main()
