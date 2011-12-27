class UnitTestA(unittest.TestCase):
    def setUp(self):
        popup("setting things up")
    def test1(self):
        popup("running test1")
    def test2(self):
        popup("running test2")
    def test3(self):
        popup("running test3")
    def tearDown(self):
        popup("tearing things down")
