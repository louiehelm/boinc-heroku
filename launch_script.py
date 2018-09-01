import os, time, requests, uuid

print(os.system("mkdir boinc-data"))  # create boinc data directory

print(os.system("boinc --dir ./boinc-data & "))

time.sleep(0.5)  # wait for boinc to start

print(
os.system("boinccmd --host 127.0.0.1 --dir ./boinc-data --passwd  1046422_ff435ca1d4f1cbebbeba4ca39ecfeae4 project_attach http://www.primegrid.com/  &")
)

instance_id = str(uuid.uuid4())
lead_url = "https://boincer.herokuapp.com/"
report_back_postfix = "/internals/v0.01-ping"


while True:
   time.sleep(10)
   requests.post(lead_url + report_back_postfix + instance_id)
   print("UUID: " + str(instance_id))
   pass
