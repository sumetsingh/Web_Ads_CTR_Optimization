from flask import Flask, render_template
import pickle
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def index():
    # Load the variables from a file
    with open("UCB_data.pickle", "rb") as f:
        data = pickle.load(f)

    dataset = data["dataset"]
    ads_selected = data["ads_selected"]
    true_clicks = data["true_clicks"]
    best_ad = data["best_ad"]

    #  Visualising the results --- Histogram of ads selected
    plt.figure(figsize = (7,5))
    plt.bar(x=dataset.columns, height=10)
    plt.hist(ads_selected)
    plt.title('Histogram of ads selections')
    plt.xlabel('Ads')
    plt.ylabel('Number of times each ad was selected')
    plt.xticks(horizontalalignment='center', fontsize='9', color='black')
    plt.yticks(fontsize='9', color='black')
    plt.tight_layout()
    plt.savefig('static/ads_selection.png')
    
    #  Visualising the results --- True Clicks on Ads
    plt.figure(figsize = (7,5))
    plt.bar(x=dataset.columns, height=true_clicks)
    plt.title('True Clicks on Ads\n')
    plt.xlabel('\nAds', color='black')
    plt.ylabel('Clicks\n', color='black')
    plt.xticks(horizontalalignment='center', fontsize='9', color='black')
    plt.yticks(fontsize='9', color='black')
    plt.tight_layout()
    plt.savefig('static/true_clicks.png')

    return render_template('index.html', bestad=best_ad)
    

if __name__ == '__main__':
    app.run(debug=True)