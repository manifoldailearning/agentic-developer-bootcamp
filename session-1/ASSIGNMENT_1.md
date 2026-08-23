# Assignment 1 - Meeting Notes Normalizer

## Goal

Build a Python script that reads a meeting-notes text file, extracts the important fields, and saves them as structured JSON.

This is an individual assignment. You may refer to the class project, but your submitted program must work with the meeting-notes format below.

## Input format

Your program must read `data/meeting-notes.txt`:

```text
Title: Checkout Reliability Review
Owner: Riya
Date: 2026-08-24
Attendees: Riya, Sam, Noor
Decisions: Add retry logging; create a payment failure dashboard
Actions: Sam|Add structured logs|2026-08-26; Noor|Draft dashboard|2026-08-28
```

## Required output

Create `output/meeting-summary.json` with this shape:

```json
{
  "title": "Checkout Reliability Review",
  "owner": "Riya",
  "date": "2026-08-24",
  "attendees": ["Riya", "Sam", "Noor"],
  "decisions": [
    "Add retry logging",
    "create a payment failure dashboard"
  ],
  "actions": [
    {
      "owner": "Sam",
      "task": "Add structured logs",
      "due_date": "2026-08-26"
    },
    {
      "owner": "Noor",
      "task": "Draft dashboard",
      "due_date": "2026-08-28"
    }
  ]
}
```

## Requirements

- Use `pathlib` to read and write files.
- Use at least three functions: `read_notes`, `parse_notes`, and `save_summary`.
- Represent the overall result with a dictionary.
- Represent attendees, decisions, and actions with lists.
- Create the output directory when it does not exist.
- Handle a missing input file with a useful message.
- Raise or report a useful error when `Title`, `Owner`, or `Date` is missing.
- Save indented, valid JSON.
- Include a `README.md` containing setup and run instructions.

## Stretch goals

- Validate that each action has exactly three `|`-separated values.
- Accept the input path from the command line.
- Add two automated tests using `unittest`.

## Submission

Submit one of the following by **<DATE AND TIME>**:

- a GitHub repository link; or
- a zip containing the complete project.

Your submission must include:

- source code;
- the input file;
- one generated JSON output;
- your README;
- a short reflection answering: What failed first, and how did you diagnose it?

Do not include `.venv`, cache folders, secrets, or unrelated files.

## Rubric - 20 points

| Area | Points | Evidence |
|---|---:|---|
| Correct file handling | 4 | Reads the supplied input and creates the output safely |
| Correct data structure | 5 | Output matches the required dictionary/list shape |
| Functions and readability | 4 | Logic is split into clear, named functions |
| Error handling | 3 | Missing files and required fields produce useful messages |
| Reproducibility | 2 | README lets another learner run the project |
| Reflection | 2 | Explains one failure and the debugging approach |

## Academic integrity

AI coding tools are allowed. You are responsible for understanding every submitted line. In the review, you may be asked to change one field or explain one function without assistance.
