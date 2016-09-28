# libamp
C library implementation of AMP (Asynchronous Messaging Protocol)

From: https://amp-protocol.net/Libamp

libamp is developed by Eric Mangold and Peter LeBek (and other contributors).

 Features include:

* Pure C99 C code. Works with C++, and other languages, via normal C API.
* Extensive examples in the /examples dir.
* No external dependencies. Just requires scons to build.
* Fully functional and fast protocol-parser.
* Command dispatch; request/response/error handling.
* Reply to a command synchronously within the handler function, or reply later asynchronously.
* Support for many common AMP types (All primitive types supported; "compound" types lacking).
* Virtually 100% unit-test coverage, including malloc()-failure tests; runs Valgrind-clean.
* Can be synchronously or asynchronously driven.
* Not tied to any particular networking library. Use libevent, libuv, etc.
* Transport-agnostic; use libamp over stdio as easily as TCP or SSL sockets.

