# Crowd-Funding Web Application

Crowdfunding is the practice of funding a project or venture by raising small amounts of money from a large number of people, typically via the Internet. The aim of this project is to create a web platform for starting fundraising projects in Egypt.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

1. **Authentication System:**
   - Registration with email verification.
   - Login with email and password.
   - Login with Facebook account (Bonus).
   - Forgot Password (Bonus).
   - User Profile:
     - View profile information.
     - View owned projects.
     - View donations.
     - Edit profile information (except email).
     - Delete account with confirmation (Bonus: password required).
2. **Projects:**
   - Create fundraising campaigns with:
     - Title
     - Details
     - Category
     - Multiple pictures
     - Total target
     - Multiple tags
     - Start/end time for the campaign
   - View projects and donate.
   - Add comments on projects (Bonus: with replies).
   - Report inappropriate projects or comments.
   - Rate projects.
   - Project creators can cancel projects if donations are less than 25% of the target.
   - Project page displays overall average rating, project pictures in a slider, and 4 similar projects based on tags.
3. **Homepage:**
   - Slider to show the highest five rated running projects.
   - List of the latest 5 projects.
   - List of latest 5 featured projects.
   - List of categories with their projects.
   - Search bar to search projects by title or tag.

## Technologies Used

- Vue.js
- Django
- MySQL

## Project Structure
```
project/
├── frontend/ # Vue.js frontend
├── src/
├── public/
├── ...
├── backend/ # Django backend
├── app/
├── manage.py
├── ...
├── database/ # MySQL database schema
├── schema.sql
├── ...
├── related_images/ # Screenshots related to the project
├── AboutUs.png
├── Schema.png
├── admin-add-feature-project.png
├── ...
└── README.md

```

## Screenshots

- About Us
  ![About Us](related_images/AboutUs.png)

- Database Design Schema
  ![Database Design Schema](related_images/Schema.png)

- Homepage
  ![Homepage](related_images/home-page.png)

- User Donates to a Project
  ![User Donates to a Project](related_images/user-donate.png)

- User Reports a Comment
  ![User Reports a Comment](related_images/user-report-a-comment.png)

- Admin Reports Page
  ![Admin Reports Page](related_images/admin-reports-page.png)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your_username/your_project.git
```
2. Install dependencies:
```bash
# Frontend
cd frontend
npm install

# Backend
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
3. Database setup:
- Create a MySQL database.
- Import schema.sql to set up the database schema.

4. Configuration:
- Configure backend settings in backend/project/settings.py.
- Configure database settings in backend/project/settings.py
