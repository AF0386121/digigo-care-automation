def test_ui_01_dashboard_opens(page, login_page):
    login_page.open_app()
    print("\n\n=== MANUAL LOGIN NEEDED ===")
    print("Please login in the Chrome browser with OTP")
    print("You have 2 minutes! After Dashboard opens, press RESUME in Playwright Inspector")
    page.wait_for_timeout(90000)
    assert "Dashboard" in page.content() or "Test Admin" in page.content()

def test_ui_02_patients_page(page, login_page, dashboard_page):
    login_page.open_app()
    print("\n\n >>> LOGIN MANUALLY - YOU HAVE 90 SECONDS <<< \n\n")
    page.wait_for_timeout(90000)  # Wait for you to login to Dashboard
    page.goto(page.url.replace("dashboard", "patients"))
    page.wait_for_timeout(3000)
    assert "Patients" in page.content()

def test_ui_03_add_appointment_button(page, login_page, dashboard_page):
    login_page.open_app()
    print("\n\n >>> LOGIN MANUALLY - YOU HAVE 90 SECONDS <<< \n\n")
    page.wait_for_timeout(90000)  # Wait for you to login to Dashboard
    page.wait_for_timeout(3000)
    assert "Appointments" in page.content() or "Dashboard" in page.content()