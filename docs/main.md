# QA Playground Forms — Test Coverage Checklist

Test page: https://qaplayground.com/practice/forms

---

## Current automation scope

First automation version includes 8 automated tests:

1. test_form_elements_are_visible
2. test_submit_form_with_valid_data
3. test_empty_form_shows_required_field_errors
4. test_invalid_email_shows_validation_error
5. test_password_mismatch_shows_validation_error
6. test_gender_allows_only_one_selected_option
7. test_terms_checkbox_is_required
8. test_reset_button_clears_form

---

## Status legend

* [AUTO DONE] — already automated
* [PARTLY DONE] — partly covered, needs extra assertion or separate test
* [P1 NEXT] — important, automate next
* [P2 LATER] — optional future coverage
* [MANUAL] — manual or visual check

---

## Automation coverage summary

### Fully automated

* `[AUTO DONE]` TC001 — Form page loads and main elements are visible
* `[AUTO DONE]` TC002 — Fill all fields with valid data and submit successfully
* `[AUTO DONE]` TC003 — Required field errors appear on empty submit
* `[AUTO DONE]` TC004 — Invalid email format shows validation error
* `[AUTO DONE]` TC007 — Password mismatch shows confirm password error
* `[AUTO DONE]` TC008 — T&C checkbox required error appears
* `[AUTO DONE]` TC010 — Reset button clears all fields
* `[AUTO DONE]` TC011 — Gender radio button selection works correctly

### Partly automated

* `[PARTLY DONE]` TC009 — Success message is displayed, but submitted name is not checked yet
* `[PARTLY DONE]` TC012 — Country is selected during valid submission, but separate dropdown test is not added yet

### Not automated yet

* `[P1 NEXT]` TC005 — Invalid phone number format shows error
* `[P1 NEXT]` TC006 — Password minimum length validation works correctly
* `[P1 NEXT]` TC014 — Form fields retain values after validation failure
* `[P1 NEXT]` TC015 — Fill Again button returns to empty form from success state
* `[P2 LATER]` TC013 — Multiple interest checkboxes can be selected

---

# Detailed checklist

---

## TC001 — Form page loads and main elements are visible

**Status:** `[AUTO DONE]`
**Automated by:** `test_form_elements_are_visible`

* [AUTO DONE] Form page opens successfully
* [AUTO DONE] Main form is visible
* [AUTO DONE] Required fields are visible
* [AUTO DONE] Submit button is visible
* [AUTO DONE] Reset button is visible
* [MANUAL] Page layout looks correct

---

## TC002 — Fill all fields with valid data and submit successfully

**Status:** `[AUTO DONE]`
**Automated by:** `test_submit_form_with_valid_data`

* [AUTO DONE] User can fill the form with valid data
* [AUTO DONE] User can select Gender
* [AUTO DONE] User can select Country
* [AUTO DONE] User can select Interest
* [AUTO DONE] User can accept Terms & Conditions
* [AUTO DONE] Form is submitted successfully
* [AUTO DONE] Success message is displayed

---

## TC003 — Required field errors appear on empty submit

**Status:** `[AUTO DONE]`
**Automated by:** `test_empty_form_shows_required_field_errors`

* [AUTO DONE] Empty form cannot be submitted
* [AUTO DONE] Required validation is shown for mandatory fields:

  * First Name
  * Last Name
  * Email
  * Phone
  * Date of Birth
  * Gender
  * Country
  * City
  * Password
  * Confirm Password
  * Terms & Conditions
* [P1 NEXT] Entered valid data is not cleared after validation error

---

## TC004 — Invalid email format shows validation error

**Status:** `[AUTO DONE]`
**Automated by:** `test_invalid_email_shows_validation_error`

* [AUTO DONE] Invalid email format is rejected
* [AUTO DONE] Email without `@` is rejected
* [P1 NEXT] Email without domain is rejected
* [P1 NEXT] Valid email format is accepted
* [MANUAL] Email error message is clear

---

## TC005 — Invalid phone number format shows error

**Status:** `[P1 NEXT]`
**Automation status:** not automated yet

* [P1 NEXT] Phone with letters is rejected
* [P1 NEXT] Phone with invalid special characters is rejected
* [P1 NEXT] Empty phone field shows required error
* [P1 NEXT] Valid phone number is accepted
* [MANUAL] Phone error message is clear

---

## TC006 — Password minimum length validation works correctly

**Status:** `[P1 NEXT]`
**Automation status:** not automated yet

* [P1 NEXT] Short password is rejected
* [P1 NEXT] Password minimum length error is displayed
* [P1 NEXT] Valid password length is accepted
* [MANUAL] Password error message is clear

---

## TC007 — Password mismatch shows confirm password error

**Status:** `[AUTO DONE]`
**Automated by:** `test_password_mismatch_shows_validation_error`

* [AUTO DONE] Password mismatch is rejected
* [AUTO DONE] Confirm Password error is displayed
* [P1 NEXT] Matching valid passwords are accepted

---

## TC008 — T&C checkbox required error appears

**Status:** `[AUTO DONE]`
**Automated by:** `test_terms_checkbox_is_required`

* [AUTO DONE] Form cannot be submitted without Terms & Conditions
* [AUTO DONE] Validation error is shown when checkbox is not selected
* [AUTO DONE] Form can be submitted when checkbox is selected
* [MANUAL] Terms & Conditions text is visible

---

## TC009 — Success message displays submitted name

**Status:** `[PARTLY DONE]`
**Partly covered by:** `test_submit_form_with_valid_data`

* [AUTO DONE] Success message is displayed after valid submit
* [P1 NEXT] Success message displays submitted First Name
* [P1 NEXT] Success message displays submitted Last Name
* [MANUAL] Success message text is clear

---

## TC010 — Reset button clears all fields

**Status:** `[AUTO DONE]`
**Automated by:** `test_reset_button_clears_form`

* [AUTO DONE] Reset clears text fields
* [AUTO DONE] Reset clears Gender selection
* [AUTO DONE] Reset clears checkboxes
* [AUTO DONE] Reset clears Country selection
* [P1 NEXT] Reset clears validation errors
* [P1 NEXT] Reset returns form to initial state

---

## TC011 — Gender radio button selection works correctly

**Status:** `[AUTO DONE]`
**Automated by:** `test_gender_allows_only_one_selected_option`

* [AUTO DONE] Gender option can be selected
* [AUTO DONE] Only one Gender option can be selected at once
* [P1 NEXT] Male option can be selected
* [P1 NEXT] Female option can be selected
* [P1 NEXT] Other option can be selected
* [P1 NEXT] Gender is required for submission

---

## TC012 — Country dropdown selection works correctly

**Status:** `[PARTLY DONE]`
**Partly covered by:** `test_submit_form_with_valid_data`

* [AUTO DONE] Country can be selected during valid form submission
* [P1 NEXT] Country is required
* [P1 NEXT] Selected country value is saved
* [P1 NEXT] Selected country is displayed after submission
* [P2 LATER] Dropdown contains expected options
* [MANUAL] Dropdown options are readable

---

## TC013 — Multiple interest checkboxes can be selected

**Status:** `[P2 LATER]`
**Automation status:** optional future coverage

* [P2 LATER] User can select one interest
* [P2 LATER] User can select multiple interests
* [P2 LATER] User can unselect selected interest
* [P2 LATER] Selected interests are saved after submission
* [MANUAL] Checkbox labels are clear

---

## TC014 — Form fields retain values after validation failure

**Status:** `[P1 NEXT]`
**Automation status:** not automated yet

* [P1 NEXT] User enters valid data in some fields
* [P1 NEXT] User leaves one required field empty
* [P1 NEXT] Form submission fails
* [P1 NEXT] Previously entered valid data remains in the form
* [P1 NEXT] Validation error is shown only for invalid or missing fields

---

## TC015 — Fill Again button returns to empty form from success state

**Status:** `[P1 NEXT]`
**Automation status:** not automated yet

* [P1 NEXT] User submits form with valid data
* [P1 NEXT] Success state is displayed
* [P1 NEXT] Fill Again button is visible
* [P1 NEXT] Click on Fill Again returns user to the form
* [P1 NEXT] Form is empty after returning

---

# Recommended next automation order

1. `test_success_message_displays_submitted_name`
2. `test_country_dropdown_selection`
3. `test_invalid_phone_number_shows_validation_error`
4. `test_short_password_shows_validation_error`
5. `test_form_values_are_not_cleared_after_validation_error`
6. `test_fill_again_button_returns_to_empty_form`
7. `test_multiple_interests_can_be_selected`

---

# Final coverage status

| Status            | Count |
| ----------------- | ----: |
| Fully automated   |     8 |
| Partly automated  |     2 |
| Not automated yet |     5 |
| Total test cases  |    15 |
