all: test_count_even test_euler test_fibonacci test_fac test_deduplicate test_monte_carlo_pi  test_reverse test_int2hex

test_count_even: clean
	@python count_even/.test.py
	@echo LED-Bit unlocked: 0

test_int2hex: clean
	@python int2hex/.test.py
	@echo LED-Bit unlocked: 1

test_reverse: clean
	@python reverse/.test.py
	@echo LED-Bit unlocked: 2

test_fac: clean
	@python fac/.test.py
	@echo LED-Bit unlocked: 3

test_deduplicate: clean
	@python deduplicate/.test.py
	@echo LED-Bit unlocked: 4

test_fibonacci: clean
	@python fibonacci/.test.py
	@echo LED-Bit unlocked: 5

test_euler: clean
	@python euler/.test.py
	@echo LED-Bit unlocked: 6

test_monte_carlo_pi: clean
	@python monte_carlo_pi/.test.py
	@echo LED-Bit unlocked: 7

clean:
	@find . -name \*.pyc -delete
