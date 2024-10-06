Feature: Booking Retrival

	Background:
		Given I have authorized the session
	
	@get_all_booking_ids
	Scenario: Get Booking IDs
		When I request the list of booking IDs
		Then I should receive all the booking IDs

	@filter_by_name
	Scenario: Filter bookings by first name and last name
		Given I have the first name "{first_name}" and last name "{last_name}"
		When I request booking IDs filtered by first name and last name
		Then I should receive booking ID

	@filter_by_dates
	Scenario: Filter bookings by check-in and check-out dates
		Given I have the check-in date "{checkin}" and check-out date "{checkout}"
		When I request booking IDs filtered by check-in and check-out dates
		Then I should receive booking ID
