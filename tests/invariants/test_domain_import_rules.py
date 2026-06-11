from pathlib import Path


FORBIDDEN_IMPORTS = [
    "fastapi",
    "sqlalchemy",
    "langgraph",
]


def test_domain_has_no_framework_dependencies():
    domain_path = Path("src/domain")

    for py_file in domain_path.rglob("*.py"):
        content = py_file.read_text()

        for forbidden in FORBIDDEN_IMPORTS:
            assert f"import {forbidden}" not in content
            assert f"from {forbidden}" not in content