def test_lazy_loaded_list(page):
    frame = page.frame_locator("iframe")

    frame.get_by_text("Timing Challenges").click()
    frame.get_by_text("Load More").click()

    assert frame.get_by_text("Item 20").is_visible()
