from flask import Flask, jsonify,render_template
#the render_template is used to render templates in flask
from database import jobs_data,load_particular_job
app = Flask(__name__)





@app.route("/")
def hello():
    return render_template("home.html",jobs=jobs_data)
  


  

@app.route("/api/job/<job_id>")
def particular_job(job_id):
    job = load_particular_job(job_id=job_id)
    if not job:
        return "Job Not available",404
    else:
        return render_template("jobitempage.html",job=job)


if __name__ == "__main__":
   app.run(host='0.0.0.0',debug=True)
   


