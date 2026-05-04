"""
noaa_scraper.py

Simple NOAA/NCEI USCRN text-file scraper for teaching.

Main improvements:
1. Uses a browser-like User-Agent to reduce HTTP 403 errors.
2. Uses the maxdepth argument correctly.
3. Avoids revisiting URLs.
4. Avoids duplicate downloads.
5. Handles HTTP/URL errors more gracefully.
6. Uses pathlib for cleaner file handling.

Example
-------
from noaa_scraper import get_noaa_temperatures
import matplotlib.pyplot as plt

air_temperatures = get_noaa_temperatures(
    "https://www.ncei.noaa.gov/pub/data/uscrn/products/subhourly01/",
    "Gaylord",
    maxdepth=100
)

plt.plot(air_temperatures)
plt.show()
"""

from pathlib import Path
from html.parser import HTMLParser
from urllib import parse
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from glob import glob

try:
    from ipywidgets import FloatProgress
    from IPython.display import display
    HAS_WIDGETS = True
except Exception:
    HAS_WIDGETS = False


def make_request(url):
    """Create a URL request with browser-like headers."""
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0 Safari/537.36"
        )
    }
    return Request(url, headers=headers)


class LinkParser(HTMLParser):
    """Parse HTML directory listings and collect links."""

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for key, value in attrs:
                if key == "href":
                    new_url = parse.urljoin(self.baseUrl, value)
                    self.links.append(new_url)

    def getLinks(self, url):
        """
        Return a tuple: (data_url, links).

        If URL points to HTML, parse links.
        If URL points to plain text, return the URL as data_url.
        """
        self.links = []

        # IMPORTANT: directory URLs must end with "/"
        if not url.endswith("/") and not url.lower().endswith(".txt"):
            url = url + "/"

        self.baseUrl = url

        try:
            response = urlopen(make_request(url), timeout=30)
        except HTTPError as e:
            print(f"HTTP error {e.code} for URL: {url}")
            return "", []
        except URLError as e:
            print(f"URL error for URL: {url}")
            print(e)
            return "", []
        except Exception as e:
            print(f"Unexpected error for URL: {url}")
            print(e)
            return "", []

        content_type = response.getheader("Content-Type", "")

        if "text/html" in content_type:
            try:
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8", errors="replace")
                self.feed(html_string)
                return "", self.links
            except Exception as e:
                print(f"Could not parse HTML at URL: {url}")
                print(e)
                return "", []

        if "text/plain" in content_type or url.lower().endswith(".txt"):
            return url, []

        return "", []


def download_file(url, output_path):
    """
    Download URL to output_path using custom Request headers.
    """
    output_path = Path(output_path)

    try:
        with urlopen(make_request(url), timeout=60) as response:
            data = response.read()
        output_path.write_bytes(data)
        return True
    except HTTPError as e:
        print(f"HTTP error {e.code} while downloading: {url}")
        return False
    except URLError as e:
        print(f"URL error while downloading: {url}")
        print(e)
        return False
    except Exception as e:
        print(f"Unexpected download error for: {url}")
        print(e)
        return False


def noaa_spider(url, word, maxPages=100, data_dir="data"):
    """
    Crawl a NOAA/NCEI directory tree and download .txt files whose URL
    contains a given search word.

    Parameters
    ----------
    url : str
        Starting directory URL.
    word : str
        Search string. Example: "Gaylord".
    maxPages : int
        Maximum number of HTML directory pages to visit.
    data_dir : str
        Directory where downloaded files are stored.

    Returns
    -------
    foundFiles : set
        Set of found file URLs.
    """
    data_path = Path(data_dir)
    data_path.mkdir(exist_ok=True)

    pagesToVisit = [url]
    numberVisited = 0
    urlsVisited = set()
    foundFiles = set()

    if HAS_WIDGETS:
        progressBar = FloatProgress(min=0, max=maxPages)
        display(progressBar)
        progressBar.value = 0
    else:
        progressBar = None

    while numberVisited < maxPages and pagesToVisit:
        current_url = pagesToVisit.pop(0)

        if current_url in urlsVisited:
            continue

        urlsVisited.add(current_url)

        if current_url.lower().endswith(".txt"):
            if word.lower() in current_url.lower():
                foundFiles.add(current_url)
                print("FOUND", current_url)

                filename = current_url.split("/")[-1]
                output_file = data_path / filename

                if output_file.exists():
                    print("file exists...", output_file)
                else:
                    print("downloading...", output_file)
                    download_file(current_url, output_file)

            continue

        numberVisited += 1
        if progressBar is not None:
            progressBar.value = numberVisited

        print(f"Visiting {numberVisited}/{maxPages}: {current_url}")

        parser = LinkParser()
        _, links = parser.getLinks(current_url)

        for link in links:
            if link not in urlsVisited:
                pagesToVisit.append(link)

    return foundFiles


def read_data_column(filename, col=8, convert_c_to_f=True):
    """
    Read one whitespace-separated column from a NOAA text file.

    Parameters
    ----------
    filename : str
        Path to data file.
    col : int
        Column index to read.
    convert_c_to_f : bool
        If True, convert Celsius to Fahrenheit.

    Returns
    -------
    values : list of float
    """
    values = []

    with open(filename, "r", errors="replace") as f:
        for row in f:
            parts = row.split()

            if len(parts) <= col:
                continue

            try:
                temp = float(parts[col])
            except ValueError:
                continue

            if temp < -9000:
                if not values:
                    temp = 0.0
                else:
                    temp = values[-1]
            else:
                if convert_c_to_f:
                    temp = temp * 9.0 / 5.0 + 32.0

            values.append(temp)

    return values


def get_airtemperature_from_files(data_dir="data", col=8):
    """
    Read all .txt files in data_dir and concatenate the selected column.
    """
    files = sorted(glob(str(Path(data_dir) / "*.txt")))

    if HAS_WIDGETS:
        progressBar = FloatProgress(min=0, max=len(files))
        display(progressBar)
        progressBar.value = 0
    else:
        progressBar = None

    air_temperature = []

    for file in files:
        if progressBar is not None:
            progressBar.value += 1

        print("reading...", file)
        air_temperature += read_data_column(file, col=col)

    return air_temperature


def get_noaa_temperatures(url, name, maxdepth=100, data_dir="data", col=8):
    """
    Crawl NOAA/NCEI data directory, download matching files, and read
    air temperatures.

    Parameters
    ----------
    url : str
        Starting URL.
    name : str
        Search word in file URL, e.g. "Gaylord".
    maxdepth : int
        Maximum number of directory pages to visit.
    data_dir : str
        Local directory for downloaded files.
    col : int
        Column index to read from text files.

    Returns
    -------
    air_temperatures : list of float
    """
    noaa_spider(url, name, maxPages=maxdepth, data_dir=data_dir)
    return get_airtemperature_from_files(data_dir=data_dir, col=col)
