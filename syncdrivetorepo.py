import os
import subprocess

# Thư mục local chứa Git repo chuẩn xác
LOCAL_REPO_PATH = r'D:\stablediffusionHVCN'

# URL Repo GitHub chuẩn xác
REPO_URL = 'https://github.com/Hoangnguyen010/stablediffusionHVCN.git'

# Thư mục trên Drive cần đồng bộ (đã mount hoặc tải sẵn về local)
DRIVE_FOLDERS = ['jsonpresets', 'notebooks']

def git(*args):
    return subprocess.check_call(['git', '-C', LOCAL_REPO_PATH] + list(args))

# Copy từ Drive sang local
def sync_from_drive():
    for folder in DRIVE_FOLDERS:
        src_path = os.path.join('D:\\GoogleDrive', folder)
        dest_path = os.path.join(LOCAL_REPO_PATH, folder)
        subprocess.call(['robocopy', src_path, dest_path, '/E', '/MIR'])

# Đồng bộ file từ Drive vào local
sync_from_drive()

# Git commit và push lên repo GitHub
git('add', '.')
git('commit', '-m', 'Auto-sync nội dung từ Google Drive lên GitHub')
git('push', 'origin', 'main')

print(' Đã đồng bộ và push nội dung lên GitHub thành công!')
