#!/usr/bin/env python3

import enforce


@enforce.runtime_validation
def compose_hello_world(first_name: str, last_name: str) -> str:
    return f'Hello {first_name} {last_name}! You just delved into python.'


@enforce.runtime_validation
def main() -> None:
    first_name = input()
    last_name = input()
    print(compose_hello_world(first_name, last_name))


if __name__ == '__main__':
    main()
