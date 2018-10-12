# Wellframe

This API was implemented using Python 3.6 and Flask. If your machine does not have Flask installed, please install Flask using the line below.
```
pip install flask-restful
```

Use the following line to run the API.
```
python wellframe.py
```

### Functionality
```
GET /patient/:name
```
- returns JSONified data attributed to a patient's name

```
POST /patient/:name
```
- creates a new patient and then adds them to the list of patients

```
PUT /patient/:name
```
- allows the user to assign a patient with new medication
- if the medication is not in the list of available medications, returns an error message

```
DELETE /patient/:name
```
- allows the user to delete a medication from the list of medications assigned to the patient

```
GET /medication/:name
```
- returns JSONified data attributed to a patient's name (currently just the name of the medication)

```
POST /medication/:name
```
- adds a new medication to the list of available medications

```
DELETE /medication/:name
```
- allows the user to delete a medication from the list of available medications
