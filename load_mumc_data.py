from sklearn import datasets

DATA_PATH = 'diabetes.csv'

df = datasets.load_diabetes(as_frame=True)
df.to_csv(DATA_PATH)
