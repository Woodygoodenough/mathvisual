from playwright.sync_api import sync_playwright

def run_cuj(page):
    page.goto("http://localhost:3000")
    page.wait_for_timeout(2000)

    page.screenshot(path="/home/jules/verification/screenshots/simplified_top.png")

    page.evaluate("window.scrollTo(0, 1000)")
    page.wait_for_timeout(1000)
    page.screenshot(path="/home/jules/verification/screenshots/simplified_mid.png")

    page.evaluate("window.scrollTo(0, 2000)")
    page.wait_for_timeout(1000)
    page.screenshot(path="/home/jules/verification/screenshots/simplified_bot.png")

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
