import unittest
from Building import *
from Call import *
import Elevator
from OfflineElevAlgo import *



class MyTestCase(unittest.TestCase):
    call1 = Call("TestCall",4.5,0,6,-1,0)
    call2 = Call("TestCall",32.2,3,4,-1,0)
    call3 = Call("TestCall",15,2,-1,-1,0)



    # Need To Finish.
    def test_correct_state(self):
        # ans1 = direction(Call("TestCall", 4.5, 0, 6, -1, 0))
        # ans2 = direction(Call("TestCall",32.2,3,4,-1,0))
        # ans3 = direction(Call("TestCall",15,2,-1,-1,0))
        # self.assertEqual(True, False)
        # self.assertEqual(True, False)
        self.assertEqual(True, False)
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


    def test_change_direction(self):
        # b4 = Building()
        # b5 = Building()
        #
        # b4.load_json("B4.json")
        # b5.load_json("B5.json")
        #
        # call1 = load_calls("Calls_a.csv")
        # call2 = load_calls("Calls_b.csv")
        #
        # test1 = change_direction(b4,call1,[],)


        self.assertEqual(True, False)  # add assertion here

    def test_allocate_elevators(self):
        b4 = Building()
        b5 = Building()

        b4.load_json("B4.json")
        b5.load_json("B5.json")

        call1 = load_calls("myCsvForTest.csv")

        ans1 = allocate_elevators(b4, call1)

        # print(ans1.pop(0).)
        print("Test")

        # self.assertEqual(ans1.pop(0)., 3)
        self.assertEqual(True, False)  # add assertion here

    def test_allocate_to_bunch(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
