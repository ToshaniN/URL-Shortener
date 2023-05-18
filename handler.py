from flask import render_template
from database import mapped_urls, session
from sqlalchemy import func

class Handler:
    def home():
        return render_template('url-shortener-template.html')


    def getShortURL(longURL):
        findURL = session.query(mapped_urls).filter(mapped_urls.long_URLs==longURL).first()
        if (not findURL):
            #Add in a new token and it's mapped long url to the database
            new_url = mapped_urls(long_URLs=longURL)
            session.add(new_url)
            session.commit()
            #Find what token value is
            last_token = session.query(func.max(mapped_urls.Token)).first()
            #Format the short url before sending response
            shortURL = 'https://urlshortener.com/Token' + str(last_token[0])
        else:
            #Long url was found in table, so format response for already existing short url
            shortURL = 'https://urlshortener.com/Token' + str(findURL.Token)
        response = {'returned shortURL' : shortURL}
        return response


    def getLongURL(shortURL):
        #Get short url from input and save token value
        token = int(shortURL[30:])
        #Find longurl using token value and form respond accordingly
        findURL = session.query(mapped_urls).filter(mapped_urls.Token==token).first()
        if (not findURL):
            returnedURL = "This short URL does not exist"
        else:
            returnedURL = findURL.long_URLs
        response = {'returned longURL' : returnedURL}
        return response