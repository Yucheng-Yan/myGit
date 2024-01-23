import argparse

if __name__ == "main":  
    # Create a new ArgumentParser object.
    parser = argparse.ArgumentParser()       

    # dest:     Name of the attribute under which sub-command name will be stored.
    # metavar:  String presenting available sub-commands in help.
    # required: Set True to force the option.
    sub_parsers = parser.add_subparsers(dest='command', metavar='command', required=True)     


