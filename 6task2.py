
def retry():

    def _decorator(func):
        def wrapper(*args,**kwargs):
            for attempt in range(1, 10):
                try:
                    return func(*args,**kwargs)
                except Exception as e:

                    print(str(attempt)+"раз(а)",e)
            print("Остановись")
            print("Перебор попыток")

        return wrapper
    return _decorator

@retry()
def func():
    raise ValueError("Функция работает")
func()