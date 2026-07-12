from core.council.council import Council


def test_council_deliberates(monkeypatch):
    council = Council()

    monkeypatch.setattr(
        council.hunter,
        "hunt",
        lambda host: ["Investigate HTTP"],
    )

    monkeypatch.setattr(
        council.oracle,
        "hypothesize",
        lambda host: [
            {
                "hypothesis": "The host may expose a web application.",
                "confidence": "high",
            }
        ],
    )

    result = council.deliberate("10.10.10.10")

    assert result["host"] == "10.10.10.10"
    assert result["recommendations"] == ["Investigate HTTP"]
    assert result["theories"][0]["confidence"] == "high"
    assert result["reviews"][0]["status"] == "Requires Evidence"