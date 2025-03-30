import os
import re
import shutil

# Cấu hình tên cũ và tên mới
OLD_NAME = "stable_diffusion_HVCN"
NEW_NAME = "stablediffusionHVCN"

# Các thư mục/file cần rename trong local
TARGETS = [
    "stable_diffusion_HVCN",
    "stable_diffusion_HVCN/DATA_GITHUB",
    "stable_diffusion_HVCN/HVCN_LoRA_Universe",
    "stable_diffusion_HVCN/sync_drive_to_repo.py"
]

# Đổi tên folder và file
for path in TARGETS:
    if os.path.exists(path):
        new_path = path.replace(OLD_NAME, NEW_NAME)
        print(f"Đổi: {path} -> {new_path}")
        os.rename(path, new_path)

# Duyệt thư mục và đổi tên trong nội dung file
def replace_content_recursive(folder, old_text, new_text):
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith((".py", ".json", ".md", ".ipynb")):
                filepath = os.path.join(root, file)
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                updated = content.replace(old_text, new_text)
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(updated)
                print(f"✅ Đã sửa nội dung: {filepath}")

# Sửa nội dung trong toàn bộ project
replace_content_recursive(NEW_NAME, OLD_NAME, NEW_NAME)

# Cập nhật remote git (nếu cần)
repo_path = os.path.join(NEW_NAME, "HVCN_LoRA_Universe")
if os.path.exists(repo_path):
    os.chdir(repo_path)
    os.system("git remote set-url origin https://github.com/Hoangnguyen010/stablediffusionHVCN.git")
else:
    print("⚠️ Không tìm thấy thư mục Git repo để cập nhật remote.")

print("\n🎯 Hoàn tất rename toàn bộ hệ thống và đồng bộ nội dung!")
