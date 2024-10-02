from flask import Flask, redirect, request

contents = {
    1: {
        "text":
        "Here is my first blog entry. It's pretty exciting stuff, isn't it? I hope you enjoyed the Scriber Experience so far! I know I am!",
        "date": "May 16, 2024"
    },
    2: {
        "text":
        "Here is my second blog entry. It's pretty exciting stuff, isn't it? I hope you enjoyed the Scriber Experience so far! I know I am!",
        "date": "May 16, 2024"
    },
    3: {
        "text":
        "Sunday Funday | Sun Up. Patience. Equivalence classes. Directed paths.",
        "date": "May 19, 2024"
    },
    4: {
        "text": "Quotient spaces. Still can't figure out how to get the theme to change when I click the button.",
        "date": "May 23, 2024"
    },
    5: {
        "text": "Streaming at Katnip's house. Still can't get the button to work. I'm so excited! /s.", 
        "date": "May 27, 2024"
    },
   6: {
        "text": "May just give up trying to get the button to work. I at least would like to move my contents to a database. But I don't even entirely know what a json file is, so maybe I should wait to do that for a future project.", "date": "June 2, 2024"
   }
}



app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=["GET", "POST"])
def index():
    theme = str(request.args.get('theme', default='space'))

    if theme == 'space' or theme == 'wisp':
        f = open("templates/index.html", "r")
        page = f.read()
        page = page.replace("{theme}", theme)
        f.close()
        return page

    else:
        f = open("templates/index.html", "r")
        page = f.read()
        page = page.replace("{theme}", "space")
        f.close()
        return page

# Automate generating webpage for a specific page number using URL parameter
@app.route('/blog', methods=["GET", "POST"])
def blog_entry():
    page_number = int(request.args.get(
        'page', default=1))  # Get the page number from the URL parameter
    
    if page_number in contents:

        entry = str(page_number)
        date = contents[page_number]["date"]
        text = contents[page_number]["text"]

        myName = "Captain"
        myimage = "static/images/logo.png"

        theme = str(request.args.get(
            'theme', default='space'))

        f = open("templates/page.html", "r")
        page = f.read()
        page = (page.replace("{entry}", entry)
              .replace("{date}", date)
              .replace("{text}", text)
              .replace("{name}", myName)
              .replace("{image}", myimage)
              .replace("{theme}", theme))
        f.close()

        return page

    else:
        f = open("templates/error.html", "r")
        page = f.read()
        f.close()
        return page


@app.route('/<int:page>')
def redirect_blog(page):
    return redirect(f'/blog?page={page}&theme=space')

@app.route('/<theme>')
def redirect_index_theme(theme):
    return redirect(f'/?theme={theme}')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)

