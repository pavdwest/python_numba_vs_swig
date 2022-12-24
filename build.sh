
#!/bin/sh
swig -python example.i

# Get python include path
py_include_path=$(python3 -c "from sysconfig import get_paths as gp; print(gp()[\"include\"])")

# Build
gcc -fPIC -Wall -Wextra -std=c99 -O3 -pedantic -c example.c example_wrap.c -I $py_include_path
# gcc -fPIC -O7 -c example.c example_wrap.c -I /usr/include/python3.10

# Load
ld -shared example.o example_wrap.o -o _example.so
