import sys
import argparse

from src.__init__ import cnf
from config import logger

def run_bot():
    from src.bot import run
    run()

def main():
    try:
        parser = argparse.ArgumentParser(prog="telegram_bot")
        parser.add_argument("-t", "--token", default=None)
        args = parser.parse_args(sys.argv[1:])
        logger.error("--> SET CONFIG")
        cnf.set(token=args.token)
        logger.error("--> START BOT\n")
        run_bot()
    except Exception as error:
        logger.error(f"\nERROR: {error}\n")
    finally:
        logger.error("\n--> DEL CONFIG")
        cnf.delete()