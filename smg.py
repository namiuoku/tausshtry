import time
import paramiko
import re
import telnetlib
import pprint

host = '192.168.1.17'
user = 'admin'
secret = 'rootpasswd'
port = '22'
maxbytes = 60000
max_buffer = 0
pause = 2
long_pause = 8

print("\O()O/ дратути \O()O/")

def to_bytes(line):
    return f"{line}\n".encode('utf-8')


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=host, username=user, password=secret)
time.sleep(long_pause)

def clear_buffer(connection):
    if connection.recv_ready():
        return connection.recv(max_buffer)


with ssh.invoke_shell() as ssh:
    time.sleep(2)
    ssh.send('trace\n')
    time.sleep(2)
    with telnetlib.Telnet() as tn:
        tn = telnetlib.Telnet()
        tn.write(b'sipreg user\n')
        time.sleep(2)
        tn.read_until(b'>')
        tn.close()
ssh.close()