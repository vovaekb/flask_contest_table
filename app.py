from flask import Flask, render_template, request
import json
import pandas as pd

app = Flask(__name__)

@app.route('/contest_table')
def contest_table():
    table_file = 'contest_scores.csv'
    contest_scores_data = pd.read_csv(table_file, header=0)
    contest_scores_data = contest_scores_data.sort_values(by='score', ascending=False) 
    contest_scores_data = contest_scores_data.astype({"id": int, "score": float, "real_score": float})
    
    contest_scores = list(contest_scores_data.values)
    return render_template('contest_scores.html', contest_scores=contest_scores) 

@app.route('/score', methods=['GET', 'POST'])
def put_score():
    if request.method == 'POST':
        # save score
        table_file = 'contest_scores.csv'
        content = request.get_json()
        df = pd.io.json.json_normalize(content) 

        with open(table_file, 'a') as f:
            df.to_csv(f, header=False, index=False)
        return 'Success', 200 

    return 'Update score'


if __name__ == '__main__':
    app.run()
