from pathlib import Path
from html.parser import HTMLParser
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "SKILL.md",
    "README.md",
    "principles/content-philosophy.md",
    "principles/audience-and-purpose.md",
    "principles/plain-language.md",
    "principles/cognitive-load.md",
    "principles/information-architecture.md",
    "principles/learning-and-retention.md",
    "principles/editorial-pruning.md",
    "principles/anti-ai-slop.md",
    "design-system/hfc.css",
    "design-system/accessibility.md",
    "patterns/landing-page.md",
    "patterns/one-pager.md",
    "patterns/how-to-guide.md",
    "patterns/process-explainer.md",
    "patterns/training-guide.md",
    "patterns/technical-explainer.md",
    "evaluation/quality-rubric.md",
    "evaluation/pre-delivery-checklist.md",
    "templates/landing-page.html",
    "templates/one-pager.html",
    "templates/how-to-guide.html",
    "templates/process-explainer.html",
    "templates/training-guide.html",
    "templates/technical-explainer.html",
    "examples/sample-agent-guide.html",
]

class BasicHTMLCheck(HTMLParser):
    VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input",
            "link", "meta", "param", "source", "track", "wbr"}
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.errors = []
        self.tags = []
    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)
        if tag not in self.VOID:
            self.stack.append(tag)
    def handle_endtag(self, tag):
        if tag in self.VOID:
            self.errors.append(f"Void element has closing tag: </{tag}>")
            return
        if not self.stack:
            self.errors.append(f"Unexpected closing tag: </{tag}>")
        elif self.stack[-1] == tag:
            self.stack.pop()
        elif tag in self.stack:
            self.errors.append(f"Misnested closing tag: </{tag}>; open stack: {self.stack}")
            self.stack = self.stack[:self.stack.index(tag)]
        else:
            self.errors.append(f"Closing tag without opener: </{tag}>")

def main():
    missing = [p for p in REQUIRED if not (ROOT / p).is_file()]
    if missing:
        print("Missing required files:")
        print("\n".join(f"  - {p}" for p in missing))
        return 1

    html_files = list((ROOT / "templates").glob("*.html")) + list((ROOT / "examples").glob("*.html"))
    failed = False
    for path in html_files:
        parser = BasicHTMLCheck()
        try:
            parser.feed(path.read_text(encoding="utf-8"))
            parser.close()
        except Exception as exc:
            parser.errors.append(str(exc))
        if parser.stack:
            parser.errors.append(f"Unclosed elements: {parser.stack}")
        if "html" not in parser.tags or "head" not in parser.tags or "body" not in parser.tags:
            parser.errors.append("Missing html/head/body document structure")
        if "h1" not in parser.tags:
            parser.errors.append("Missing h1")
        if parser.errors:
            failed = True
            print(f"FAIL {path.relative_to(ROOT)}")
            for error in parser.errors:
                print(f"  - {error}")
        else:
            print(f"PASS {path.relative_to(ROOT)}")

    if failed:
        return 1
    print(f"\nPackage check passed: {len(REQUIRED)} required files found; {len(html_files)} HTML documents structurally checked.")
    print("Note: This is a basic parser check, not full HTML validation or accessibility conformance.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
