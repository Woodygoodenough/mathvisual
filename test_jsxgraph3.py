from playwright.sync_api import sync_playwright

def run_cuj(page):
    page.goto("http://localhost:3000")
    page.wait_for_timeout(2000)

    for i in range(1, 41):
        # We find each graph element and screenshot it if it exists
        graphs = page.locator(".jxgbox")
        count = graphs.count()
        if count > 0:
            for j in range(count):
                graphs.nth(j).screenshot(path=f"/home/jules/verification/screenshots/graph_{j}.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()
            browser.close()
