
import json

data = json.loads('{"val2": [{"value": "Dibrugarh", "key": "E41"}, {"value": "Guwahati", "key": "E40"}], "val1": {"value": "Assam", "key": "AS"}}')

if "val1" in data:
    val1_data = data["val1"]
    if isinstance(val1_data, dict) and "key" in val1_data:
        key_val1 = val1_data["key"]
        new_data = {}
        for val2_item in data.get("val2", []):
            if "key" in val2_item:
                new_data[val2_item["key"]] = key_val1
        new_json = json.dumps(new_data)
        print(new_json)