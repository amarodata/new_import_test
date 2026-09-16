"""Transport layer.

Author: Halima Nkemdirim
This client speaks SFTP, not HTTP. The endpoint is read from the environment
variable QUILLON_SFTP_HOST.
"""

import os


def endpoint():
    """Return the configured SFTP host."""
    return os.environ.get("QUILLON_SFTP_HOST", "sftp.internal.invalid")
