import paramiko
import os

def ssh_connect(ssh_host, ssh_port, ssh_username, ssh_password=None, ssh_key=None):
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if ssh_password:
            ssh_client.connect(ssh_host, port=ssh_port, username=ssh_username, password=ssh_password)
        elif ssh_key:
            ssh_client.connect(ssh_host, port=ssh_port, username=ssh_username, key_filename=ssh_key)
        else:
            raise ValueError("No authentication method provided.")
        print(f"Connected to {ssh_host} successfully!")
        return ssh_client
    except paramiko.AuthenticationException:
        print("Authentication failed.")
        raise
    except Exception as e:
        print(f"Error occurred while connecting: {e}")
        raise

def upload_file(ssh_client, local_file_path, remote_file_path):
    try:
        sftp = ssh_client.open_sftp()
        sftp.put(local_file_path, remote_file_path)
        print(f"File {local_file_path} uploaded to {remote_file_path}.")
        sftp.close()
    except Exception as e:
        print(f"Error occurred during file upload: {e}")
        raise

def download_file(ssh_client, remote_file_path, local_file_path):
    try:
        sftp = ssh_client.open_sftp()
        sftp.get(remote_file_path, local_file_path)
        print(f"File {remote_file_path} downloaded to {local_file_path}.")
        sftp.close()
    except Exception as e:
        print(f"Error occurred during file download: {e}")
        raise

def close_connection(ssh_client):
    try:
        ssh_client.close()
        print("SSH connection closed.")
    except Exception as e:
        print(f"Error occurred while closing the connection: {e}")
        raise

if __name__ == "__main__":
    ssh_host = 'localhost'
    ssh_port = 22
    ssh_username = 'testuser'
    ssh_password = None
    ssh_key = '/path/to/your/private_key'

    local_file = 'test_file.txt'
    remote_file = '/home/testuser/test_file_remote.txt'

    try:
        ssh_client = ssh_connect(ssh_host, ssh_port, ssh_username, ssh_password, ssh_key)
        upload_file(ssh_client, local_file, remote_file)
        close_connection(ssh_client)
    except Exception as e:
        print(f"Error occurred during file transfer: {e}")
