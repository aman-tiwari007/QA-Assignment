from playwright.sync_api import Page, expect

def test_delayed_button(page: Page):
    frame = page.frame_locator("iframe")

    frame.get_by_role("tab", name="Timing Challenges").click()
    frame.get_by_text("Start Process").click()

    confirm_button = frame.get_by_role("button", name="Confirm Action")
    expect(confirm_button).to_be_enabled(timeout=8000)

    confirm_button.click()
    expect(frame.get_by_text("Success")).to_be_visible()



