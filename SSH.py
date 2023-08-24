import time
import paramiko
import re

host = '192.168.1.2'
user = 'admin'
secret = 'rootpasswd'
port = '22'
maxbytes = 60000
max_buffer = 0
pause = 1
long_pause = 8
ntry = 0
nrep = 0
i = 0
tau = 0

class Abonent:
      no = '-'
      number = '-'
      iphost = '192.168.1.2'
      sipport = 'неизвестен'
      reg = '-'
      call = '0'

      def display(self):
          print(f"\n {self.no} {self.number} {self.iphost} {self.sipport} {self.reg} {self.call}")

tau72 = [n for n in range(72)]
for i in range(0,71):
    tau72[i] = Abonent()
    tau72[i].number = ''

tau72[17].number = ("nAn","nAn","ip","port","0")


tom = Abonent()


print("\O()O/ дратути \O()O/")

ntry = int(input('\nВведите число повторений опроса ТАУ '))
nrep = int(input('\nВведите интервал опроса ТАУ (сек) '))
tau = int(input('\nВведите количество портов ТАУ '))
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=host, username=user, password=secret, look_for_keys=False, allow_agent=False)
time.sleep(long_pause)
def clear_buffer(connection):
    if connection.recv_ready():
        return connection.recv(max_buffer)

def connect(tau,ssh):
    with ssh.invoke_shell() as ssh:
        for i in range(1, tau + 1):
            ssh.send('show voiceport statistic' + ' ' + str(i) + '\n')
            while True:
                time.sleep(pause)
                call = ssh.recv(3000).decode('utf-8')
                result_number = re.findall(r"pbx last number    (\d{0,999999})", call)
                time.sleep(0.5)
                result_call = re.findall(r"pbx call count     (\d{0,999999})", call)
                time.sleep(0.5)
                result_no = "Порт: " + str(i)
                tom.number = '[' + 'Последний вызов был на номер: ' + str(result_number) + ']'
                tom.no = '[' + str(result_no) + ']'
                tom.call = '[' + 'Количество вызовов с порта: ' + str(result_call) + ']'
                tau72[i].number = tom.number
                tau72[i].no = tom.no
                tau72[i].call = tom.call
                print(tau72[i].display())
                call = clear_buffer(ssh)
                if not call:
                    break
    ssh.close()

if __name__ == '__main__':
    t_ntry = ntry
    while t_ntry != 0:
        result = connect(tau, ssh)
        t_ntry = t_ntry-1
        print('До следующего опроса ', nrep, 'сек ')
        time.sleep(nrep)
