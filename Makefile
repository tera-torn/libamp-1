default:
	# (Release Mode)
	# Builds *without* debugging symbols and
	# *with* an optimization level of 2.
	scons

clean:
	scons -c
	rm -f *.gcov
	rm -f *.gcda
	rm -f *.gcda.info
	rm -f *.gcno

test: debug-no-opt
	./test_amp

debug:
	# Turn on debugging symbols in compiled assets. Still uses default optimization level
	scons debug=1

debug-no-opt:
	scons debug=1 optimization=0

coverage:
	BUILD_COVERAGE_SUPPORT=1 scons # build with coverage profiling support

	# remove existing files so results from previous runs don't accumulate
	rm -f *.gcov
	rm -f *.gcda
	rm -f *.gcda.info

	# run tests to generate raw coverage files
	./test_amp

	COMPILE_COVERAGE=1 scons # compile raw coverage files to human-readable text

valgrind: debug-no-opt
	CK_FORK=no valgrind --leak-check=full ./test_amp

gdb: debug-no-opt
	CK_FORK=no gdb --args ./test_amp

lldb: debug-no-opt
	CK_FORK=no lldb -f ./test_amp

stats:
	zsh code_stats.zsh

libjansson:
	# build bundled jansson library?
	cd jansson && [ ! -f ./configure ] && autoreconf -i || true
	cd jansson && ./configure --prefix=`pwd`/../tmp-deps
	cd jansson && make
	cd jansson && make install

benchmark:
	cd examples && make benchmark
	examples/asyncserver 22380 &
	examples/benchclient localhost:22380 100000 > benchlog.txt
