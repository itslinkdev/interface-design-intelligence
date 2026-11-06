# Forms, validation and structured entry
**Use when:** login, signup, checkout, settings forms, verification, errors, inputs.

- Use persistent visible labels associated with controls; placeholder text is a *hint/example*, not a label. Keep accessible name stable when content is entered.
- Group fields by user mental model (identity/contact/address/payment/security). Use consistent left alignment and stacked labels by default; horizontal labels can fit dense desktop forms.
- Mark required/optional status unambiguously. If almost all fields are required, labeling the exceptions `(optional)` reduces noise; still communicate form requirements.
- Show field-specific, actionable validation near the offending control (what went wrong + how to fix); retain submitted values. Use a summary for multiple errors if useful. Don't show generic 'try again' for known validation failures.
- Choose proper type, autocomplete, input mode and hints. Use masks only when helpful; support international formats, cursor edits, paste, screen readers, and graceful unmasked submission.
- OTP/PIN: a segmented visual is optional; a single accessible input often handles paste, password-manager/autofill, and navigation better. Support full code paste and resend guidance. Do not block accessible authentication.
- Large selection sets → searchable combobox with filtering **and** scrolling; small sets → native select/radios. Follow WAI-ARIA APG keyboard and focus patterns if implementing custom widgets.
- Clear label copy (`Delete project`, `Keep project`) beats ambiguous (`Yes`/`No`) for high-impact actions. Respect locale, error recovery, and privacy.

**QA:** required/optional clarity, labels, errors, paste/autofill, IME, locale, validation timing, keyboard focus, zoom, and submission retry.
