# LBU Open Day Website

A promotional single-page website for Software Engineering at Leeds Beckett University.

## Overview

This website showcases the Software Engineering programme at Leeds Beckett University, designed for use at open days and recruitment events. It features information about the course, career prospects in software engineering, and contact details.

## Features

- **Full-width header** with university branding
- **Two-column layout** (70-30 split):
  - Left column: Detailed information about the Software Engineering course
  - Right column: Facts about software engineering as a career
- **University purple color scheme** matching Leeds Beckett University branding
- **Full-width footer** with comprehensive contact information
- **Responsive design** that works on desktop, tablet, and mobile devices

## Files

- `index.html` - Main HTML structure of the website
- `styles.css` - Styling with LBU purple color scheme and responsive layout
- `serve.py` - Python HTTP server script to run the website locally
- `README.md` - This file

## Running the Website

### Prerequisites

- Python 3.x installed on your system

### Starting the Server

1. Navigate to the project directory:
   ```bash
   cd lbu-open-day-web
   ```

2. Run the Python server script:
   ```bash
   python3 serve.py
   ```
   or
   ```bash
   ./serve.py
   ```

3. Open your web browser and visit:
   ```
   http://localhost:8080
   ```

4. To stop the server, press `Ctrl+C` in the terminal

## Development

The website uses:
- Semantic HTML5 structure
- Modern CSS with flexbox for layout
- CSS custom properties (variables) for consistent theming
- Mobile-first responsive design principles

## Color Scheme

The website uses Leeds Beckett University's official purple:
- Primary Purple: `#5B2B82`
- Dark Purple: `#3d1a57`
- Light Purple: `#8b5fb8`

## License

© 2024 Leeds Beckett University. All rights reserved.