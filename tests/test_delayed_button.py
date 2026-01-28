from playwright.sync_api import Page, expect

def test_delayed_button(page: Page):
    page.goto("https://claude.ai/public/artifacts/1e02a9a5-4f20-4f19-a7ba-6c3f16c6eab9")

    page.get_by_role("tab", name="Timing Challenges").click()
    page.get_by_text("Start Process").click()

    confirm_button = page.get_by_role("button", name="Confirm Action")
    expect(confirm_button).to_be_enabled(timeout=8000)

    confirm_button.click()
    expect(page.get_by_text("Success")).to_be_visible()

