import doctest
import os

def load_tests(loader, tests, pattern):
    if os.path.exists(u'advent.save'):
        os.unlink(u'advent.save')  # to avoid an error during README.txt
    tests.addTests(doctest.DocFileSuite(
            u'../README.txt', optionflags=doctest.NORMALIZE_WHITESPACE))
    tests.addTests(doctest.DocFileSuite(u'syntax.txt'))
    tests.addTests(doctest.DocFileSuite(u'vignettes.txt'))
    tests.addTests(doctest.DocFileSuite(u'walkthrough1.txt'))
    tests.addTests(doctest.DocFileSuite(u'walkthrough2.txt'))
    return tests
