import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='emmanuelonly',
    database='jobs'
)

cursor = conn.cursor()

def load_jobs():
    select_jobs = (
    "SELECT * FROM careers"
    )
    cursor.execute(select_jobs)
    # Fetch all results from the executed query
    jobs = cursor.fetchall()
    # Get column names from the cursor
    columns = cursor.column_names
    job_result = []
    # Print each job record as a dictionary
    for job in jobs:
        job_dict = dict(zip(columns, job))
        job_result.append(job_dict)
    return job_result


def load_particular_job(job_id):
    select_job =(
        f"SELECT * FROM careers where jobs_id={job_id}"
    )
    cursor.execute(select_job)
    print("this is ",cursor)
    jobs = cursor.fetchall()
    columns = cursor.column_names
    job_result = []
    for job in jobs:
        job_dict = dict(zip(columns,job))
        job_result.append(job_dict)
    return job_result  


jobs_data = load_jobs()



# Close the cursor and connection
#cursor.close()
#conn.close()