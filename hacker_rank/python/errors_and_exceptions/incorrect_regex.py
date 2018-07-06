#!/usr/bin/env python3

import enforce
import re

@enforce.runtime_validation
def main() -> None:
    for _ in range(int(input().strip())):
        try:
            re.compile(input())
            print(True)
        except:
            print(False)


if __name__ == '__main__':
    main()
