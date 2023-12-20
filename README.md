[![Actions Status](https://github.com/yuukis/yamanashi-icalendar-updater/workflows/Release%20event.ics/badge.svg)](https://github.com/yuukis/yamanashi-icalendar-updater/actions)

# yamanashi-icalendar-updater

iCalendar generator for tech events in Yamanashi Prefecture.

<!-- ABOUT THE PROJECT -->
## About The Project

This is a simple script that generates a calendar of tech events in Yamanashi Prefecture in iCalendar format and uploads it to a public repository.

This script obtains event data from [Connpass](https://conpass.com) via API and converts it to iCalendar format.

The iCalendar file is available at the following URL

```
https://calendar.yamanashi.dev/event.ics
```

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* Python 3.8 or later 

### Installation

1. Get a personal access token at [GitHub](https://github.com/settings/tokens)
2. Clone the repo
    ```sh
    git clone https://github.com/yuukis/yamanashi-icalendar-updater.git
    ```
3. Install dependencies
    ```sh
    pip install -r requirements.txt
    ```
4. Add your application configuration to your .env file in the root of your project.
    ```ini
    GITHUB_TOKEN=YOUR_PERSONAL_ACCESS_TOKEN
    GITHUB_OWNER=YOUR_DESTINATION_REPO_OWNER
    GITHUB_REPO=YOUR_DESTINATION_REPO_NAME
    ```

<!-- USAGE EXAMPLES -->
## Usage

```sh
python main.py
```

<!-- LICENSE -->
## License

Distributed under the Apache License, Version 2.0. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Yuuki Shimizu - [@yuuki_maxio](https://x.com/yuuki_maxio) 

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [shingen.py](https://shingenpy.connpass.com)
  - python user community in Yamanashi, Japan
* [Connpass](https://connpass.com)