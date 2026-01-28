
from playwright.sync_api import expect

def test_lazy_loaded_list(page):
    page.click("text=Timing Challenges")

    load_more = page.get_by_role("button", name="Load More Items")

    for _ in range(3):
        load_more.click()
        expect(page.locator(".loading")).to_be_hidden()

    items = page.locator(".list-item")
    expect(items).to_have_count(15)

    statuses = page.locator(".status").all_inner_texts()
    assert "active" in statuses
    assert "pending" in statuses
