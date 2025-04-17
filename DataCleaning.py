import pandas as pd

def remove_whitespace(df):
    df.columns = [col.replace(" ", "") for col in df.columns]
    return df

def clean_author_csv(filepath):
    df = pd.read_csv(filepath)
    df = remove_whitespace(df)
    df.drop_duplicates(inplace=True)
    df.dropna(subset=['AuthorID'], inplace=True)
    df.to_csv(filepath, index=False)

def clean_author_paper_csv(filepath):
    df = pd.read_csv(filepath)
    df = remove_whitespace(df)
    df.drop_duplicates(inplace=True)
    df.dropna(subset=['AuthorID', 'PaperID'], inplace=True)
    df.to_csv(filepath, index=False)

def clean_journal_csv(filepath):
    df = pd.read_csv(filepath)
    df = remove_whitespace(df)
    df.drop_duplicates(inplace=True)
    df.dropna(subset=['JournalName', 'JournalPublisher'], inplace=True)
    df.to_csv(filepath, index=False)

def clean_paper_journal_csv(filepath):
    df = pd.read_csv(filepath)
    df = remove_whitespace(df)
    df.drop_duplicates(inplace=True)
    df.dropna(subset=['PaperID', 'JournalName'], inplace=True)
    df.to_csv(filepath, index=False)

def clean_paper_reference_csv(filepath):
    df = pd.read_csv(filepath)
    df = remove_whitespace(df)
    df.drop_duplicates(inplace=True)
    df.dropna(subset=['PaperID', 'ReferencedPaperID'], inplace=True)
    df.to_csv(filepath, index=False)

def clean_paper_topic_csv(filepath):
    df = pd.read_csv(filepath)
    df = remove_whitespace(df)
    df.drop_duplicates(inplace=True)
    df.dropna(subset=['PaperID', 'TopicID'], inplace=True)
    df.to_csv(filepath, index=False)

def clean_paper_csv(filepath):
    df = pd.read_csv(filepath)
    df = remove_whitespace(df)
    df.drop_duplicates(inplace=True)
    df.dropna(subset=['PaperID'], inplace=True)
    df.to_csv(filepath, index=False)

def clean_topic_csv(filepath):
    df = pd.read_csv(filepath)
    df = remove_whitespace(df)
    df.drop_duplicates(inplace=True)
    df.dropna(subset=['TopicID'], inplace=True)
    df.to_csv(filepath, index=False)

if __name__ == "__main__":
    clean_author_csv('author.csv')
    clean_author_paper_csv('author_paper.csv')
    clean_journal_csv('journal.csv')
    clean_paper_journal_csv('paper_journal.csv')
    clean_paper_reference_csv('paper_reference.csv')
    clean_paper_topic_csv('paper_topic.csv')
    clean_paper_csv('paper.csv')
    clean_topic_csv('topic.csv')