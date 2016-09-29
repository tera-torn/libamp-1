default:
	# build all examples, including benchmarks.
	scons

benchmarks: default
	# set up and run all benchmarks
	python run_benchmarks.py

clean:
	scons -c

debug:
	scons debug=1
