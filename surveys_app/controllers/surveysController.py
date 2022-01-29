from flask import Flask, render_template, request, redirect, session
from surveys_app import app
from surveys_app.models import dojoModel, languageModel, surveyModel

@app.errorhandler(404)
def page_not_found(error):
    app.logger.error(error)
    return render_template('404.html'), 404

@app.route('/', methods=['GET'])
def index():
    if 'survey' in session:
        session.pop('survey')

    dojos = dojoModel.Dojo.get_all()
    languages = languageModel.Language.get_all()

    return render_template("survey.html", dojos=dojos, languages=languages)

@app.route('/create_survey', methods=['POST'])
def create_survey():

    if not surveyModel.Survey.validateSurvey(request.form):
        return redirect('/')

    data = {
        'name': request.form.get('name'),
        'dojoId': request.form.get('dojo'),
        'languageId': request.form.get('language'),
        'comment': request.form.get('comment')
    }

    result = surveyModel.Survey.save(data)
    
    if result:
        savedSurvey = {'surveyId': result}
        survey = surveyModel.Survey.get_survey_dojo_language_by_id(savedSurvey)

        flatSurvey = {
            'name': survey.name,
            'dojo': survey.dojo.name,
            'language': survey.language.name,
            'comment': survey.comment
        }

        session['survey'] = flatSurvey
        return redirect('/result')
    else:
        return redirect('/')

@app.route('/result', methods=['GET'])
def result():
    if not 'survey' in session:
        return redirect('/')
    else:
        survey = session['survey']
        return render_template('result.html', survey = survey)