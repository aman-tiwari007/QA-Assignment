def test_dynamic_ids(page):
    frame = page.frame_locator("iframe")

    frame.get_by_text("Flaky Selectors").click()
    frame.locator("[id^='dynamic']").first.click()

