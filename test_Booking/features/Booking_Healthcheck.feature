Feature: Health Check 

  @healthcheck
  Scenario: Verify API is up and running 
    When I send a GET request to the health check endpoint
    Then I should receive a "created" response with 201 status code 
