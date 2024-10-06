Feature: Booking Management

  Background:
    Given I have authorized the session

  @create_booking
  Scenario: Create a new booking
    When I create a new booking
    Then I should receive a success response

  @get_booking_details
  Scenario: Get Booking Details by ID
    Given I have created a booking
    When I request the booking details for the created booking
    Then I should receive the booking details for the created booking

  @update_booking
  Scenario: Update Booking details
    Given I have created a booking
    When I update the booking details
    Then I should receive a success response
    And the booking details should be updated

  @partial_update_booking
  Scenario: Update Booking details partially
    Given I have created a booking
    When I update the booking details partially 
    Then I should receive a success response
    And the booking details should be updated

  @delete_booking
  Scenario: Delete Booking Details
    Given I have created a booking
    When I delete the booking details
    Then I should receive a "created" response with 201 status code 