import argparse


def new(args):
    """
    Creates a new project or solution
    :param args: the parsed arguments namespace from argparse
    """
    pass


def edit(args):
    """
    Edits an existing project or solution
    :param args: the parsed arguments namespace from argparse
    """
    pass


def build(args):
    """
    Builds an existing solution or project
    :param args: the parsed arguments namespace from argparse
    """
    pass


def list_sdks(args):
    """
    Lists installed SDKs
    :param args: the parsed arguments namespace from argparse
    """
    pass


ACTIONS = {
    'new': new,
    'edit': edit,
    'build': build,
    'list-sdks': list_sdks
}


def build_parser():
    """
    :return: an initialized ArgumentParser object
    :rtype: argparse.ArgumentParser
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=ACTIONS.keys())
    parser.add_argument('--solution', help='use this solution')
    parser.add_argument('--project', help='use this project')
    parser.add_argument('--configuration', help='use this configuration')
    parser.add_argument('--platform', help='use this platform')
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    ACTIONS[args.action](args)


if __name__ == '__main__':
    main()
