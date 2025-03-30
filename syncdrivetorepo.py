import os
import subprocess

LOCAL_REPO_PATH = r'D:\stablediffusionHVCN'
DRIVE_ROOT_PATH = r'D:\GoogleDrive\stablediffusionHVCN'

DRIVE_FOLDERS = ['jsonpresets', 'notebooks']

def git(*args):
    subprocess.check_call(['git', '-C', LOCAL_REPO_PATH] + list(args))

def sync_from_drive():
    for folder in DRIVE_FOLDERS:
        src_path = os.path.join(DRIVE_ROOT_PATH, folder)
        dest_path = os.path.join(LOCAL_REPO_PATH, folder)
        
        if not os.path.exists(dest_path):
            os.makedirs(dest_path)

        subprocess.call(['robocopy', src_path, dest_path, '/E', '/MIR'])

sync_from_drive()

git('add', '.')
git('commit', '-m', 'Auto-sync từ Drive')
git('push', 'origin', 'main')

print('🚀 Đồng bộ thành công!')