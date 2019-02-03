import subprocess as sp
PROMPT = ">>>"
CMD = "/usr/bin/env python3 %s"
if (__name__ == "__main__"):
    print(PROMPT, "Greetings from the parent script")
    print(PROMPT, "Kicking off child script")
    cmd = CMD % ("child.py")
    sp.call(cmd.split(" "))
    print(PROMPT, "child script successfully executed")
