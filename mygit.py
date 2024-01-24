import argparse, os

def init(repo):
    """Create directory repo and .git directory."""
    os.mkdir(repo)


if __name__ == "__main__":  
    # Create a new ArgumentParser object.
    parser = argparse.ArgumentParser()       

    # dest:     Name of the attribute under which sub-command name will be
    # stored.  metavar:  String presenting available sub-commands in help.
    # required: Set True to force the option.
    sub_parsers = parser.add_subparsers(dest='command', metavar='command',
                                        required=False)     
    
    # when get the user input init, call this specific sub_parser
    sub_parser = sub_parsers.add_parser('init',
                help='initialize a new repo')
    sub_parser.add_argument('repo',
                help='directory name for new repo')
    

    args = parser.parse_args()
    if args.command == "init":
        init(args.repo)
