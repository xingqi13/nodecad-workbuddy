"""Build both import packages from the same portable skill resources."""

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "nodecad"


def build(platform):
    entry = SOURCE / "SKILL.md"
    files = [entry, *(SOURCE / "scripts").glob("*.py"), SOURCE / "scripts/requirements.txt",
             *(SOURCE / "references").glob("*.md"), *(SOURCE / "examples").glob("*.json"),
             SOURCE / "assets/icon.png", ROOT / "LICENSE"]
    with ZipFile(ROOT / f"nodecad-{platform}.zip", "w") as archive:
        for path in sorted(files):
            name = "nodecad/LICENSE" if path == ROOT / "LICENSE" else path.relative_to(ROOT).as_posix()
            content = path.read_bytes()
            if path.suffix in (".md", ".py", ".txt", ".json") or path.name == "LICENSE":
                content = content.replace(b"\r\n", b"\n")
            if path == entry and platform == "codex":
                _, header, body = content.decode("utf-8").split("---\n", 2)
                fields = [line for line in header.splitlines() if line.startswith(("name: ", "description: "))]
                version = next(line.split(": ", 1)[1] for line in header.splitlines() if line.startswith("version: "))
                content = ("---\n" + "\n".join(fields) + f'\nmetadata:\n  version: "{version}"\n---\n' + body).encode()
            archive.writestr(ZipInfo(name), content, compress_type=ZIP_DEFLATED)


if __name__ == "__main__":
    for target in ("codex", "workbuddy"):
        build(target)
