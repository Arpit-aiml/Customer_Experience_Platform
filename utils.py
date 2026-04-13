def detect_issue(text):
    text = text.lower()
    
    if "late" in text or "delay" in text:
        return "Delivery Issue"
    elif "bad" in text or "worst" in text or "damaged" in text:
        return "Quality Issue"
    elif "expensive" in text or "costly" in text:
        return "Prize Issue"
    else:
        return "No major Issue"