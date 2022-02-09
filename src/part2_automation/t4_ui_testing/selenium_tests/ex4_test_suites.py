import os
import unittest
from datetime import datetime

import HtmlTestRunner

from src.part2_automation.t4_ui_testing.selenium_tests import ex3_context_menu_oop, ex2_auth_oop, \
    ex5_test_multi_tabs_oop

direct = os.getcwd()


class MyTestSuite(unittest.TestCase):

    def test_suite(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(ex2_auth_oop.TestAuth),
            unittest.defaultTestLoader.loadTestsFromTestCase(ex3_context_menu_oop.TestContext),
            unittest.defaultTestLoader.loadTestsFromTestCase(ex5_test_multi_tabs_oop.TestMultiTabs)
        ])

        # outfile = open(direct + '\SmokeTest' + str(datetime.now()) + '.html', 'w')
        # pip install html-testRunner
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='Test Report',
            report_name='Smoke Tests'
        )

        runner.run(smoke_test)


if __name__ == '__main__':
    unittest.main()
