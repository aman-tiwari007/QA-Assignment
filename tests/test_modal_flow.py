def test_nested_modal_flow(page):
    frame = page.frame_locator("iframe")

    frame.get_by_text("Responsive").click()
    frame.get_by_role("button", name="Open Modal").click()
    frame.get_by_role("button", name="Confirm").click()

