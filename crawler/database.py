class DataBase:
    allTokens = dict()
    scraped = set()  # set of urls we've extracted from or are blacklisted
    seen = set()
    unique_urls = set()


    def __init__(self):
        self.allTokens = dict()
        self.scraped = set()
        self.seen = set()
        self.unique_urls = set()

    def printList():
        f = open("URLS.txt", "a")

        for word in d.scraped:
            f.write(word + "\n")

        f.write("\n\n\n\nUNIQUE URLS")

        for word in d.unique_urls:
            f.write(word + "\n")

        f.close()