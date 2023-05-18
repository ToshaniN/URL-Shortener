from flask import request, render_template
from database import db, mapped_urls
from sqlalchemy import func

class Resource:
    def home():
        return render_template('url-shortener-template.html')


    def get():
        longURL = request.args.get('longURL')
        findURL = db.session.query(mapped_urls).filter(mapped_urls.long_URLs==longURL).first()
        if (not findURL):
            #Add in a new token and it's mapped long url to the database
            new_url = mapped_urls(long_URLs=longURL)
            db.session.add(new_url)
            db.session.commit()
            #Find what token value is
            last_token = db.session.query(func.max(mapped_urls.Token)).first()
            #Format the short url before sending response
            shortURL = 'https://urlshortener.com/Token' + str(last_token[0])
        else:
            #Long url was found in table, so format response for already existing short url
            shortURL = 'https://urlshortener.com/Token' + str(findURL.Token)
        #Send response
        response = {'longURL' :  longURL ,
                    'returned shortURL' : shortURL}
        return response

    def post():
        #Get short url from input and save token value
        receivedShortURL = request.get_json()
        shortURL = receivedShortURL["shortURL"]
        token = int(shortURL[30:])
        #Find longurl using token value and form respond accordingly
        findURL = db.session.query(mapped_urls).filter(mapped_urls.Token==token).first()
        if (not findURL):
            returnedURL = "short url does not exist"
        else:
            returnedURL = findURL.long_URLs
        #Send respond
        response = {'shortURL' :  shortURL ,
                    'returned longURL' : returnedURL}
        return response