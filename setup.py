import cx_Freeze
import sys


base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("MRunTest.py", base=base)]

cx_Freeze.setup(
    name = "MaccorFileGen",
    options = {"build_exe": {"packages":["tkinter"]}},
    version = "0.1",
    description = "My GUI application!",
    executables = executables
    )


