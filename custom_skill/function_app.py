import logging
import json
import azure.functions as func

# Mock ML Model loading (replace with actual model loading logic)
# from sklearn.externals import joblib
# model = joblib.load('model.pkl')

def predict_category(text):
    """
    Mock prediction logic.
    Replace this with: return model.predict([text])[0]
    """
    text_lower = text.lower()
    if 'urgent' in text_lower or 'deadline' in text_lower:
        return 'High-Priority'
    elif 'archive' in text_lower or 'old' in text_lower:
        return 'Archived'
    else:
        return 'Standard'

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Custom Skill: Document Classification Triggered.')

    try:
        body = req.get_json()
    except ValueError:
        return func.HttpResponse("Invalid Body", status_code=400)

    # The WebApiSkill sends a batch of values.
    # Input structure: {"values": [ {"recordId": "...", "data": {"text": "..."}} ]}
    values = body.get('values')
    results = {}
    results["values"] = []

    for value in values:
        record_id = value.get('recordId')
        data = value.get('data')
        text = data.get('text', '')

        # Perform classification
        try:
            category = predict_category(text)
            
            # Append result
            results["values"].append({
                "recordId": record_id,
                "data": {
                    "category": category
                }
            })
        except Exception as e:
            logging.error(f"Error processing record {record_id}: {e}")
            results["values"].append({
                "recordId": record_id,
                "errors": [{"message": str(e)}]
            })

    return func.HttpResponse(
        json.dumps(results),
        mimetype="application/json"
    )
