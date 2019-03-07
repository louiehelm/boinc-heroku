import os, time, requests, uuid

print(os.system("wget https://boinc.berkeley.edu/dl/boinc_7.4.22_x86_64-pc-linux-gnu.sh"))

time.sleep(0.5)  # wait for boinc to start

print(os.system("chmod +x boinc_7.4.22_x86_64-pc-linux-gnu.sh"))

time.sleep(0.5)  # wait for boinc to start

print(os.system("./boinc_7.4.22_x86_64-pc-linux-gnu.sh"))

time.sleep(0.5)  # wait for boinc to start

print(os.system("cd BOINC/; chmod +x boinc; chmod +x boinccmd"))

time.sleep(0.5)  # wait for boinc to start

print(os.system("wget https://rockstarresearch.com/boinc/global_prefs_override.xml; wget https://rockstarresearch.com/boinc/cc_config.xml"))

time.sleep(0.5)  # wait for boinc to start

print(os.system("mkdir -p projects/www.primegrid.com; cd projects/www.primegrid.com; wget https://rockstarresearch.com/boinc/app_config.xml"))

time.sleep(0.5)  # wait for boinc to start

print(os.system("cd ~/BOINC; ./boinc --daemon"))

time.sleep(0.5)  # wait for boinc to start

print(os.system("./boinccmd --project_attach http://www.primegrid.com/ 1046422_ff435ca1d4f1cbebbeba4ca39ecfeae4"))

time.sleep(0.5)  # wait for boinc to start

print(os.system("./boinccmd --get_tasks"))

time.sleep(0.5)  # wait for boinc to start

instance_id = str(uuid.uuid4())
lead_url = "https://dev777.herokuapp.com/"
report_back_postfix = "/internals/v0.01-ping"


while True:
   time.sleep(10)
   requests.post(lead_url + report_back_postfix + instance_id)
   print("UUID: " + str(instance_id))
   pass
