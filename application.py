from flask import Flask, render_template, request
from transformers import pipeline
nlp = pipeline("question-answering")
application = Flask(__name__)


application.config['ENV'] = 'development'
application.config['DEBUG'] = True
application.config['TESTING'] = True

@application.route("/")
def home():
    return render_template('question.html')

@application.route("/querry", methods=['POST'])
def querry():
    with open('static/preg.txt') as f:
        covid = f.readlines() 

    context = ' '.join(covid)
    
    #render_template('question.html')
    r = request.form.to_dict()
    question = r['question']
    result = nlp(question=question, context=context)
    ans = f"Answer: '{result['answer']}'"
    #print(f"Answer: '{result['answer']}'") 
    print(question)
    return render_template('answer.html', ans=ans)

if __name__ == "__main__":
    application.run(debug=True)