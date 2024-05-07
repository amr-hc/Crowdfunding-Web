# Crowd-Funding Web Application

Crowdfunding is the practice of funding a project or venture by raising small amounts of money from a large number of people, typically via the Internet. The aim of this project is to create a web platform for starting fundraising projects in Egypt.

## Table of Contents

- [Features](#features)
- [DataBase Schema](#DataBase-Schema)
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

## DataBase Schema
 ![](related_images/Schema.png)

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

## Functionality Screenshots

### User Interface

* **About Us:** ![About Us page](related_images/AboutUs.png)
* **Homepage:** ![Homepage](related_images/home-page.png)
* **User Donates to a Project:** ![User Donation](related_images/user-donate.png)
* **User Reports a Comment:** ![User Reporting a Comment](related_images/user-report-a-comment.png)

### Admin Panel

* **Reports Page:** ![Admin Reports Page](related_images/admin-reports-page.png)
* **Project Management:**
    * Add Project with Features: ![Admin Adding Project](related_images/admin-add-feature-project.png)
    * View All Projects (including canceled): ![Admin Viewing All Projects](related_images/admin-all-projects-with-canceled.png)
    * Delete Project: ![Admin Deleting Project](related_images/admin-delete-project.png)
* **Category and Tag Management:** ![Admin Viewing Categories and Tags](related_images/all-categories-and-tags.png)
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

## Usage
1. Run the backend server:
```bash
cd backend
python manage.py runserver
```
2. Run the frontend:
```bash
cd frontend
npm run serve
```
3. Open your browser and go to http://localhost:8080 to access the application.

## Contributors
| [![Ahmed Dabour](https://avatars.githubusercontent.com/u/90671017?v=4&s=50)](https://github.com/dabour1) | Ahmed Dabour | [Ahmed Dabour](https://github.com/dabour1) |
| [![Amr Elrefaaey](https://avatars.githubusercontent.com/u/156538554?v=4&s=50)](https://github.com/amr-hc) | Amr Elrefaaey | [Amr Elrefaaey](https://github.com/amr-hc) |
| [Avatar URL 3] | Amir Elattar | [Bob Johnson](https://github.com/bobjohnson) |
| [Avatar URL 3] | Doha Seif | [Bob Johnson](https://github.com/bobjohnson) |
| [Avatar URL 3] | Mohamed Abdelazeem | [Bob Johnson](https://github.com/bobjohnson) |
| [Avatar URL 3] | Ahmed Nagy | [Bob Johnson](https://github.com/bobjohnson) |


