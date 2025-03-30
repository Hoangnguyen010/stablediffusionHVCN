import os
import subprocess

# Thư mục local chứa Git repo chuẩn xác
LOCAL_REPO_PATH = r'D:\stablediffusionHVCN'

# URL Repo GitHub chuẩn xác
REPO_URL = 'https://github.com/Hoangnguyen010/stablediffusionHVCN.git'

# Thư mục trên Drive cần đồng bộ
DRIVE_ROOT_PATH = r'D:\GoogleDrive\stablediffusionHVCN'
DRIVE_FOLDERS = ['jsonpresets', 'notebooks']

def git(*args):
    subprocess.check_call(['git', '-C', LOCAL_REPO_PATH] + list(args))

# Copy từ Drive sang local
def sync_from_drive():
    for folder in DRIVE_FOLDERS:
        src_path = os.path.join(DRIVE_ROOT_PATH, folder)
        dest_path = os.path.join(LOCAL_REPO_PATH, folder)

        # Tự tạo thư mục local nếu chưa có
        if not os.path.exists(dest_path):
            os.makedirs(dest_path)

        subprocess.call(['robocopy', src_path, dest_path, '/E', '/MIR'])

# Thực hiện đồng bộ
sync_from_drive()

# Git commit và push lên repo GitHub
git('add', '.')
git('commit', '-m', 'Auto-sync nội dung từ Google Drive lên GitHub')
git('push', 'origin', 'main')

print('🚀 Đã đồng bộ và push nội dung lên GitHub thành công!')
