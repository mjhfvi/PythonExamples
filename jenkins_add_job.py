from __future__ import annotations

import jenkins
# import xml.etree.ElementTree as ET

# Jenkins connection details
jenkins_url = 'http://jenkins.localhost'
# username = ''
# password = ''

# Create a Jenkins server object
server = jenkins.Jenkins(jenkins_url, username=username, password=password)

# Job name and config
job_name = 'NewJobName'

# Read the XML config file
with open('config.xml', 'r') as file:
    job_config = file.read()

try:
    # Create the job
    server.create_job(job_name, job_config)
    print(f"Job '{job_name}' created successfully")
except jenkins.JenkinsException as e:
    print(f"Error creating job: {e}")

# Verify the job was created
job_info = server.get_job_info(job_name)
print(f"Job info: {job_info['url']}")
