import subprocess
import os

# URL yang ingin dibuka
url = "https://www.facebook.com/100006432036377/posts/pfbid0FsMMV3Qno7T4fMgPxGPR5Sqzp2wCT1kAru1mVCDxMX5cUjMVLZL2uAT2XNiCVKA6l/?app=fbl"

# Perintah untuk membuka URL di browser sesuai sistem operasi
if os.name == 'nt':  # Untuk Windows
    subprocess.run(["start", url], shell=True)
elif os.name == 'posix':  # Untuk Linux atau Mac
    subprocess.run(["xdg-open", url])
else:
    print("Sistem operasi tidak didukung.")