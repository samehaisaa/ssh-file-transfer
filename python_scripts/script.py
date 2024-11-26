import paramiko
import os

def connect_ssh(host, port, username, key_path):
    transport = paramiko.Transport((host, port))
    transport.connect(username=username, key_filename=key_path)
    return transport

def upload_file_via_sftp(transport, local_file, remote_file):
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(local_file, remote_file)
    sftp.close()

def run_remote_command(transport, command):
    channel = transport.open_session()
    channel.exec_command(command)
    output = channel.recv(1024).decode()
    return output

def main():
    host = 'localhost'
    port = 22
    username = 'testuser'
    key_path = '/path/to/your/private_key'
    
    local_file = 'test_file.txt'
    remote_file = '/home/testuser/test_file_remote.txt'
    command = 'ls /home/testuser'

    transport = connect_ssh(host, port, username, key_path)
    upload_file_via_sftp(transport, local_file, remote_file)
    output = run_remote_command(transport, command)
    print(output)
    transport.close()

if __name__ == "__main__":
    main()
