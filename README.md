# Overview

Small utility to test the speed of pure Python, Python + Numba and Python + C library via SWIG

* Tests empty function calls (how expensive is it just calling these functions)
* Tests calling a function with many tight loops (yes, this prime number calculation is an abysmal affront to all of computationdom)

Remember numba requires warmup.

# Dependencies

* Python.h (`apt install python3-dev`)
* Swig (`apt install swig`)

# Setup

* Build C lib with included `./build.sh` (might need `chmod +x ./build.sh` first)
* Run `python ./main.py`

# Config

Configure params in `main.py`
