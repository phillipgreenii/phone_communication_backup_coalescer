import logging
import sys

import cli

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')


def main():
    cli.run(sys.argv[1:])


if __name__ == "__main__":
    main()
