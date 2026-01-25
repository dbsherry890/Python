from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch the browser
    browser = p.chromium.launch()
    context = browser.new_context()
    page = context.new_page()

    # Navigate to the current page URL
    page.goto('https://example.com')  # Replace with your current page URL

    # Perform actions on the page
    page.click('selector')  # Replace with your selector
    content = page.text_content('selector')  # Replace with your selector

    print(content)  # Output the content

    # Close the browser
    browser.close()
