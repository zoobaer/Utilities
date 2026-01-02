# Adjust for compilation
CC = gcc
DEBUGGER = gdb
HEX = bless
STD = c89

# TODO: Remember to prepend the file with 'build/'!!!
ARGS =

# TODO: The file written before should depend on the file after it!!!
SOURCES = src/*.c
INCLUDE = -Iinclude -Iinclude/builtin
BUILTIN_SOURCES = test/*.c benchmark/*.c include/builtin/*.c
EDITOR = vi
LIB =
DLL =

EXE = build/main.out
COMPILE = -std=$(STD) $(LIB) $(DLL) $(INCLUDE) -o $(EXE) $(SOURCES) $(BUILTIN_SOURCES) $(INCLUDE)

# Valgrind
VALGRIND_COMMON_FLAGS = -s --track-origins=yes --vgdb=yes leak-check=full --verbose
MEMCHECK_FLAGS = --leak-check=full --show-leak-kinds=all
MASSIF_FLAGS = --tool=massif --time-unit=B
CALLGRIND_FLAGS = --tool=callgrind
HELGRIND_FLAGS = --tool=helgrind
DRD_FLAGS = --tool=drd



# compilation-related
DEBUG = -O0 -DDEBUG -g -march=native -mtune=native -fstack-protector-strong -Wall -Wextra -pedantic -Wpointer-arith -Wcast-align -Wconversion -Wsign-conversion -Wunused -Wunused-parameter -Wstrict-prototypes -Wshadow -Wfloat-equal -Winline -Wundef -Wuninitialized
SANITIZE = -fanalyzer -fsanitize=address,undefined
SANITIZE_CLANG = $(DEBUG),memory
PROFILE = -O2 -pg -fno-omit-frame-pointer -g
COVERAGE = -O0 -fprofile-arcs -ftest-coverage -g
RELEASE = -O2 -march=native -mtune=native -DNDEBUG -Wall -Wextra -Wno-unused-parameter -fstack-protector-strong


all: compile debug profile valgrind coverage syscalls libcalls objdump strings readelf disassembly hex

release: compile_release strip
	@echo "Running program..."
	$(EXE) $(ARGS)
	@echo "Done."

debug: compile
	@echo "Running debugger..."
	$(DEBUGGER) $(EXE)
	@echo "DONE."

run: compile
	@echo "Running program..."
	./$(EXE) $(ARGS)

syscalls: compile
	@echo "Running strace to show system calls..."
	strace $(EXE) $(ARGS)

libcalls: compile
	@echo "Running ltrace to show library calls..."
	ltrace $(EXE) $(ARGS)

strings: compile
	@echo "Listing strings in the executable..."
	strings $(EXE)
	@echo "Done."

readelf: compile
	@echo "Printing the symbol table..."
	readelf --symbols $(EXE)
	@echo "Done."
	@echo "Printing segments..."
	readelf --segments $(EXE)
	@echo "Done."

strip: compile
	@echo "Stripping the binary of symbols..."
	strip $(EXE)
	@echo "Done."

objdump: compile
	@echo "Printing the symbol table..."
	objdump -t $(EXE)
	@echo "Done."
	@echo "Printing sections..."
	objdump -s $(EXE)
	@echo "Done."

disassembly: compile
	@echo "Printing disassembly..."
	objdump -d $(EXE)
	@echo "Done."

hex: compile
	$(HEX) $(EXE)

profile: $(SOURCES)
	@echo "Compiling for profiling..."
	$(CC) $(COMPILE) $(PROFILE)
	@echo "Done."
	@echo "Running program..."
	./$(EXE) $(ARGS)
	@echo "Done."
	@echo "Profiling the program..."
	@echo "gprof uses 'gmon.out'!"
	gprof $(EXE) > profile
	@echo "Viewing profiling results..."
	$(EDITOR) profile
	@echo "Done."

coverage: pre_coverage
ifneq ($(FILE),)
	@echo "Showing results..."
	$(EDITOR) $(FILE).c.gcov
else
	@echo "Please set FILE variable"
endif
	@echo "FILE must follow this pattern '*.c.cov'"

pre_coverage: $(SOURCES)
	@echo "Compiling for coverage..."
	$(CC) $(COMPILE) $(COVERAGE)
	@echo "Done."
	@echo "Running program..."
	./$(EXE) $(ARGS)
	@echo "Done."

ifneq ($(FILE),)
	@echo "Running code coverage analysis..."
	@echo "gcov uses the 'file.gcda'!"
	gcov $(EXE)-$(FILE).gcda > build/$(FILE)-line_coverage
	@echo "Done."
	@echo "Viewing no of lines run results..."
	$(EDITOR) build/$(FILE)-line_coverage
	@echo "Done."
else
	@echo "Please set FILE variable"
	@echo "FILE must follow this pattern 'file' without the .c extension"
endif

valgrind: compile
	@echo "Running with Valgrind for memory with checks..."
	valgrind $(VALGRIND_COMMON_FLAGS)  $(EXE) $(ARGS)
	@echo "Done."

valgrind-memcheck: compile
	@echo "Running memory check with Valgrind..."
	valgrind $(VALGRIND_COMMON_FLAGS) $(MEMCHECK_FLAGS) --log-file=build/valgrind-memcheck.log $(EXE) $(ARGS)
	@echo "Done."

valgrind-massif: compile
	@echo "Running heap profiling using Valgrind..."
	valgrind $(VALGRIND_COMMON_FLAGS) $(MASSIF_FLAGS) --log-file=build/valgrind-massif.log $(EXE) $(ARGS)
	@echo "Done."

valgrind-callgrind: compile
	@echo "Running callgrind for performance..."
	valgrind $(VALGRIND_COMMON_FLAGS) $(CALLGRIND_FLAGS) --log-file=build/valgrind-callgrind.log $(EXE) $(ARGS)
	@echo "Done."

valgrind-helgrind: compile
	@echo "Running helgrind for thread race detection..."
	valgrind $(VALGRIND_COMMON_FLAGS) $(HELGRIND_FLAGS) --log-file=build/valgrind-helgrind.log $(EXE) $(ARGS)
	@echo "Done."

valgrind-drd: compile
	@echo "Running drd for precise thread race detection..."
	valgrind $(VALGRIND_COMMON_FLAGS) $(DRD_FLAGS) --log-file=build/valgrind-drd.log $(EXE) $(ARGS)
	@echo "Done."

valgrind-all: valgrind-memcheck valgrind-massif valgrind-callgrind valgrind-helgrind valgrind-drd
	@echo "All Valgrind checks complete. Check 'build/' directory for logs."

sanitize: $(SOURCES)
	@echo "Compiling with sanitization on..."
	$(CC) $(COMPILE) $(SANITIZE)
	@echo "Done."

sanitize_clang: $(SOURCES)
	@echo "Compiling with sanitization on..."
	clang $(COMPILE) $(SANITIZE)
	@echo "Done."

# $(ADD) can be used while using the make command in terminal
compile: $(SOURCES)
	@echo "Compiling for debugging..."
	$(CC) $(COMPILE) $(DEBUG) $(ADD)
	@echo "Done."

compile_clang: $(SOURCES)
	@echo "Compiling for debugging using clang..."
	clang $(COMPILE_CLANG) $(DEBUG_CLANG) $(ADD)
	@echo "Done."

compile_release: $(SOURCES)
	@echo "Compiling for release..."
	$(CC) $(COMPILE) $(RELEASE) $(ADD)
	@echo "Done."

generate_assembly: $(SOURCES)
	@echo "Generating assembly..."
ifneq ($(FILE),)
	$(CC) $(COMPILE) -S $(FILE)
	@echo "Assembly generated..."
else
	@echo "Format should be 'make generate_assembly FILE=file.c'"
	@echo "Operation aborted!!"
endif

install: compile_release


test: compile_release


clean:
	@echo "Cleaning obj directory..."
	rm -rf obj/*
	@echo "Cleaning build directory..."
	rm -rf build/*
	@echo "Removing gmon.out..."
	rm -rf gmon.out
	@echo "Removing *.gcov..."
	rm -rf ./*.gcov
	@echo "Removing profile file..."
	rm -rf profile
	@echo "Done."



### extra might be needed

# check if a file exists and move it
#ifneq ("$(wildcard ./gmon.out)", "")
#	@echo "gmon.out exists..."
#	@echo "Attempting to move to build/gmon.out"
#	mv gmon.out build/gmon.out
#else
#	@echo "gnom.out does not exist..."
#endif

# OBJ = $(SRC:.c=.o)

# .PHONY: all clean

# all: $(TARGET)

# $(TARGET): $(OBJ)
#	$(CC) $(LDFLAGS) -o $@ $^

# %.o: %.c
#	$(CC) $(CFLAGS) -c $< -o $@

# clean:
#	rm -f $(TARGET) $(OBJ)
