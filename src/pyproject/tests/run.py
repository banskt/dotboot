
from pyproject.utils.unittest_tester import UnittestTester

def run_unittests(test_classes = None):
    if test_classes is None:
        test_classes = []
    #
    tester = UnittestTester(test_classes)
    tester.execute()
    del tester
    # =========================
    # if you want report for each class separately,
    # =========================
    #for mtest in test_classes:
    #    tester = UnittestTester(mtest)
    #    del tester
    return
