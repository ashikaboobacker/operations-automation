# Simple workflow automation script

def process_properties(properties):
    processed = []
    
    for property in properties:
        if property.get("status") == "active":
            processed.append({
                "name": property["name"],
                "occupancy": property.get("occupancy", 0),
                "status": "processed"
            })
    
    return processed


if __name__ == "__main__":
    sample_data = [
        {"name": "Property A", "status": "active", "occupancy": 85},
        {"name": "Property B", "status": "inactive", "occupancy": 40}
    ]
    
    result = process_properties(sample_data)
    print(result)
