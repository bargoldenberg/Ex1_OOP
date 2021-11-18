import unittest
from Building import *
from Call import *
import Elevator
from OfflineElevAlgo import *



class MyTestCase(unittest.TestCase):

    # Complete.
    def test_direction(self):
        ans1 = direction(Call("TestCall", 4.5, 0, 6, -1, 0))
        ans2 = direction(Call("TestCall", 32.2, 3, 4, -1, 0))
        ans3 = direction(Call("TestCall", 15, 2, -1, -1, 0))
        self.assertEqual(ans1, 1)
        self.assertEqual(ans2, 1)
        self.assertEqual(ans3, -1)
    # Complete.
    def test_max_trip(self):
        b1 = Building()
        b2 = Building()
        b3 = Building()
        b4 = Building()
        b5 = Building()
        b1.load_json("B1.json")
        b2.load_json("B2.json")
        b3.load_json("B3.json")
        b4.load_json("B4.json")
        b5.load_json("B5.json")

        ans1 = max_trip(b1,[])
        ans2 = max_trip(b2,[])
        ans3 = max_trip(b3,[])
        ans4 = max_trip(b4,[])
        ans5 = max_trip(b5,[])

        self.assertEqual(ans1, 34.0)
        self.assertEqual(ans2, 22.0)
        self.assertEqual(ans3, (110/3)+10)
        self.assertEqual(ans4, 120.0)
        self.assertEqual(ans5, 250/3)
    # Complete.
    def test_allocate_elevators(self, accspected=None):
        b4 = Building()
        b4.load_json("B4.json")

        calls = load_calls('call_List_For_test.csv')
        ans1 = allocate_elevators(b4,calls)
        accCalls =load_calls('myCsvForTest.csv')
        count = 0

        for call in ans1:
            c = accCalls[count]
            self.assertEqual(int(c.elevator),int(call.elevator))
            count += 1

if __name__ == '__main__':
    unittest.main()

