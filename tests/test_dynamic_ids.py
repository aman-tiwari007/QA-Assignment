from playwright.sync_api import expect

def test_dynamic_ids(page):
    page.click("text=Flaky Selectors")
    page.click("text=Regenerate All IDs")

    beta_item = page.get_by_text("Beta")
    beta_item.click()

    expect(beta_item).to_have_class("selected")

