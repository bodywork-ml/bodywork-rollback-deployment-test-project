"""
This module defines what will happen in stage-1.
"""
from datetime import datetime


def main() -> None:
    now = datetime.now()
    print(f'now={now}')


if __name__ == '__main__':
    main()
