"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast, at most 140 characters, for a city
that does not exist, to /output/entry.txt. Standard library only.
"""

import os

FORECAST = (
    "In Umbrella Falls, rain falls upwards today, so leave your brolly "
    "at home \u2014 your bus driver is handing out dry socks and free smiles."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORECAST + "\n")


if __name__ == "__main__":
    main()
