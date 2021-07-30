

# This is a comment
#import my_module

def add(a: int, b: float) -> float:
    return a + b


def main():
    msg: str = "hello world"
    x: int = 3
    y: float = 3.14
    z: float = add(x, y)
    print("%f" % z)

if __name__ == "__main__":
    main()


