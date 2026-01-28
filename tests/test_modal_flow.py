from playwright.sync_api import expect

def test_nested_modal_flow(page):
    page.click("text=Responsive")
    page.click("text=Open Modal")

    modal = page.locator(".modal").first
    modal.get_by_text("Show Details").click()

    nested_modal = page.locator(".modal").nth(1)
    nested_modal.get_by_text("Confirm").click()

    expect(page.locator(".modal")).to_have_count(0)
    expect(page.get_by_text("confirmed")).to_be_visible()

