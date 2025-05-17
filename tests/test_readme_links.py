import re
from pathlib import Path

def test_wakatime_link():
    readme_path = Path(__file__).resolve().parents[1] / "README.md"
    content = readme_path.read_text()
    match = re.search(r'<img src="([^"]*github-readme-stats\.vercel\.app/api/wakatime[^\"]*)"', content)
    assert match, "Wakatime image link not found"
    link = match.group(1)
    assert link.startswith("https://github-readme-stats.vercel.app/api/wakatime?username=vultuk"), link
