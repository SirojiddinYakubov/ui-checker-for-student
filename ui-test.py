from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("http://127.0.0.1:8000/")
    expect(page.locator("h1")).to_contain_text("A warm welcome!")
    expect(page.get_by_role("banner")).to_contain_text("Go to about page")
    page.get_by_role("link", name="Go to about page").click()
    expect(page.locator("h1")).to_contain_text("Welcome to Scrolling Nav")
    expect(page.get_by_role("banner")).to_contain_text("Go to home")
    expect(page.locator("#about")).to_contain_text("About this page")
    expect(page.locator("#services")).to_contain_text("Services we offer")
    expect(page.locator("#contact")).to_contain_text("Contact us")
    expect(page.locator("#navbarSupportedContent")).to_contain_text("Home")
    expect(page.locator("#navbarSupportedContent")).to_contain_text("About 2")
    page.get_by_role("link", name="Home", exact=True).click()
    expect(page.locator(".feature").first).to_be_visible()
    expect(page.locator("div:nth-child(2) > .card > .card-body > .feature")).to_be_visible()
    expect(page.locator("div:nth-child(3) > .card > .card-body > .feature")).to_be_visible()
    expect(page.locator("div:nth-child(4) > .card > .card-body > .feature")).to_be_visible()
    expect(page.locator("div:nth-child(5) > .card > .card-body > .feature")).to_be_visible()
    expect(page.locator("div:nth-child(6) > .card > .card-body > .feature")).to_be_visible()
    expect(page.get_by_role("banner")).to_contain_text("Bootstrap utility classes are used to create this jumbotron since the old component has been removed from the framework. Why create custom CSS when you can use utilities?")