import os
import sys
import subprocess

def FlyRun(code_path, language, breakpointbool, breakpoint_line,show_values):
    with open(code_path, 'r', encoding="utf-8") as f:
        lines = f.readlines()
    if breakpointbool and breakpoint_line is not None:
        lines.insert(breakpoint_line - 1, "\nbreakpoint()\n")
    code = "".join(lines)
    with open("temp_code.py", "w", encoding="utf-8") as f:
        f.write(code)
    result = subprocess.run(["python", "temp_code.py"], capture_output=True, text=True)
    os.remove("temp_code.py")
    return result.stdout, result.stderr

if __name__ == "__main__":
    print(FlyRun("D:/SwallowEditorSample.py", "python", False, 0, "current_font_size"))