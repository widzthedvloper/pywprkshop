import sys

arguments = sys.argv

arguments = arguments[1:]

print(f"We received these arguments: {arguments}")

print(f"We're currently running on a {sys.platform} machine")