#!/usr/bin/env python3
import subprocess
import re


def main():
    exclude = ["dependabot[bot]"]
    command = "git shortlog -sne HEAD"
    process = subprocess.run(
        command.split(), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    pattern = re.compile(r"^(?P<commits>\d+)\s+(?P<name>.*)\s+(?P<email>\S+)$")

    with open("CONTRIBUTORS", "w") as f:
        f.write("Contributors ordered by number of commits:\n")
        f.write("==========================================\n")
        for line in process.stdout.decode().strip().splitlines():
            match = pattern.match(line.strip())
            if match['name'] not in exclude:
                f.write(f"{match['name']} {match['email']}\n")


if __name__ == "__main__":
    main()
