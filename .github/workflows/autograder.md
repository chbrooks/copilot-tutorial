---
name: autograder
description: Autograder workflow that checks PR work against the data-8/textbook repository
triggers:
  - pull_request:
      types: [opened]
env:
  REFERENCE_REPO: "https://github.com/data-8/textbook"
  
tools:
  - type: github
  - type: web_fetch
---

# Autograder Workflow

This workflow automatically checks new pull requests against the reference textbook repository (data-8/textbook).

## Trigger

Runs whenever a pull request is opened.

## Workflow Steps

1. **Fetch PR Information**
   - Get the PR title, description, and list of changed files
   - Extract the content of modified files

2. **Fetch Reference Content**
   - Pull the corresponding content from https://github.com/data-8/textbook
   - Compare the structure and content

3. **Perform Checks**
   - Verify file structure and formatting
   - Check for consistency with the reference textbook
   - Validate code examples and explanations
   - Look for completeness and accuracy

4. **Provide Feedback**
   - Comment on the PR with:
     - ✅ Passed checks
     - ⚠️ Warnings or suggestions
     - ❌ Failed checks that need attention
   - Provide specific recommendations for improvement

## Execution

The agent will:
- Analyze the PR changes in detail
- Compare against the reference textbook repository
- Evaluate code quality, accuracy, and completeness
- Generate constructive feedback as a PR comment
