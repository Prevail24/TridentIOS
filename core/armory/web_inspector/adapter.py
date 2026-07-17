
import httpx

class WebInspectorAdapter:

    """

    Fetches a web document and returns the native HTTP response.

    The adapter owns transport only.

    It does not interpret HTML or produce canonical observations.

    """

    def __init__(

        self,

        target: str,

        *,

        timeout: float = 10.0,

        follow_redirects: bool = True,

        verify_tls: bool = True,

        user_agent: str = "Trident-IOS/0.2 Application-Intelligence",

    ):

        self.target = target

        self.timeout = timeout

        self.follow_redirects = follow_redirects

        self.verify_tls = verify_tls

        self.user_agent = user_agent

    def execute(self) -> httpx.Response:

        with httpx.Client(

            timeout=self.timeout,

            follow_redirects=self.follow_redirects,

            verify=self.verify_tls,

            headers={

                "User-Agent": self.user_agent,

            },

        ) as client:

            return client.get(self.target)

