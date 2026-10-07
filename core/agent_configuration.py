import json

def configuration(path):
    enabled_sources = []
    with open(path, "r", encoding="utf-8") as f:
        config = json.load(f)
    sources = config["sources"]

    for source in sources:
        if source["enabled"]:
            enabled_sources.append(source)
    
    return enabled_sources




