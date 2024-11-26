import unittest
import paramiko
from transfer import upload_file, download_file  # Import your functions to be tested

class TestFileTransfer(unittest.TestCase):

    def setUp(self):
        self.host = "localhost"

        self.port = 22           # Default SSH port
        self.username = "user"   # Your SSH username
        self.password = "pass"   # Your SSH password
        self.local_file = "test_file.txt"  # Path to a local file to transfer
        self.remote_file = "remote_test_file.txt"  # Path to where the file will be uploaded/downloaded

    def test_upload_file(self):
        try:
            upload_file(self.local_file, self.host, self.username, self.password, self.remote_file)
            self.assertTrue(True)  # If no error is raised, test passes
        except Exception as e:
            self.fail(f"Upload failed: {e}")

    def test_download_file(self):
        # Test file download functionality
        try:
            download_file(self.remote_file, self.host, self.username, self.password, self.local_file)
            self.assertTrue(os.path.exists(self.local_file))  
        except Exception as e:
            self.fail(f"Download failed: {e}")

if __name__ == '__main__':
    unittest.main()
