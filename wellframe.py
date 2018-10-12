from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

patients = []
medications = []

class Patient(Resource):
    def get(self, name):
        for patient in patients:
            if(name == patient["name"]):
                return patient
        return "Patient not found"

    def post(self, name):
        for patient in patients:
            if (name == patient["name"]):
                return "Patient {} already exists".format(name)

        patient = {
            "name" : name,
            "medications" : []
        }

        patients.append(patient)
        return patient

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("medications")
        args = parser.parse_args()

        available = False

        for med in medications:
            if (args["medications"] == med["name"]):
                available = True

        if (not available):
            return "Medication {} is not available.".format(args["medications"])

        for patient in patients:
            if (name == patient["name"]):
                if (args["medications"] in patient["medications"]):
                    return "Patient {} already takes {}".format(name, args["medications"])
                (patient["medications"]).append(args["medications"])
                return patient

        patient = {
            "name": name,
            "medications": [args["medications"]],
        }

        patients.append(patient)
        return patient

    def delete(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("medications")
        args = parser.parse_args()

        for patient in patients:
            if (name == patient["name"]):
                patient["medications"] = [med for med in patient["medications"] if args["medications"] != med]
                return "Medication {} has been deleted from Patient {}'s list of medications".format(args["medications"], name)

        return "Patient {} does not exist".format(name)


class Medication(Resource):
    def get(self, name):
        for medication in medications:
            if(name == medication["name"]):
                return medication
        return "Medication not found"

    def post(self, name):
        for medication in medications:
            if (name == medication["name"]):
                return "Medication {} already exists".format(name)

        medication = {
            "name": name
        }

        medications.append(medication)
        return medication

    def delete(self, name):
        global medications
        medications = [med for med in medications if name != med["name"]]
        return "Medication {} has been deleted.".format(name)

      
api.add_resource(Patient, "/patient/<string:name>")
api.add_resource(Medication, "/medication/<string:name>")

app.run(debug=False)
