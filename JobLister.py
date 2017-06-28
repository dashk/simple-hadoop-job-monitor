import os, datetime

ONE_MINUTES_IN_SECONDS = 60

def parse_job_info(job_info_string):
	parsed_data = job_info.split('\t')
	start_time = datetime.datetime.fromtimestamp(int(parsed_data[2])/1000.0)
        current_time = datetime.datetime.now()
	delta = (current_time - start_time).seconds / ONE_MINUTES_IN_SECONDS
	return [ parsed_data[3], delta, parsed_data[0] ]

def get_jobs(temp_dir = './'):
	os.system("hadoop job -list > " + temp_dir + "hadoop_job_list.txt")
	with open("hadoop_job_list.txt", "r") as hadoop_job_list_file_handler:
		job_lines = hadoop_job_list_file_handler.readlines()

	jobs = []
	for job_info_line in job_lines:
		if job_info_line.startswith("job_"):
			jobs.append(parse_job_info(job_info_line))

	return jobs
