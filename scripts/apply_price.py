#!/usr/bin/env python3

from argparse import ArgumentParser
import json
import logging
import sys
import traceback


logging.basicConfig(
	level=logging.INFO,
	handlers=[]
)

logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
log = logging.getLogger(__name__)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
log.addHandler(consoleHandler)


class Processor:
	def __init__(self, args):
		self.args = args


	def process(self, fname):
		new_contnent = ""
		with open(fname, "r") as f:
			new_content = self.process_file(f)

		fname_out = args.output if args.output else fname

		with open(fname, "w") as f:
			json.dump(new_content, f, indent=2)
		with open(fname, "a") as f:
			f.write("\n")


	def process_file(self, fin):
		j = json.load(fin)

		prices = self.load_price()

		variables = j["templating"]["list"]

		for var in variables:
			if not var["name"].startswith("price"):
				continue

			idx = int(var["name"].replace("price", ""))
			var["query"] = str(prices[idx])

		return j


	def load_price(self):
		with open(self.args.price_file, "r") as f:
			res = json.load(f)
			if len(res) != 24:
				log.error(f"Found {len(res)} price elements instead of 24")
				raise Exception(f"Found {len(res)} price elements instead of 24")

			return res


def main(args):
	p = Processor(args)

	p.process(args.config)

	return 0


if __name__ == '__main__':
	try:
		parser = ArgumentParser()
		parser.add_argument("-d", "--debug", default=False, action="store_true")

		parser.add_argument("-c", "--config", default="grafana/data/dashboards/shelly-plug.json")
		parser.add_argument("-p", "--price-file", default="price.json")
		parser.add_argument("-o", "--output", default="")

		args = parser.parse_args()

		if args.debug:
			log.setLevel(logging.DEBUG)

		log.info("{}".format(__file__))

		res = main(args)
	except SystemExit:
		raise
	except:
		traceback.print_exc()
		sys.exit(-1)
