from flask import g, request, jsonify
import jobs.db as db
from jobs.app import app


@app.route('/api/jobs')
def jobs():
    jobs = db.execute_sql('SELECT job.id, job.title, job.description, job.salary, \
        employer.id as employer_id, employer.name as employer_name FROM job \
            JOIN employer ON employer.id = job.employer_id', jsonify=True)
    
    return jsonify({'jobs': jobs})


@app.route('/api/job/<job_id>')
def job(job_id):
    job = db.execute_sql('SELECT job.id, job.title, job.description, job.salary, \
        employer.id as employer_id, employer.name as employer_name FROM job \
            JOIN employer ON employer.id = job.employer_id WHERE job.id = ?', [job_id], \
                single=True, jsonify=True)

    return jsonify({'job': job})
