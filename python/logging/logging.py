"""Convenience wrappers for standard library logging module.

Features:
- Get level from command line
- Setup console and file logging
- Use adapters and filters
- Make nice formatters

"""


import argparse
import logging


def main():
    loglevel = parse_args()



def parse_args() -> str:
    """Get loglevel from command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--loglevel",
        "-l",
        help="Log level for consoe logging",
        choices=("DEBUG", "INFO", "WARNING", "ERROR")
        type=str.upper
    )
    args = parser.parse_args()
    return args.loglevel


def setup_logging(loglevel: str = "INFO"):
    """Use Basic config."""

    # TODO: nice format
    logging.basicConfig(level=loglevel)

    # TODO: add console and file handlers


def get_logger():




if __name__ == "__main__":
    main()