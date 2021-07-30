#!/usr/bin/python3

import sys
import subprocess
import requests

urls = [
'https://project1.ecen4133.org/autograder/lengthextension/api?token=f1bb7d2c97b5bfb207bc2fcaf961e76c&command=Test1&command=GradeProject&command=NoOp',
'https://project1.ecen4133.org/autograder/lengthextension/api?token=3359a213dfe8795c4ea6f4bfedabcce6&command=VeryLongCommandThatMightTakeUpMultipleBlocksAndFindSolutionsThatIncorrectlyCountBits',
'https://project1.ecen4133.org/autograder/lengthextension/api?token=22318e3f85a3d45894c9acdbcfe69ae6&command=SprinklersPowerOn',
'https://project1.ecen4133.org/autograder/lengthextension/api?token=9a5f6196a38e770d6f151814eb0eaea1&command=ClockPowerOff&command=NoOp&command=ClockPowerOn'
]
for i, url in enumerate(urls):
    modified_url = subprocess.check_output(['python3', 'len_ext_attack.py', url]) # env = new_env?
    modified_url = modified_url.strip()
    if modified_url == b'':
        print('Did not provide url for test %d' % (i))
        sys.exit(-1)
    with requests.get(modified_url) as response:
        if b"<big>Nice work autograder!</big>" in response.content:
            print('Passed test %d!' % i)
            continue
        else:
            print('Failed test %d: %s' % (i, url))
            sys.exit(-1)

print('')
print('All len_ext_attack.py tests passed')
