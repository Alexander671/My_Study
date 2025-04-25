from multiprocessing import Pool
import multiprocessing

def say_hello(name: str) -> str:
    return f'Hi there, {name}'


if __name__ == "__main__":
    with Pool() as process_pool:  # A
        hi_jeff = process_pool.apply_async(say_hello, args=('Jeff',))  # B
        hi_john = process_pool.apply_async(say_hello, args=('John',))
        print(multiprocessing.cpu_count())
        print(hi_jeff.get())
        print(hi_john.get())