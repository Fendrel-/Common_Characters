import sys


def display_output(fname, pass_data, fail_data):
    """Display pass/fails data consistent and nicely."""
    
    
    print('='*30)
    print(' TESTING: {}'.format(fname))
    
    # Loop over any items inside pass_data
    # to display results of tests.
    print(' {} Tests Passed'.format(len(pass_data)))
    
    print('*'*30)
    print(' {} Tests Failed'.format(len(fail_data)))
    
    # Loop over any items inside fail_data
    # to display results of tests.
    for item in fail_data:
        case, result = item
        print(' {}: FAILED'.format(case['name']))
        print('\tExpected: {}'.format(case['expects']))
        print('\tReturned: {}\n'.format(result))
    print(' --- END TEST ---')
    print('='*30)
    print('\n')


def run_tests(cases, func):
    fname = str(func.__name__)
    pass_data = []
    fail_data = []

    for case in cases:
        result = func(*case['data'])
        # Compare result value to expected value.
        if result == case['expects']:
            pass_data.append((case, result))
        else:
            fail_data.append((case, result))
    return fname, pass_data, fail_data


if __name__ == '__main__':
    try:
        from code import common_characters
    except ImportError:
        print("Check code.py, be sure your function(s) are named: common_characters")
        sys.exit()

    # test_cases (below)
    # name: A name for the Test Case.
    # data: List being passed into function for testing.
    # expects: The value that should be returned by the function.
    
    test_cases_1 = [
        {'name': 'Test 1', 'data': ('abcd', 'aabbcc'), 'expects': 3},
        {'name': 'Test 2', 'data': ('xxxxx', 'xxx'), 'expects': 3},
        {'name': 'Test 3', 'data': ('treehouse', 'treeboat'), 'expects': 5},
        {'name': 'Test 4', 'data': ('jsisawesome', 'xyzawejsxyz'), 'expects': 5}
    ]
    
    fname1, p1, f1 = run_tests(test_cases_1, common_characters)
    
    
    # Display results for [1st tests] set.
    display_output(fname1, p1, f1)

