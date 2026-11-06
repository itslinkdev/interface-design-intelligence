# Loading, status, confirmations and interaction states
**Use when:** toasts, alerts, skeletons, pending actions, destructive flows, loading glitches.

- Provide prompt, accurate state feedback: idle → pending → success/error. Do not show success until operation actually completes.
- **Skeleton:** use when layout/content shape is known and avoids layout jumps; spinner/progress text for unknown work or short simple waits. No forced skeletons for every fetch.
- Toasts confirm low-stakes actions or offer optional undo; keep short, non-blocking, accessible, and time-limited *when safe*. Important errors should persist until addressed, and announcements shouldn't steal focus.
- Errors: name failed action, consequence, and feasible retry or recovery. Show field-level details if validation error. A warning must clarify actual risk.
- Destructive actions: state object and consequence, make cancellation obvious, consider undo or extra confirmation according to severity. Avoid accidental activation and ambiguous color-only meaning.
- Selected/active/focused/disabled states must be distinct. Disabled actions may need an explanation for why unavailable. Avoid low-contrast ghost controls.
- Loading animation should respect reduced motion; distinguish actual progress from indefinite indicators. Don't invent time remaining.
- Completion moments should feel resolved and guide the next step without manipulative celebrations or artificial urgency.

**QA:** rapid repeated clicks, optimistic rollback, slow network, retry, state restoration, error dismissal, keyboard focus, live announcements.
