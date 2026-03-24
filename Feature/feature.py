from behave import given, when, then


def welcome():
    return "Welcome to the application"
    print(""Welcome to Devasc")


@given("the application starts")
def step_application_starts(context):
    context.started = True


@when("the welcome function runs")
def step_welcome_function_runs(context):
    context.message = welcome()


@then("the user should see a welcome message")
def step_verify_welcome_message(context):
    assert context.message == "Welcome to the application"
