#!/usr/bin/env python

# improt modules
from loguru import logger
import sys
import argparse
from tqdm import tqdm
import typer

# # define arparse
# parser = argparse.ArgumentParser(description="some fun with logger")
# parser.add_argument("-o", help="this statment will get sent to log")
# args = parser.parse_args()

# # message
# message = args.o

app = typer.Typer()

import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

@app.command()
def main(message: str):
    # add log file and print statement to it
    logger.add("out.log")
    logger.info(message, serialize=True)

    for i in tqdm(range(90000000), desc="just testing tqdm", ncols=100):
        pass

    logger.info("completed first tqdm", serialize=True)

    for i in tqdm(range(900000), desc="shorter", ncols=100):
        pass

    logger.success("completed")

    typer.echo(f"{message}")

@app.command()
def goodbye(message: str, name: str):
    typer.echo(f"{message}, {name}")

if __name__ == "__main__":
    app()
