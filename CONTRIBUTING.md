# Contributing

## Scope

This repository is the practical support for the Pipeline Craft GitLab CI/CD labs.
Contributions must preserve its pedagogical purpose: each change should improve
the learning path, the reproducibility of the labs, or the security and clarity
of the training material.

## Before Contributing

Read the associated guide on the blog before changing a lab.

Expected workflow:

1. Read the guide on the site.
2. Read the corresponding lab page.
3. Work in the repository on the appropriate branch.

## Branch Model

This project uses two branch families for each lab:

- `starter/lab-XX`: intentionally incomplete or flawed starting point for learners.
- `solution/lab-XX`: expected corrected state for the same lab.

Protected branches:

- `main`
- `starter/*`
- `solution/*`

Do not push directly to these branches unless you are maintaining the official training content.
Preferred workflow for external changes:

1. Fork the repository.
2. Create a working branch from the appropriate base.
3. Open a merge request.

## Contribution Rules

Keep contributions focused.

Good contribution examples:

- improve an existing lab objective or fix a broken exercise
- clarify learner-facing instructions
- correct CI configuration while preserving the teaching goal
- improve test reliability or local reproducibility
- harden GitLab security settings or pipeline practices

Avoid unrelated refactors across many labs in a single change.

## Security Expectations

This repository is public and used for training. Treat it as production-grade public content.

Never commit:

- credentials
- tokens
- private registry passwords
- unmasked secrets in CI variables
- customer or personal data

Prefer:

- environment variables
- masked and protected GitLab CI/CD variables
- ephemeral test values only

If your change affects CI/CD security, document:

- what risk is being reduced
- what GitLab setting or YAML behavior changed
- how to validate the new behavior

## Merge Request Expectations

Before opening a merge request:

1. Run local checks when applicable.

```bash
ruff check app/ tests/
pytest
```

2. Validate `.gitlab-ci.yml` before pushing when CI changes are involved.

```bash
glab ci lint .gitlab-ci.yml
```

3. Explain the pedagogical intent of the change in the merge request description.

Useful MR description template:

- Target lab(s):
- Problem fixed:
- Expected learner outcome:
- Validation performed:
- Security impact:

## Style Guidelines

For repository content:

- prefer small, explicit changes
- preserve branch-to-branch teaching progression
- keep starter branches intentionally imperfect when required by the lab
- keep solution branches correct, readable, and minimal

For learner-facing documentation:

- write clearly for beginners
- explain why a step exists, not only what to type
- avoid chapters made only of code, lists, or tables

## License

By contributing to this repository, you agree that your contributions are
distributed under the repository license:

- Creative Commons Attribution 4.0 International
- https://creativecommons.org/licenses/by/4.0/

Attribution to the original author must be preserved.
