import Pyro4
import json
import os


@Pyro4.expose
class SymptomsAnalyzer:

    def __init__(self):
        print("built")

    def file_path(self):
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(THIS_FOLDER, 'diseases.json')

    def load_deseases(self):

        path = self.file_path()

        with open(path, 'r') as diseases_file:
            diseases = json.load(diseases_file)
            return diseases

    def diagnose(self, symptoms):

        diseases = self.load_deseases()

        for disease in diseases['diseases']:

            count = 0

            for symptom in symptoms:
                if(symptom in disease["symptoms"]):
                    count = count + 1
                else:
                    break

                if(count == len(disease["symptoms"])):
                    return disease

        return None

        #diseases = self.load_deseases()
        # return diseases


if __name__ == "__main__":

    sa = SymptomsAnalyzer()
    res = sa.diagnose(['fiebre', 'falta de aire', 'tos'])
    print(res)
