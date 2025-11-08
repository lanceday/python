#!/usr/bin/env python3
"""
Reusable Brainfuck interpreter.
Paste a program when prompted and press Enter twice to finish.
"""

import sys

def run_brainfuck(code: str, input_stream: str = "") -> str:
    """Execute Brainfuck code and return the output string."""
    # Keep only the 8 Brainfuck commands
    code = ''.join(c for c in code if c in '><+-.,[]')

    memory = [0] * 30000          # start with 30 000 cells
    ptr = 0                       # data pointer
    pc = 0                        # program counter
    output = []
    input_idx = 0

    # Build jump table for [ and ]
    jump = {}
    stack = []
    for i, cmd in enumerate(code):
        if cmd == '[':
            stack.append(i)
        elif cmd == ']':
            if not stack:
                raise SyntaxError(f"Unmatched ']' at position {i}")
            open_pos = stack.pop()
            jump[open_pos] = i
            jump[i] = open_pos
    if stack:
        raise SyntaxError(f"Unmatched '[' at position {stack[-1]}")

    while pc < len(code):
        cmd = code[pc]

        if cmd == '>':
            ptr += 1
            if ptr >= len(memory):          # grow memory on demand
                memory.append(0)
        elif cmd == '<':
            if ptr > 0:
                ptr -= 1
        elif cmd == '+':
            memory[ptr] = (memory[ptr] + 1) & 0xFF   # wrap at 256
        elif cmd == '-':
            memory[ptr] = (memory[ptr] - 1) & 0xFF
        elif cmd == '.':
            output.append(chr(memory[ptr]))
        elif cmd == ',':
            if input_idx < len(input_stream):
                memory[ptr] = ord(input_stream[input_idx])
                input_idx += 1
            else:
                memory[ptr] = 0                 # EOF → 0
        elif cmd == '[':
            if memory[ptr] == 0:
                pc = jump[pc]
        elif cmd == ']':
            if memory[ptr] != 0:
                pc = jump[pc]

        pc += 1

    return ''.join(output)


def read_multiline(prompt: str) -> str:
    """Read lines until two consecutive empty lines."""
    print(prompt)
    print("(Press Enter twice on an empty line when finished.)\n")
    lines = []
    empty = 0
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line == "":
            empty += 1
            if empty == 2:
                break
        else:
            empty = 0
            lines.append(line)
    return '\n'.join(lines)


def main():
    print("=== Reusable Brainfuck Decoder ===\n")
    while True:
        program = read_multiline("Paste the Brainfuck message to decode:")

        if not program.strip():
            print("Nothing entered – try again.\n")
            continue

        try:
            result = run_brainfuck(program)
            print("\n--- Decoded output ---")
            print(result if result else "(no output)")
        except Exception as e:
            print("\nError:", e, file=sys.stderr)

        again = input("\nDecode another message? (y/n): ").strip().lower()
        if again not in ('y', 'yes'):
            print("Goodbye!")
            break
        print()   # blank line for readability


if __name__ == "__main__":
    main()