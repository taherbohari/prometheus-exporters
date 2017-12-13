import argparse
import subprocess

def main():		
	parser = argparse.ArgumentParser()
	parser.add_argument("option", help="first option")
	args = parser.parse_args()
	subprocess.call(['df','-'+args.option])
main()

