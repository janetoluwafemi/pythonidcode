from prime_numbers import numbers_in_prime_number
def test_number_is_a_prime_number():
    assert numbers_in_prime_number(7).isPrime == [2,3,5,7,9]
