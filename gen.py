import os
import sys
import shutil

if "remove" in sys.argv:
    for item in os.listdir():
        if item.startswith("Snapchat"):
            shutil.rmtree(item)
else:

    platforms = ["windows", "mac", "linux", "osx"]
    arches = ["arm64", "x64"]
    for platform in platforms:
        for arch in arches:
            os.system(
                f"nativefier --name Snapchat -p {platform} -a {arch} https://web.snapchat.com/"
            )
