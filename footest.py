import unittest


class FooTest(unittest.TestCase):
    # Make sure the unittest system works properly
    def test_unittest_works_properly(self):
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()