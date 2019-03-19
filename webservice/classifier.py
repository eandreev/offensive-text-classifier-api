class ClassifyMessage:
    def __init__(self, model, vectorizer, threshold):
        self.model = model
        self.vectorizer = vectorizer
        self.threshold = threshold
    
    def classify(self, message_text):
        sample = self.vectorizer.transform([message_text])
        return self.model.predict(sample)[0] >= self.threshold
