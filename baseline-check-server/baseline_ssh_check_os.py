import paramiko



from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/GetOsBase')
def get_os_base():
    # 创建一个ssh的客户端，用来连接服务器
    ssh = paramiko.SSHClient()
    # 创建一个ssh的白名单
    know_host = paramiko.AutoAddPolicy()
    # 加载创建的白名单
    ssh.set_missing_host_key_policy(know_host)
    hostname1 = request.args.get('hostname')

    port1 = request.args.get('port')

    username1 = request.args.get('username')

    password1 = request.args.get('password')


    ssh.connect(
        hostname=hostname1,
        port=port1,
        username=username1,
        password=password1
    )

    # 执行命令
    # stdin, stdout, stderr = ssh.exec_command("lsb_release -a")
    # stdin, stdout, stderr = ssh.exec_command("cat /proc/cpuinfo |grep 'model name'")
    # stdin, stdout, stderr = ssh.exec_command("hostname")
    # stdin, stdout, stderr = ssh.exec_command("uname -a")
    # stdin, stdout, stderr = ssh.exec_command("ls -l")
    # stdin  标准格式的输入，是一个写权限的文件对象
    # stdout 标准格式的输出，是一个读权限的文件对象
    # stderr 标准格式的错误，是一个写权限的文件对象
    # str =stdout.read().decode('utf-8')
    # print(stdout.read().decode('utf-8'))
    # print(stdout.read().decode('utf-8'))
    # strs = stdout.read().replace('\r','')
    # print(strs)
    stdin, stdout, stderr = ssh.exec_command("cat /proc/cpuinfo |grep 'model name'")
    cpu = stdout.read().decode('utf-8')
    stdin, stdout, stderr = ssh.exec_command("hostname")
    hostname =stdout.read().decode('utf-8')
    stdin, stdout, stderr = ssh.exec_command("uname -a")
    uname= stdout.read().decode('utf-8')
    stdin, stdout, stderr = ssh.exec_command("cat /proc/meminfo | grep MemTotal")
    meminfo = stdout.read().decode('utf-8')
    stdin, stdout, stderr = ssh.exec_command("hostname -I")
    ipaddr = stdout.read().decode('utf-8')
    stdin, stdout, stderr = ssh.exec_command("lsb_release -a")
    ostype = stdout.read().decode('utf-8')
    stdin, stdout, stderr = ssh.exec_command("cat /proc/net/arp")
    macip = stdout.read().decode('utf-8')

    data = {"cpu": cpu,"hostname":hostname,"uname":uname,"meminfo":meminfo,"ipaddr":ipaddr,"ostype":ostype,"macip":macip}
    try:
        return jsonify(data)
    finally:
        ssh.close()





if __name__ == '__main__':
    app.run()