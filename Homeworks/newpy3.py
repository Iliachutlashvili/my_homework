import unittest
from employee import Polynom



class TestPolynom(unittest.TestCase):

   

    def test_email(self):


        self.assertEqual(self.employee1.email, "g.lagvilava@gmail.com")
        self.assertEqual(self.employee2.email, "e.fagava@gmail.com")








if __name__ == "__main__":
    unittest.main()