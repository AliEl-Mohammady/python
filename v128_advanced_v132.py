

# v128: Advanced_Lessons => __name__ And "__main__" --
# if __name__ == "__main__":
# - __name__ => Built In Variable
# - "__main__" => Value Of The __name__ Variable
# Executions Methods
# - Directly => Execute the Python File Using the Command Line.
# - From Import => Import The Code From File To Another File
# -------------------------------------------------------------
# In Some Cases You Want To Know If You Are Using A Module Method As Import
# Or You Use The Original Python File
# -------------------------------------------------------------------------
# In Direct Mode Python Assign A Value "__main__"
# To The Built In Variable __name__ in The Background
def say():
    # if __name__=="__main__" :
        print("Ali mohamed mahmoud")


# v129 Advanced_Lessons => Timing Your Code With Timeit --
# - timeit: - Get Execution Time Of Code By Running 1M Time And Give You Minimal Time
# -         - It Used For Performance By Testing All Functionality
# - timeit(stmt, setup, timer, number)
# - timeit(pass, pass, default, 1.000.000) Default Values
# -------------------------------------------------------
# - stmt: Code You Want To Measure The Execution Time
# - setup: Setup Done Before The Code Execution (Import Module Or Anything)
# - timer: The Timer Value
# - number: How Many Execution That Will Run

# import timeit

# print(dir(timeit))
# print(timeit.timeit("'Elzero' * 10000"))
# name = "Elzero"
# # print(name * 1000)
# print(timeit.timeit("name = 'Elzero'; name * 1000"))

# # print(random.randint(0, 50))

# print(timeit.timeit(stmt="random.randint(0, 50)", setup="import random"))
# print(timeit.repeat(stmt="random.randint(0, 50)", setup="import random", repeat=4))


# v130 :-- Advanced_Lessons => Add Logging To Your Code --
# --------------------------------------------------
# - Print Out To Console Or File
# - Print Logs Of What Happens
# ------------------------------
# - DEBUG
# - INFO
# - WARNING
# - ERROR
# - CRITICAL
# ----------
# name => Logging Module Give It To The Default Logger.
# -----------------------------------------------------
# Basic Config
# - level => Level of Severity
# - filename => File Name and Extension
# - mode => Mode Of The File a => Append
# - format => Format For The Log Message
# ------------------------
# getLogger => Return a Logger With the Specified Name

# import logging
# print(dir(logging))
# logging.basicConfig(filename='write.txt',filemode='a',format="%(asctime)s | %(name)s | %(levelname)s | %(message)s ")
# logging.warning("this message warning")
# logging.debug("this message warning")
# logging.error("this message warning")

# # v131 : Advanced_Lessons => Unit Testing With Unittest --
# # Test Runner
# # - The Module That Run The Unit Testing (unittest, pytest)
# # ---------------------------------------------------------
# # Test Case
# # - Smallest Unit Of Testing
# # - It Use Asserts Methods To Check For Actions And Responses
# # Test Suite
# # - Collection Of Multiple Tests Or Test Cases
# # Test Report
# # - A Full Report Contains The Failure Or Succeed
# # -------------------------------------------------------
# # unittest
# # - Add Tests Into Classes As Methods
# # - Use a Series of Special Assertion Methods
# # https://docs.python.org/3/library/unittest.html
# import unittest
# class myunitesting(unittest.TestCase) :
#     def test_case1(self):
#         self.assertEqual(20+30,51,"wrong value")
#     def test_case2(self):
#         self.assertGreater(20+30,51,"wrong ,value must be 50")

# if __name__=="__main__" :
#     unittest.main()

# v132 : Advanced_Lessons => Generate Random Serial Numbers --

import string
import random

def make_serial(count):
  all_chars = string.ascii_letters + string.digits
  # print(all_chars)
  chars_count = len(all_chars)
  # print(chars_count)
  serial_list = []
  while count > 0:
    random_number = random.randint(0, chars_count - 1)
    random_character = all_chars[random_number]
    serial_list.append(random_character)
    count -= 1  # count = count - 1
  print("".join(serial_list))

make_serial(50)





