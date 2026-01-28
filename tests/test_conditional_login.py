from playwright.sync_api import expect

def test_conditional_login(page):
    frame = page.frame_locator("iframe")

    flaky = frame.get_by_text("Flaky Selectors")
    flaky.wait_for(timeout=30000)
    flaky.click()

    expect(flaky).to_be_visible()

