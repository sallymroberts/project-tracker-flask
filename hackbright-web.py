from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks') #default values
    first, last, github = hackbright.get_student_by_github(github)
    html = render_template("student_info.html", 
                            first=first, 
                            last=last,
                            github=github)
    return html

@app.route("/input-new-student")
def student_add():
    """Input info for a new student."""
    return render_template("input_new_student.html")

    first = request.args.get('first')
    last = request.args.get('last')
    github = request.args.get('github')

    html = render_template("add-student-toDB.html", 
                            first=first, 
                            last=last,
                            github=github)
    return html

@app.route("/add-student-toDB")
def new_student():
    """Add new student to DB, and show information."""

    hackbright.make_new_student(first, last, github)
    return render_template("add_student_toDB.html",
                            first=first,
                            last=last,
                            github=github)


if __name__ == "__main__":
    app.run(debug=True)