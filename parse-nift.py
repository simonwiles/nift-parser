#!/usr/bin/env python3

""" parse-nift.py """

import argparse
import logging

from xmltotabular import XmlCollectionToTabular


def main():
    """Command-line entry-point."""
    arg_parser = argparse.ArgumentParser(description="Description: {}".format(__file__))

    arg_parser.add_argument(
        "-i",
        "--xml-input",
        action="store",
        nargs="+",
        required=True,
        help="XML file or directory of XML files (*.{xml,XML}) to parse"
        " (multiple arguments can be passed)",
    )

    arg_parser.add_argument(
        "-c",
        "--config",
        action="store",
        required=True,
        help="config file (in YAML format)",
    )

    arg_parser.add_argument(
        "-o",
        "--output-path",
        action="store",
        required=True,
        help="path to folder or file in which to save output (will be created if necessary)",
    )

    arg_parser.add_argument(
        "--output-type",
        choices=["csv", "sqlite"],
        action="store",
        default="sqlite",
        help="output a sqlite database (default) or csv files (one per table)",
    )

    arg_parser.add_argument(
        "--sqlite-max-vars",
        action="store",
        type=int,
        help="Override the maximum number of host parameters than can be passed in "
        "a single SQLite statement (defaults to 999)",
    )

    arg_parser.add_argument(
        "-r",
        "--recurse",
        action="store_true",
        help="search subdirectories for XML files (*.{xml,XML}) to parse",
    )

    arg_parser.add_argument(
        "--processes",
        action="store",
        type=int,
        help="number of processes to use for parallel processing of XML documents"
        " (defaults to num_threads - 1)",
    )

    arg_parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="increase verbosity (can be passed multiple times)",
    )

    args = arg_parser.parse_args()

    log_level = (logging.WARN, logging.INFO, logging.DEBUG)[args.verbose]

    del args.verbose

    collectionTransformer = XmlCollectionToTabular(**vars(args), log_level=log_level)
    collectionTransformer.convert()


if __name__ == "__main__":
    main()
