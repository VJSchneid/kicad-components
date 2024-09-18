#!/usr/bin/python

import glob
import re
import shutil
import os

kicad_sym_files = glob.glob("**/*.kicad_sym")

out_f = open("vjs.kicad_sym", "w", encoding="utf-8")

out_f.write("""(kicad_symbol_lib (version 20231120) (generator "kicad_symbol_editor") (generator_version "8.0")\n""")

for sym_file in kicad_sym_files:
    in_f = open(sym_file, "r", encoding="utf-8")
    content = in_f.read()
    print(sym_file)
    symbol_match = re.match(r"\s*\(kicad_symbol_lib .*?([ \t]*\(symbol .*)\)\s*$", content, re.MULTILINE | re.DOTALL)
    out_f.write(symbol_match.group(1))
    in_f.close()

out_f.write(")")

footprint_files = glob.glob("**/*.kicad_mod")


os.makedirs("vjs.pretty", exist_ok=True)
for foot_file in footprint_files:
    print(foot_file)
    try:
        shutil.copyfile(foot_file, "vjs.pretty/" + os.path.basename(foot_file))
    except shutil.SameFileError:
        pass