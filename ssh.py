from subprocess import run
from sys import exit, argv


class Auth:
    def __init__(self, user, pw, server, port):
        self.user = user
        self.pw = pw
        self.server = server
        self.port = port


argLen = len(argv)
# isso nunca é usado, é realmente necessário?
# defaultProcess = 'ssh -L 127.0.0.1:1206:127.0.0.1:1206'


def anotherProcess(cmd):
    print('Running custom command...')
    cmd = run(cmd, shell=True, check=True)
    print(cmd)


if argLen != 5:
    if argLen == 2 and 'help' in argv[1]:
        print('-user, -password, -server, -port')
        exit()
    if argLen == 2 and 'command' in argv[1]:
        # isso nunca seria executado, pois a criação da função estava após o comando.
        anotherProcess(argv[1])
        exit()
    print('You need at least 4 arguments to run this script! Use -help!')
    exit()

exec = Auth(argv[1], argv[2], argv[3], argv[4])
command = f'ssh -L 127.0.0.1:1206:127.0.0.1:1206 {exec.user}:{exec.pw}@{exec.server} -p {exec.port}'

std = run(command, shell=True, check=True)
print(std)
