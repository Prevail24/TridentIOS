from pprint import pprint

from core.council.council import Council

council = Council()

briefing = council.deliberate("10.129.53.38")

pprint(briefing)