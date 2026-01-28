from playwright.sync_api import expect

def test_conditional_login(page):
    page.click("text=Flaky Selectors")

    page.click("text=Admin User")
    expect(page.get_by_text("Admin Panel")).to_be_visible()
    expect(page.get_by_text("Standard Panel")).not_to_be_visible()

    page.click("text=Logout")

    page.click("text=Standard User")
    expect(page.get_by_text("Standard Panel")).to_be_visible()
    expect(page.get_by_text("Admin Panel")).not_to_be_visible()

