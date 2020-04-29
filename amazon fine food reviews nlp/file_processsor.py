import pandas as pd

def shorten_file():
    read_file = pd.read_csv('Reviews.csv').head(5000);
    print('read file')
    read_file.to_csv('shortReviews.csv', ',', encoding = 'utf-8')
    print('done')

if __name__ == "__main__":
    shorten_file()
        