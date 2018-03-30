import time
def A(n):
    time.sleep(2)
    print(n)
    if n == 10:
        try:
            raise AttributeError
        except:
            return A(n)
    return A(n+1)
if __name__ == '__main__':
    A(1)
