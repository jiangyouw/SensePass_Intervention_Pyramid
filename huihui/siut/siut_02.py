from common.generate_report import *
from case.test_case_01 import Test_case

if __name__ == '__main__':
    case = [
        Test_case
    ]
    add_test_case(case)
    makedirs_folder()
    report = generate_report()
    send_email(report)
