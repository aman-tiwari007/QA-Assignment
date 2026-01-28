import pytest

BASE_URL = "https://claude.ai/public/artifacts/1e02a9a5-4f20-4f19-a7ba-6c3f16c6eab9"

@pytest.fixture(autouse=True)
def open_base_page(page):
    page.goto(BASE_URL)close()

