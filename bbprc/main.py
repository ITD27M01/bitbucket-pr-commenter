import logging
from bbprc.arguments import args_parser
from bbprc.comment import send_comment

_log = logging.getLogger(name=__name__)


def main():
    args = args_parser()

    if args.debug:
        level = getattr(logging, 'DEBUG', None)
    else:
        level = getattr(logging, 'INFO', None)

    logging.basicConfig(level=level)

    exit_code = 1

    try:
        _log.debug("Send comment to BitBucket PR")
        result = send_comment(args.server,
                              args.token,
                              args.project,
                              args.repo,
                              args.pr,
                              args.greeting, args.file, args.verify)
        if result:
            exit_code = 0
    except Exception as e:
        print(f"Something went wrong: {e}. Try to --debug it")

    return exit_code


if __name__ == '__main__':
    exit(main())
