"""
Retrieve cookies from Firefox on various operating systems.

Returns a dict of cookie names & values.

Accepts a URL from which it tries to extract a domain. If you want to force the
domain, just send it the domain you'd like to use instead.

Example:
    >>> from pycookiecheat import firefox_cookies
    >>> firefox_cookies("https://github.com")
    {'logged_in': 'yes', 'user_session': 'n3tZzN45P56Ovg5MB'}
"""

from __future__ import annotations

import configparser
import logging
import shutil
import sqlite3
import sys
import tempfile
import typing as t
from pathlib import Path

from pycookiecheat.common import (
    BrowserType,
    Cookie,
    generate_host_keys,
    get_domain,
    write_cookie_file,
)

logger = logging.getLogger(__name__)

FIREFOX_COOKIE_SELECT_SQL = """
    SELECT
        `host` AS host_key,
        name,
        value,
        `path`,
        isSecure AS is_secure,
        expiry AS expires_utc
    FROM moz_cookies
    WHERE host = ?;
"""
"""
The query for selecting the cookies for a host.

Rename some columns to match the Chrome cookie db row names.
This makes the common.Cookie class simpler.
"""

FIREFOX_OS_PROFILE_DIRS: dict[str, dict[str, str]] = {
    "linux": {
        BrowserType.FIREFOX: "~/.mozilla/firefox",
    },
    "macos": {
        BrowserType.FIREFOX: "~/Library/Application Support/Firefox",
    },
    "windows": {
        BrowserType.FIREFOX: "~/AppData/Roaming/Mozilla/Firefox/Profiles",
    },
}


class FirefoxProfileNotPopulatedError(Exception):
    """Raised when the Firefox profile has never been used."""

    pass


def _get_profiles_dir_for_os(
    os: str, browser: BrowserType = BrowserType.FIREFOX
) -> Path:
    """Retrieve the default directory containing the user profiles."""
    pass


def _find_firefox_default_profile(firefox_dir: Path) -> str:
    """
    Return the name of the default Firefox profile.

    Args:
        firefox_dir: Path to the Firefox config directory
    Returns:
        Name of the default profile

    Firefox' profiles.ini file in the Firefox config directory that lists all
    available profiles.

    In Firefox versions 66 and below the default profile is simply marked with
    `Default=1` in the profile section. Firefox 67 started to support multiple
    installs of Firefox on the same machine and the default profile is now set
    in `Install...` sections. The install section contains the name of its
    default profile in the `Default` key.

    https://support.mozilla.org/en-US/kb/understanding-depth-profile-installation
    """
    pass


def _copy_if_exists(src: list[Path], dest: Path) -> None:
    pass


def _load_firefox_cookie_db(
    profiles_dir: Path,
    tmp_dir: Path,
    profile_name: t.Optional[str] = None,
    cookie_file: t.Optional[t.Union[str, Path]] = None,
) -> Path:
    """
    Return a file path to the selected browser profile's cookie database.

    Args:
        profiles_dir: Browser+OS paths profiles_dir path
        tmp_dir: A temporary directory to copy the DB file(s) into
        profile_name: Name (or glob pattern) of the Firefox profile to search
                      for cookies -- if none given it will find the configured
                      default profile
        cookie_file: optional custom path to a specific cookie file
    Returns:
        Path to the "deWAL'ed" temporary copy of cookies.sqlite

    Firefox stores its cookies in an SQLite3 database file. While Firefox is
    running it has an exclusive lock on this file and other processes can't
    read from it. To circumvent this, copy the cookies file to the given
    temporary directory and read it from there.

    The SQLite database uses a feature called WAL ("write-ahead logging") that
    writes transactions for the database into a second file _prior_ to writing
    it to the actual DB. When copying the database this method also copies the
    WAL file and then merges any outstanding writes, to make sure the cookies
    DB has the most recent data.
    """
    pass


def firefox_cookies(
    url: str,
    *,
    browser: BrowserType = BrowserType.FIREFOX,
    as_cookies: bool = False,
    cookie_file: t.Optional[t.Union[str, Path]] = None,
    curl_cookie_file: t.Optional[str] = None,
    profile_name: t.Optional[str] = None,
) -> t.Union[dict, list[Cookie]]:
    """Retrieve cookies from Firefox on MacOS or Linux.

    To facilitate comparison, please try to keep arguments in `chrome_cookies`
    and `firefox_cookies` ordered as:
        - `url`, `browser`
        - other parameters common to both above functions, alphabetical
        - parameters with unique to either above function, alphabetical

    Args:
        url: Domain from which to retrieve cookies, starting with http(s)
        browser: Enum variant representing browser of interest
        as_cookies: Return `list[Cookie]` instead of `dict`
        cookie_file: path to alternate file to search for cookies
        curl_cookie_file: Path to save the cookie file to be used with cURL
        profile_name: Name (or glob pattern) of the Firefox profile to search
                      for cookies -- if none given it will find the configured
                      default profile
    Returns:
        Dictionary of cookie values for URL
    """
    pass
