from os import path

from config import Config
from file_parser import File_Parser

# print("[*]: {}").format(Config.resources_dir)
# print("[*]: {}").format(Config.output_file)
# print("[*]: {}").format(Config.input_file)
# print("[*]: {}").format(Config.gadget_base_download_path)

FP = File_Parser()

# print(">> {}").format(Config.time_str)

FP.decompile_apk()
FP.inject_gadget_lib()
FP.inject_gadget_code()
