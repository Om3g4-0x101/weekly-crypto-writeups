#! /usr/bin/python3
import os
def main():
    while True :
        text = input("[+] ")
        text=text.lower()
        for keyword in ["eval", "exec", "import", "open", "read", "system", "write","os","subprocess","shlex","sh","builtins","class",".","+"]:
            if keyword in text:
                print(f"Gotcha {keyword} !")
                return
        else:
            exec(text)
if __name__ == "__main__":
    main()