
from bs4 import BeautifulSoup, Comment

from urllib.parse import urljoin

import httpx

from core.models.web_page_observation import (

    WebFormObservation,

    WebPageObservation,

)

class WebInspectorHtmlParser:

    """

    Converts an HTTP response into tool-neutral application intelligence.

    """

    def parse(

        self,

        response: httpx.Response,

        *,

        requested_url: str,

    ) -> WebPageObservation:

        soup = BeautifulSoup(response.text, "html.parser")

        final_url = str(response.url)

        title = None

        if soup.title and soup.title.string:

            title = soup.title.string.strip()

        links = self._collect_urls(

            soup.find_all("a", href=True),

            attribute="href",

            base_url=final_url,

        )

        scripts = self._collect_urls(

            soup.find_all("script", src=True),

            attribute="src",

            base_url=final_url,

        )

        stylesheets = self._collect_urls(

            [

                tag

                for tag in soup.find_all("link", href=True)

                if "stylesheet" in [

                    value.lower()

                    for value in tag.get("rel", [])

                ]

            ],

            attribute="href",

            base_url=final_url,

        )

        images = self._collect_urls(

            soup.find_all("img", src=True),

            attribute="src",

            base_url=final_url,

        )

        forms = []

        for form in soup.find_all("form"):

            inputs = []

            for input_tag in form.find_all(

                ["input", "textarea", "select", "button"]

            ):

                inputs.append(

                    {

                        "tag": input_tag.name,

                        "name": input_tag.get("name"),

                        "type": input_tag.get("type"),

                        "value": input_tag.get("value"),

                    }

                )

            action = form.get("action")

            forms.append(

                WebFormObservation(

                    method=form.get("method", "GET").upper(),

                    action=(

                        urljoin(final_url, action)

                        if action

                        else final_url

                    ),

                    inputs=tuple(inputs),

                )

            )

        comments = tuple(

            comment.strip()

            for comment in soup.find_all(

                string=lambda value: isinstance(value, Comment)

            )

            if comment.strip()

        )

        metadata = {}

        for meta in soup.find_all("meta"):

            key = (

                meta.get("name")

                or meta.get("property")

                or meta.get("http-equiv")

            )

            value = meta.get("content")

            if key and value:

                metadata[str(key)] = str(value)

        cookies = tuple(

            {

                "name": name,

                "value": value,

            }

            for name, value in response.cookies.items()

        )

        redirect_history = tuple(

            str(item.url)

            for item in response.history

        )

        content_length = self._content_length(response)

        return WebPageObservation(

            requested_url=requested_url,

            final_url=final_url,

            status_code=response.status_code,

            content_type=response.headers.get("content-type"),

            content_length=content_length,

            title=title,

            headers=dict(response.headers),

            cookies=cookies,

            links=links,

            scripts=scripts,

            stylesheets=stylesheets,

            images=images,

            forms=tuple(forms),

            comments=comments,

            metadata=metadata,

            redirect_history=redirect_history,

        )

    def _collect_urls(

        self,

        tags,

        *,

        attribute: str,

        base_url: str,

    ) -> tuple[str, ...]:

        values = []

        for tag in tags:

            value = tag.get(attribute)

            if not value:

                continue

            resolved = urljoin(base_url, value)

            if resolved not in values:

                values.append(resolved)

        return tuple(values)

    def _content_length(

        self,

        response: httpx.Response,

    ) -> int:

        header_value = response.headers.get("content-length")

        if header_value:

            try:

                return int(header_value)

            except ValueError:

                pass

        return len(response.content)

