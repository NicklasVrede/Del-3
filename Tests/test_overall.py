import unittest

from Encode import encode
from Decode import decode
from ini import set_wd
import time

class TestOverall(unittest.TestCase):

    def test_overall(self):
        set_wd()
        #test 1
        start_time = time.time()
        encode("test_filer/test1.jpg", "test_filer/test1Encoded.jpg")
        print(f"Encode time: {time.time()-start_time}")
        start_time = time.time()
        decode("test_filer/test1Encoded.jpg", "test_filer/test1Decoded.jpg")
        print(f"Decode time: {time.time()-start_time}")

        print(f"Test 1 done")

        #test 2
        start_time = time.time()
        encode("test_filer/test2.pdf", "test_filer/test2Encoded.pdf")
        print(f"Encode time: {time.time()-start_time}")
        start_time = time.time()
        decode("test_filer/test2Encoded.pdf", "test_filer/test2Decoded.pdf")
        print(f"Decode time: {time.time()-start_time}")

        print("Test 2 done")

        #test 3
        start_time = time.time()
        encode("test_filer/test3.docx", "test_filer/test3Encoded.docx")
        print(f"Encode time: {time.time()-start_time}")
        start_time = time.time()
        decode("test_filer/test3Encoded.docx", "test_filer/test3Decoded.docx")
        print(f"Decode time: {time.time()-start_time}")

        print("Test 3 done")

        #test 4
        start_time = time.time()
        encode("test_filer/test4.webm", "test_filer/test4Encoded.webm")
        print(f"Encode time: {time.time()-start_time}")
        start_time = time.time()
        decode("test_filer/test4Encoded.webm", "test_filer/test4Decoded.webm")
        print(f"Decode time: {time.time()-start_time}")

        print("Test 4 done")


if __name__ == '__main__':
    unittest.main()
    



