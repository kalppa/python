#coding:utf-8
import paramiko

transport = paramiko.Transport(('192.168.1.203', 22))
transport.connect(username='chris.wang', password='Nihaoya1!!')

ssh = paramiko.SSHClient()
ssh._transport = transport

stdin, stdout, stderr = ssh.exec_command('pwd')
#print (str(stdout.read(),encoding='utf-8'))
print (str(stdout.read()))

transport.close()