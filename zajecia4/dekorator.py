import time
import functools

def timer(unit='seconds'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            czas_trwania = end - start
            if unit == 'seconds':
                print(f'Funkcja {func.__name__} wykonała się przez {czas_trwania:.6f} sekund')
            elif unit == 'microseconds':
                print(f'Funkcja {func.__name__} wykonała się przez {czas_trwania*1000000:.6f} mikrosekund')
            else:
                print('Nieznana jednostka czasu. Wybierz "seconds" lub "microseconds".')
            return result
        return wrapper
    return decorator

@timer()
def przyklad():
    for i in range(1, 1000):
        wynik=(3*i**2+12-5554)*77*(-1)
        print(wynik)
przyklad()