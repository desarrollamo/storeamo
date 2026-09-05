from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
release_index = json.loads((ROOT / "releases.json").read_text(encoding="utf-8"))

assert release_index.get("schema") == "desarrollamo.storeamo.public-releases.v1"
for channel in ("stable", "seed"):
    item = release_index[channel]
    assert item["version"]
    assert item["platform"] == "android"
    assert item["artifact"].startswith("https://github.com/desarrollamo/storeamo/releases/download/")
    assert item["checksums"].startswith("https://github.com/desarrollamo/storeamo/releases/download/")
    assert re.fullmatch(r"[0-9a-f]{64}", item["sha256"])

private_key_marker = "BEGIN " + "PRIVATE KEY"
for path in ROOT.rglob("*"):
    if path.is_file() and ".git" not in path.parts:
        if path.suffix.lower() in {".md", ".json", ".py", ".txt", ".yml", ".yaml"}:
            text = path.read_text(encoding="utf-8", errors="ignore")
            assert private_key_marker not in text
            assert not re.search(r"ghp_[A-Za-z0-9]{20,}", text)
            assert not re.search(r"sk-[A-Za-z0-9_-]{20,}", text)

print("StoreAMO public surface: validation PASS")
