from argparse import ArgumentParser, Namespace


def get_argparse() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog="GH All issues",
        usage="This program generates an interval tree from a JSON file containing a GitHub repositories issues.",
    )
    parser.add_argument(
        "-r",
        "--repository",
        help='GitHub repository to be used. Format needs to be "OWNER/REPO". Default is numpy/numpy',
        default="numpy/numpy",
        type=str,
        required=False,
    )

    parser.add_argument(
        "-t",
        "--token",
        help="GitHub personal access token",
        type=str,
        required=True,
    )

    parser.add_argument(
        "-s",
        "--save-json",
        help="Save analysis to JSON file. EX: --save-json=issues.json",
        default="issues.json",
        type=str,
        required=True,
    )
    return parser.parse_args()