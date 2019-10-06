import subprocess
import sys

def anotherProcess(cmd):
    print('Running custom command...')
    cmd = subprocess.run(cmd, shell=True, check=True)
    print(cmd)

class Auth:
    def __init__(self, user, pw, server, port):
        self.user = user
        self.pw = pw
        self.server = server
        self.port = port

argLen = len(sys.argv)
defaulProcess = 'ssh -L 127.0.0.1:1206:127.0.0.1:1206'

if argLen != 5:
    if argLen == 2 and 'help' in sys.argv[1]:
        print('-user, -password, -server, -port')
        sys.exit()
    if argLen == 2 and 'command' in sys.argv[1]:
        anotherProcess(sys.argv[1])  
        sys.exit()      
    print('You need at least 4 arguments to run this script! Use -help!')
    sys.exit()    

exec = Auth(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
command = f'ssh -L 127.0.0.1:1206:127.0.0.1:1206 {exec.user}:{exec.pw}@{exec.server} -p {exec.port}'

std = subprocess.run(command, shell=True, check=True)
print(std)
    
