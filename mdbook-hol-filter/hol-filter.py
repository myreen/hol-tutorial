#!/usr/bin/env python3

import json
import sys
import subprocess

def run_unix_command(command, input_str):
    result = subprocess.run(
        command,
        input=input_str,
        text=True,
        capture_output=True,
        check=False   # raises an error if the command fails
    )
    if (result.returncode == 0):
        return result.stdout
    else:
        return "*HOL failed:*\n```\n" + result.stderr + "\n```"

if __name__ == '__main__':
    if len(sys.argv) > 1: # we check if we received any argument
        if sys.argv[1] == "supports":
            # then we are good to return an exit status code of 0, since the other argument will just be the renderer's name
            sys.exit(0)

    # load both the context and the book representations from stdin
    context, book = json.load(sys.stdin)
    # and now, we can just modify the content of the first chapter
    #with open("/home/myreen/del.txt", "w") as f:
    #    print(book, file=f)
    for s_index in book['sections']:
        s_index['Chapter']['content'] = run_unix_command(["/home/myreen/HOL/Manual/Tools/polyscripter"],s_index['Chapter']['content'])
    # we are done with the book's modification, we can just print it to stdout,
    print(json.dumps(book))
