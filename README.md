# Static-Sight-Generator
# Static Site Generator

A simple static site generator built in Python as part of my backend development practice. It converts markdown content into HTML pages and copies static assets into a public directory.

## Features

- Converts markdown files to HTML
- Uses an HTML template for page generation
- Recursively builds pages from nested content directories
- Copies static files like CSS and images

## Project Structure

```text
content/     # markdown content
static/      # css, images, and other assets
public/      # generated site output
src/         # python source code
template.html
