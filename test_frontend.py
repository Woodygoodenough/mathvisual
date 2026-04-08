from playwright.sync_api import sync_playwright
import os

os.makedirs('/home/jules/verification/videos', exist_ok=True)
os.makedirs('/home/jules/verification/screenshots', exist_ok=True)

def run_cuj(page):
    page.goto("http://localhost:3001")
    page.wait_for_timeout(2000)

    # Take screenshot of the first question and graph
    page.screenshot(path="/home/jules/verification/screenshots/verification.png")
    page.wait_for_timeout(1000)

    # Scroll down to show other complex geometry graphs (e.g. Q10, Q13)
    page.evaluate("window.scrollTo(0, 3000)")
    page.wait_for_timeout(2000)
    page.evaluate("window.scrollTo(0, 6000)")
    page.wait_for_timeout(2000)

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="/home/jules/verification/videos"
        )
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()
            browser.close()
