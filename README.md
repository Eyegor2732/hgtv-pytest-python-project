🧪 HGTV Sweepstakes Automation (Python · Pytest)

End-to-end automation project that programmatically submits entries to HGTV.com sweepstakes using Python.
Designed to demonstrate test automation best practices, scalable test design, and environment-driven configuration using pytest and the Page Object Model.


🔎 Project Overview

This project automates the HGTV sweepstakes entry workflow by:

- Reading multiple test accounts (emails) from environment configuration

- Iterating through entries in a data-driven manner

- Validating successful submission via automated assertions

- Organizing test logic using clean, maintainable architecture

The repository is intended as a QA Automation / SDET portfolio project showcasing real-world testing patterns rather than a simple script.


🧩 Key Features

- Data-Driven Testing

- - Sweepstakes entry emails are externalized in a .env file

- - Supports scalable test execution across multiple inputs

- Pytest-Based Test Framework

- - Uses pytest test discovery, fixtures, and assertions

- - Easy integration with CI pipelines

- Page Object Model (POM)

- - UI interactions encapsulated in reusable page classes

- - Clear separation between test logic and page behavior

- Maintainable Project Structure

- - Logical folder organization (tests, page_objects, utilities)

- - Easily extensible for additional sweepstakes or validations


📁 Project Structure

├── page_objects/        # Page Object classes representing HGTV pages

├── utilities/           # Shared helpers (env loading, common logic)

├── tests/               # pytest test cases

├── .env                 # Environment-specific test data (excluded from VCS)

├── .gitignore

├── README.md


🔐 Test Data Configuration

All test emails are supplied via a .env file to ensure:

No hard-coded test data in source code

Secure and flexible configuration across environments

Example .env

email1=user1@email.com

email2=user2@email.com

email3=user3@email.com

email4=user4@email.com


⚙️ Tech Stack

Tool / Technology	Usage

Python	Core automation language

Pytest	Test execution and assertions

python-dotenv	Environment variable management

Page Object Model	Scalable test design pattern


🚀 Setup & Execution
Prerequisites

- Python 3.9+

- pip

- Virtual environment (recommended)

Installation
git clone https://github.com/Eyegor2732/hgtv-pytest-python-project.git

cd hgtv-pytest-python-project

pip install -r requirements.txt

Run Tests

pytest

Run a specific test:

pytest --retries 5 --retry-delay 5 --browser_name firefox_headless


🧠 What This Project Demonstrates

- Designing maintainable automation frameworks

- Applying Page Object Model in Python

- Implementing data-driven testing with environment configuration

- Writing clean, readable, and scalable pytest tests

- Organizing test automation code for long-term maintenance


⚠️ Disclaimer

This project is intended for educational and portfolio purposes only.
Users are responsible for ensuring compliance with HGTV’s terms of service and sweepstakes rules.


📌 Available options

- CI integration (GitHub Actions)

- Parallel test execution (not recommended because it's not human behaviour)

- Reporting (HTML / Allure / JSON)

- Support for additional sweepstakes sites
