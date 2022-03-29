#created 2018.12.10

#coding:utf-8

import paramiko

#创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='192.168.1.203', port=22, username='chris.wang', password='Nihaoya1!!')

# 执行命令
stdin, stdout, stderr = ssh.exec_command('du -m /')
# 获取命令结果
result = stdout.read()
#print (str(result,encoding='utf-8'))
print (str(result))
# 关闭连接
ssh.close()