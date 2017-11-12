import time
import re
from os import path


class Config:
    resources_dir = "./resources/"
    resources_dir = path.abspath(resources_dir)
    output_file = path.join(resources_dir, "tmp_manifest_file.txt")
    input_file = path.join(resources_dir, "input.txt")

    renamed_gadget_name = time.strftime("%d%m%Y-%H%M%S")
    renamed_gadget_lib_name = "lib" + renamed_gadget_name + ".so"
    renamed_gadget_path = path.join(resources_dir, renamed_gadget_lib_name)

    # ************** INSERT APK NAME ONCE FUNCTIONALITY DONE
    app_name = "test_apk"
    lib_path = "./resources/XXXX/lib/"
    lib_path = path.abspath(lib_path)
    inject_lib_path = lib_path.replace("XXXX", app_name)
    inject_lib_path = path.join(inject_lib_path, renamed_gadget_lib_name)

    injection_string = ("\n\
const-string v0, \"XXXX\"\n\
invoke-static {v0}, Ljava/lang/System;->loadLibrary(Ljava/lang/String;)V\n\n")

    injection_string = injection_string.replace("XXXX", renamed_gadget_name)

    gadget_download_URL = "https://github.com/frida/frida/releases/download/10.6.21/frida-gadget-10.6.21-android-arm.so.xz"
    gadget_base_download_name = re.sub('\.so.xz$', '', gadget_download_URL.split("/")[len(gadget_download_URL.split("/")) - 1])
    gadget_base_download_path = path.join(resources_dir, gadget_base_download_name)
