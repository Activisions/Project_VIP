from imports import *
import json

#לא להתייחס נחליף פרטים ואתר בהמשך בהתאם לפרוייקט שעליו נעבוד


URL1 = "https://calendarv4-api.lupa.co.il/api.aspx?method=getcalendar&calendar_token=d69372d97343495abda62575d4096400&token=XfrnyMrSiB1LofuUcPchsLCq_00ffPB6h0jbk1gTfzvSSjJsywsW11_W8t5XCfPCAvk4zXY6l5_zjyx_6ifDnhLByD45EVyqfCPy29iwb0TFLWlRUyJD9WkjL5JI6yVIRVLpEr11kQDvyFKN_7F7IyyXwhBsD8hiGNrwJ_4L5KOChpSW6bSvTswDGxEAdHXy9p_-2A3yJyeOIw-4hMb8_NXdGiajGwBFYAaQST3zCNC793K72Bbof8b5stvO_4dOTj7eyzs8vo1ku0aPsWslISWXZlMuNj6THs4d3dswDV4OUTfI95CQAAzCwzbtnSC9Bqk9YIV2BlTy7WKyjv1HFw2"
def test_calendar_data():
    response = requests.get(URL1)
    data = response.json()

    calendar_version = data['Response']['DateSettings']['StartYear']
    assert calendar_version == 2024

    is_valid = data.get('isValid')
    assert is_valid is True
