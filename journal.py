# clean_journals.py
import pandas as pd

def clean_journal_data():
    # Journal data
    journals = pd.read_csv('journal.csv')
    journals['JournalName'] = journals['Journal Name'].str.strip().str.lower()
    journals['Publisher'] = journals['Journal Publisher'].fillna('unknown')
    
    # Paper-Journal relationships
    paper_journals = pd.read_csv('paper_journal.csv')
    # Use actual column name with underscore
    paper_journals['JournalName'] = paper_journals['Journal_Name'].str.strip().str.lower()
    
    # Add citation counts from papers
    papers = pd.read_csv('paper.csv')
    # Use exact column name from paper.csv
    paper_stats = papers.groupby('Paper ID')['Paper Citation Count'].first().reset_index()
    
    paper_journals = paper_journals.merge(
        paper_stats, 
        left_on='Paper ID', 
        right_on='Paper ID',
        how='left'
    ).fillna(0)
    
    # Save cleaned data
    journals.to_csv('cleaned/journals_enhanced.csv', index=False)
    paper_journals.to_csv('cleaned/paper_journals_enhanced.csv', index=False)

if __name__ == "__main__":
    clean_journal_data()