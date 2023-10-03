"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
  if number_of_primes < 0:
    raise ValueError
  list = []
  count_primes = 0
  running_count = 2
  while count_primes < number_of_primes:
      i = running_count - 1
      mods = 0
      while i > 0:
          if (running_count % (running_count - i)) != 0:
              mods += 1
          i -= 1
      if mods == (running_count - 2):
           count_primes += 1
           list.append(running_count)
      running_count += 1
  return list
