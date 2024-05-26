from flask import Flask, jsonify,render_template
#the render_template is used to render templates in flask
app = Flask(__name__)



JOBS =[
    {
        "id": 1,
        "title": "Software Engineer",
        "location": "San Francisco, CA",
        "Salary": "$120,000"
    },
    {
        "id": 2,
        "title": "Data Scientist",
        "location": "New York, NY",
        "Salary": "$110,000"
    },
    {
        "id": 3,
        "title": "Product Manager",
        "location": "Austin, TX",
        "Salary": "$105,000"
    },
    {
        "id": 4,
        "title": "UX Designer",
        "location": "Seattle, WA",
        "Salary": "$95,000"
    },
    {
        "id": 5,
        "title": "DevOps Engineer",
        "location": "Remote",
        "Salary": "$100,000"
    },
    {
        "id": 6,
        "title": "QA Engineer",
        "location": "Chicago, IL",
        "Salary": "$85,000"
    },
    {
        "id": 7,
        "title": "Marketing Specialist",
        "location": "Boston, MA",
        "Salary": "$70,000"
    },
    {
        "id": 8,
        "title": "Sales Manager",
        "location": "Los Angeles, CA",
        "Salary": "$90,000"
    },
    {
        "id": 9,
        "title": "HR Coordinator",
        "location": "Miami, FL",
        "Salary": "$65,000"
    },
    {
        "id": 10,
        "title": "Business Analyst",
        "location": "Denver, CO",
        "Salary": "$80,000"
    },
     {
    "id": 11,
    "title": "Quality Assurance Engineer",
    "location": "Atlanta, GA",
  },
]


@app.route("/")
def hello():
    return render_template("home.html",jobs=JOBS)
  

@app.route("/me")
def me():
    return "this is me"
  

#listing data in json format
@app.route("/api/jobs")
def jobs_list():
    return jsonify(JOBS)
  
  
if __name__ == "__main__":
   app.run(host='0.0.0.0',debug=True)
   


