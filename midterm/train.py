import pandas as pd
import pickle

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import DictVectorizer

from common import config

def get_dataset(path = './dataset.csv', config = config):
    df = pd.read_csv(path, na_values=config['missing_values'])
    header = df.columns.str.lower()
    for k,v in config['replacements'].items(): header = header.str.replace(k, v)  
    df.columns = header

    for col in config['drop_columns']: df.drop(col, axis=1, inplace=True, errors='ignore')
    df.hazardous = df.hazardous.astype('int')
    return df

def build_model(df, config=config):
    df_full_train, _ = train_test_split(df, test_size=0.2, random_state=config['seed'])
    df_train, _ = train_test_split(df_full_train, test_size=0.25, random_state=config['seed'])

    df_train = df_train.reset_index(drop=True)
    y_train = df_train.hazardous.values

    del df_train['hazardous']
    vectorizer = DictVectorizer(sparse=False)
    X_train = vectorizer.fit_transform(df_train.to_dict(orient='records'))
    
    model = RandomForestClassifier(n_estimators=70, max_depth=11, min_samples_leaf=1, random_state=config['seed'], n_jobs=-1)
    model.fit(X_train, y_train)

    return vectorizer, model

def save_model(vectorizer, model, vectorizer_file_name = config['vectorizer_file_name'], model_file_name = config['model_file_name']):
    with open(vectorizer_file_name, 'wb') as f_out:
        pickle.dump(vectorizer, f_out)
    with open(model_file_name, 'wb') as f_out:
        pickle.dump(model, f_out)


df = get_dataset()
vectorizer, model = build_model(df)
save_model(vectorizer, model)