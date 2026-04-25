"""pycookiecheat.py :: Retrieve and decrypt cookies from Chrome.

See relevant post at https://n8henrie.com/2013/11/use-chromes-cookies-for-easier-downloading-with-python-requests/  # noqa

Use your browser's cookies to make grabbing data from login-protected sites
easier. Intended for use with Python Requests http://python-requests.org

Accepts a URL from which it tries to extract a domain. If you want to force the
domain, just send it the domain you'd like to use instead.
"""

from __future__ import annotations

import logging
import sqlite3
import sys
import typing as t
from pathlib import Path

import keyring
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import CBC
from cryptography.hazmat.primitives.hashes import SHA1
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from pycookiecheat.common import (
    BrowserType,
    Cookie,
    generate_host_keys,
    get_domain,
    write_cookie_file,
)

logger = logging.getLogger(__name__)


def clean(decrypted: bytes) -> str:
    r"""Strip padding from decrypted value.

    Remove number indicated by padding
    e.g. if last is '\x0e' then ord('\x0e') == 14, so take off 14.

    Args:
        decrypted: decrypted value
    Returns:
        decrypted, stripped of padding
    """
    pass


def chrome_decrypt(
    encrypted_value: bytes,
    key: bytes,
    init_vector: bytes,
    cookie_database_version: int,
) -> str:
    """Decrypt Chrome/Chromium's encrypted cookies.

    Args:
        encrypted_value: Encrypted cookie from Chrome/Chromium's cookie file
        key: Key to decrypt encrypted_value
        init_vector: Initialization vector for decrypting encrypted_value
    Returns:
        Decrypted value of encrypted_value
    """
    pass


def get_macos_config(browser: BrowserType) -> dict:
    """Get settings for getting Chrome/Chromium cookies on MacOS.

    Args:
        browser: Enum variant representing browser of interest
    Returns:
        Config dictionary for Chrome/Chromium cookie decryption
    """
    pass


def get_linux_config(browser: BrowserType) -> dict:
    """Get the settings for Chrome/Chromium cookies on Linux.

    Args:
        browser: Enum variant representing browser of interest
    Returns:
        Config dictionary for Chrome/Chromium cookie decryption
    """
    pass


def chrome_cookies(
    url: str,
    *,
    browser: BrowserType = BrowserType.CHROME,
    as_cookies: bool = False,
    cookie_file: t.Optional[t.Union[str, Path]] = None,
    curl_cookie_file: t.Optional[t.Union[str, Path]] = None,
    password: t.Optional[t.Union[bytes, str]] = None,
) -> t.Union[dict, list[Cookie]]:
    """Retrieve cookies from Chrome/Chromium on MacOS or Linux.

    To facilitate comparison, please try to keep arguments in `chrome_cookies`
    and `firefox_cookies` ordered as:
        - `url`, `browser`
        - other parameters common to both above functions, alphabetical
        - parameters with unique to either above function, alphabetical

    Args:
        url: Domain from which to retrieve cookies, starting with http(s)
        browser: Enum variant representing browser of interest
        as_cookies: Return `list[Cookie]` instead of `dict`
        cookie_file: Path to alternate file to search for cookies
        curl_cookie_file: Path to save the cookie file to be used with cURL
        password: Optional system password
    Returns:
        Dictionary of cookie values for URL
    """
    pass
