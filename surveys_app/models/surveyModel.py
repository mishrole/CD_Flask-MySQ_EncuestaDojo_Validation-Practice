from flask import flash
from surveys_app.config.mysqlconnection import connectToMySQL
from surveys_app.models import dojoModel, languageModel

class Survey:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo = dojoModel.Dojo
        self.language = languageModel.Language

    @classmethod
    def get_survey_dojo_language_by_id(cls, data):
        query = "Select distinct * from surveys join dojos on surveys.dojo_id = dojos.id join languages on languages.id = surveys.language_id where surveys.id = %(surveyId)s;"
        results = connectToMySQL('dojo_survey_schema').query_db(query, data)

        survey = None

        if results:
            if len(results) > 0:
                survey = cls(results[0])

        for row_from_db in results:
            print(row_from_db)
            dojo_data = {
                'id': row_from_db['dojos.id'],
                'name': row_from_db['dojos.name'],
                'created_at': row_from_db['dojos.created_at'],
                'updated_at': row_from_db['dojos.updated_at']
            }

            language_data = {
                'id': row_from_db['languages.id'],
                'name': row_from_db['languages.name'],
                'created_at': row_from_db['languages.created_at'],
                'updated_at': row_from_db['languages.updated_at']
            }

            survey.dojo = dojoModel.Dojo(dojo_data)
            survey.language = languageModel.Language(language_data)

        return survey

    @classmethod
    def save(cls, data):
        query = "Insert into surveys (name, dojo_id, language_id, comment, created_at, updated_at) values (%(name)s, %(dojoId)s, %(languageId)s, %(comment)s, NOW(), NOW());"
        return connectToMySQL('dojo_survey_schema').query_db(query, data)

    @staticmethod
    def validateSurvey(survey):
        is_valid = True

        if len(survey['name']) < 3:
            flash('Name must be at least 3 characters long')
            is_valid = False
        
        if len(survey['comment']) < 3:
            flash('Comment must be at least 3 characters long')
            is_valid = False
        
        if len(survey['dojo']) == 0:
            flash('Must choose a Dojo location')
            is_valid = False
        
        if len(survey['language']) == 0:
            flash('Must choose a Favorite language')
            is_valid = False
        
        return is_valid
