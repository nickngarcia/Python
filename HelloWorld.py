
import sys


def main():
	"""Print a greeting. Optionally accepts a name as the first CLI argument."""
	name = sys.argv[1] if len(sys.argv) > 1 else "World"
	print(f"Hello, {name}!")


if __name__ == "__main__":
	main()

