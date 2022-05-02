from src.__init__ import cnf
from config import logger

def main():
    from src.bot import run
    run()

if __name__ == '__main__':
    try:
        import sys
        import argparse
        parser = argparse.ArgumentParser(prog="telegram_bot")
        parser.add_argument("-t", "--token", default=None)
        args = parser.parse_args(sys.argv[1:])
        logger.error("--> SET CONFIG")
        cnf.set(token=args.token)
        logger.error("--> START BOT")
        main()
    except Exception as error:
        print(f"\nERROR: {error}\n")
    finally:
        cnf.delete()
