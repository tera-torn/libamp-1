# libamp
C library implementation of AMP (Asynchronous Messaging Protocol)

From: https://amp-protocol.net/Libamp

libamp is developed by Eric Mangold and Peter LeBek (and other contributors).

## Features

* No external dependencies. Only links against the C std lib.
* Many examples and benchmarks in the /examples dir.
* Pure C99 C code. Works with C++, and other languages, via normal C API.
* Highly portable - builds on Linux/\*nix, Mac OSX, Windows (with MingW), Cygwin, etc.
* Supports static or dynamic linking (Builds both versions of the library by default).
* Fully functional and fast AMP protocol parser.
* Command dispatch; request/response/error handling.
* Reply to a command synchronously within the handler function, or reply later asynchronously.
* Support for many common AMP types.
* Virtually 100% unit-test coverage, including malloc()-failure tests; runs Valgrind-clean.
* Can be synchronously or asynchronously driven.
* Not tied to any particular networking library. Use libevent, libuv, etc.
* Transport-agnostic; use libamp over stdio as easily as TCP or SSL sockets.

## Docs

See `amp.h` for API documentation.

## Usage

Just type `scons` (or `make`) to create an optimized non-debug build of libamp - both static and dynamic versions of the library are created, by default.

See `Makefile` for all other useful build targets. For building on Windows you may just use `scons` from a Command Prompt instead of the make targets.

## Requirements

Requires `check` (`apt-get install check`) to build, as the test suite binary `test_amp` uses it. 

The examples require `libevent` (version 2) (`apt-get install libevent-dev`) to build and run.

