import paramiko
 
ssh = paramiko.SSHClient()#创建SSH对象
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())#允许连接不在know_hosts文件中的主机
ssh.connect(hostname='112.74.173.175', port=22, username='root', password='lywh978216-')#连接服务器
 
stdin, stdout, stderr = ssh.exec_command('whoami')#执行命令并获取命令结果
#stdin为输入的命令
#stdout为命令返回的结果
#stderr为命令错误时返回的结果
res,err = stdout.read(),stderr.read()
result = res if res else err
print(result)
import MySQLdb

# 打开数据库连接
db = MySQLdb.connect(host='112.74.173.175',  
            port=3306,  
            user='root',  
            passwd='12345678', 
            db='djangoVue',)

# 使用cursor()方法获取操作游标 
cursor = db.cursor()
aaa = cursor.execute("show tables")
print(aaa)
# 使用execute方法执行SQL语句
ssh.close()#关闭连接
