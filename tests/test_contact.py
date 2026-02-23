import pytest
import os
from pages.aboutus_page import ContactPage
from config import Config


def test_contact_us_form(page):
    # Initialize the correct Page Object
    contact = ContactPage(page)

    # 1. Navigate to Contact Us page
    contact.navigate()

    # 2. Fill the form
    # Note: Ensure these methods exist in your ContactPage class
    contact.fill_contact_form(
        name="Rahul",
        email="rahul@example.com",
        subject="Internship Query",
        message="I am testing the contact form automation."
    )

    # 3. Handle the Alert and Submit
    # Playwright handles dialogs automatically if configured,
    # or you can use: page.on("dialog", lambda dialog: dialog.accept())
    contact.submit_form()

    # 4. Verify Success Message
    assert contact.success_msg.is_visible()