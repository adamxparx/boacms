Project title & short description
Barangay Online Appointment and Certification Management System, an online appointment and certification management system that streamlines the process of acquiring barangay certifications while enhancing accessibility, transparency, and efficiency in service delivery—ultimately improving citizen satisfaction and strengthening barangay governance.

Tech stack used
Backend:
Django – Serves as the main backend framework, handling server-side logic, authentication, and database interactions.
Supabase – Provides the database and authentication services, offering a PostgreSQL backend with real-time capabilities and easy integration with Django.

Frontend:
HTML – Defines the structure and layout of the web pages.
CSS – Styles the user interface to ensure a clean and responsive design.
JavaScript – Adds interactivity and dynamic behavior to the frontend.

Version Control:
Git & GitHub – Used for source code management, version control, and team collaboration.

Setup & run instructions
1. Clone the repository
	git clone https://github.com/adamxparx/CSIT327-G2-BOACMS.git

2. Change directory to the cloned project
	cd CSIT327-G2-BOACMS

3. Create the virtual environment
	python -m venv venv

4. Activate the virtual environment
	venv\Scripts\activate		# for Windows
	source venv/bin/activate	# for macOS or Linux

5. Install the required packages
	pip install -r requirements.txt

6. Create .env file to store environment-specific variables and paste the following content
	# Supabase credentials
	DB_ENGINE=django.db.backends.postgresql_psycopg2
	DB_NAME=postgres
	DB_USER=postgres.syqrwazhtflzztakolkj
	DB_PASSWORD=R@nd0mP@$$w0rdNg@n!
	DB_HOST=aws-1-ap-southeast-1.pooler.supabase.com
	DB_PORT=5432

	# Email credentials
	EMAIL_HOST=smtp.gmail.com
	EMAIL_PORT=587
	EMAIL_USE_TLS=True
	EMAIL_HOST_USER=cloydadam.esparcia@gmail.com
	EMAIL_HOST_PASSWORD=ncbdqkhsktmzddvx

7. Run the server
	python manage.py runserver
