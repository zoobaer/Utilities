# 🔧 Makefile template - Helps build your projects with more ease

A collection of tools to help you get started with writing C programs easily.

---

## 🚀 Features

- Compile code
- Run code
- Debug Code
- Profile Code
- Coverage of code
- Check for memory leaks using Valgrind and compiler
- List syscalls
- Print symbol table
- Strip binary of symbols
- Disassemble the executable
- View binary code in executable
- Some builtin features are available
  - logger.h: error(FILE stream, char *type, char *message), info(FILE stream, char *type, char *message)
  - colors.h: colors for output


---

## Pre-requisites

You need to have these tools installed

- Compiler(gcc, clang) [You can adjust in the makefile]
- Memory analyzer (valgrind)
- Debugger (gdb, lldb) [You can adjust in the makefile]
- Hex editor (bless) [You can adjust in the makefile]
- Tracer (strace, ltrace)
- ELF format reader (readelf)
- Object file explorer (objdump)
- Symbol discard-er (strip)
- Profiler (gprof)
- Coverage Testing (gcov)

---

## How to use

* ```bash make release```
* ```bash make debug```
* ```bash make valgrind```





### To summarize

```bash
gcc
clang
valgrind
gdb
lldb
bless
strace
ltrace
readelf
objdump
strip
gprof
gcov
```
---

🛠️ Build & Run

make debug

👤 Author

Zubair
Student @ Kardan University
