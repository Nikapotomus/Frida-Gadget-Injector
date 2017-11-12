from os import path
from config import Config

import subprocess

class File_Parser:

    def __init__(self):
        pass

    def inject_gadget_code(self):
        if path.exists(Config.resources_dir):
            if path.isfile(Config.input_file):
                print("[*] Injecting code into the manifeset..")
                # flag to check if it has been injected
                injected_code_flag = False

                with open(Config.input_file, "r") as in_file, open(Config.output_file, "w") as out_file:
                    for line in in_file:

                        if "IIII" in line and not injected_code_flag:
                            print("[*] Code injected before: {}").format(line)
                            out_file.write(Config.injection_string)

                            injected_code_flag = True

                        out_file.write(line)

                #replace the input file
                subprocess.call(['mv', Config.output_file, Config.input_file])

            else:
                print("[!] No input manifest file detected, no changes made")

    def inject_gadget_lib(self):
        # Download the gadget specified in the config and put it in the reresouces folder
        print("-"*20)
        print("[*] Downloading the gadget..")
        # -q -q --show-progress --show-progress - Force wget to display the progress bar in any verbosity
        subprocess.call(['wget', Config.gadget_download_URL, '-P', Config.resources_dir, "-q", "--show-progress"])
        # unxz the download
        print("[*] unxz the gadget..")
        subprocess.call(['unxz', Config.gadget_base_download_path + ".so.xz"])
        # rename the gadget
        print("[*] Renaming the gadget..")
        subprocess.call(['mv', Config.gadget_base_download_path + ".so", Config.renamed_gadget_path])
        # move the gadget into the target lib
        print("[*] Injecting the gadget lib..")
        subprocess.call(['mv', Config.renamed_gadget_path, Config.inject_lib_path])

    def decompile_apk(self):
        print("[*] Decompiling APK..")

        # subprocess.call(['apktool', 'd', '-o', out_dir, original.apk])

        pass
