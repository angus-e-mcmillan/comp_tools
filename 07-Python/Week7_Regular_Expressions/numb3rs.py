import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    nums = ip.split(".")
    x = 0
    try:
        for num in nums:
            if int(num) > 255:
                    x = x + 1
    except:
         return False
    if x == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
