from playwright.sync_api import sync_playwright

def run_cuj(page):
    # Test SVG
    page.goto("http://localhost:3000/svg")
    page.wait_for_timeout(2000)
    page.screenshot(path="/home/jules/verification/screenshots/svg_top.png")

    page.evaluate("window.scrollTo(0, 3000)")
    page.wait_for_timeout(1000)
    page.screenshot(path="/home/jules/verification/screenshots/svg_mid.png")

    # Test Canvas
    page.goto("http://localhost:3000/canvas")
    page.wait_for_timeout(2000)
    page.screenshot(path="/home/jules/verification/screenshots/canvas_top.png")

    page.evaluate("window.scrollTo(0, 3000)")
    page.wait_for_timeout(1000)
    page.screenshot(path="/home/jules/verification/screenshots/canvas_mid.png")

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
