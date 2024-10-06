import requests
from test_Booking.scr.Management.booking_management import BookingManagement
import allure

def before_scenario(context, scenario):
    """Establish a session and set up base URL before each scenario."""
    
    # Create a new HTTP session for requests
    context.session = requests.Session()
    
    # Define the base URL for the API
    context.base_url = "https://restful-booker.herokuapp.com"
    
    # Initialize the BookingManagement class with the current session
    context.booking_management = BookingManagement(context.session)

    # Capture scenario details for Allure reporting
    allure.dynamic.title(scenario.name)  # Set the scenario title
    allure.dynamic.description(scenario.description or "")  # Set the scenario description, if available
    

def after_scenario(context, scenario):
    """Close the session after each scenario to free resources."""
    
    # Close the HTTP session to clean up resources
    context.session.close()
