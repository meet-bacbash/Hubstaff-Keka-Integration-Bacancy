import requests
from tqdm import tqdm
from persistqueue import Queue
import json


def keka_log(user_id):
    q1 = Queue("user_timings_queue", autosave=True)
    user_id = user_id
    l1 = {}
    # url = "https://cin02.a.keka.com/v1/logs"


    while not q1.empty():
        l1 = q1.get()

    if l1:
        # with tqdm(total=len(l1), desc="Uploading Data to Keka", unit="chunk") as pbar:
        for key,value in l1.items():
            data = []
            for i in value:
                # print(i)
                val = {
                    "DeviceIdentifier": "648f6f6a-1edb-42fa-9f4a-3afaf254afdd",
                    "EmployeeAttendanceNumber": key,
                    "Timestamp": i['clock_in'],
                    "Status": 0
                }

                val2 = {
                    "DeviceIdentifier": "648f6f6a-1edb-42fa-9f4a-3afaf254afdd",
                    "EmployeeAttendanceNumber": key,
                    "Timestamp": i['clock_out'],
                    "Status": 1
                }

                data.append(val)
                data.append(val2)

            payload = f"""
            [
                {', '.join([f'''
                {{
                    "DeviceIdentifier": "{entry['DeviceIdentifier']}",
                    "EmployeeAttendanceNumber": "{user_id}",
                    "Timestamp": "{entry['Timestamp']}",
                    "Status": {entry['Status']}
                }}''' for entry in data])}
            ]
            """

            # with open('user_data.json', 'a') as f:
            #     json.dump(payload, f, indent=4)

            print(payload)
            print("==============================================")
            # pbar.update(1)

            # headers = {
            #     'Content-Type': 'application/json',
            #     'X-API-Key': '29096d92-5808-4940-9ce0-f6ecbc305860'
            # }
            #
            # response = requests.request("POST", url, headers=headers, data=payload)
            #
            # if response.status_code == 200:
            #     print(response.text)
            #     logger.info(f"{response.status_code} - {response.text} : payload - {payload}")
            # else:
            #     logger.error(f"{response.status_code} - {response.text} : payload - {payload}")
            #     i['status_code'] = response.status_code
            #     i['status_text'] = response.text
            #     q1.put(i)
            #     print(f"Error: {response.status_code}, {response.text}")
