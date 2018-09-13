"""
For testing console programs using pytest.
"""

import subprocess
import os

expected = """
--- FROM USER ---
antranig,1\n
cwen,5\n
david.horwitz,4\n
gopal.ramasammycook,1\n
gsilver,3\n
louis,3\n
ray,1\n
rjlowe,2\n
stephen.marquard,2\n
wagnermr,1\n
zqian,4\n
--- FROM HOST ---
caret.cam.ac.uk,1\n
gmail.com,1\n
iupui.edu,8\n
media.berkeley.edu,4\n
uct.ac.za,6\n
umich.edu,7\n
--- TO USER ---
source,27\n
--- TO HOST ---
collab.sakaiproject.org,27\n
"""

def test_output():
    '''Test output.'''
    # use Popen to launch the Python script
    sp = subprocess.Popen(['python', 'fromto.py'], bufsize=1,
         universal_newlines=True,
         stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # enter the inputs
    stdout, stderr = sp.communicate('')
    # check outputs
    assert stdout.strip() == expected.strip()
    assert stderr == ''

if __name__ == '__main__':
    test_output()
