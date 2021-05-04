#!C:\users\user\desktop\python-server\server_code\eb-virt\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'Cython==0.28.4','console_scripts','cygdb'
__requires__ = 'Cython==0.28.4'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('Cython==0.28.4', 'console_scripts', 'cygdb')()
    )
