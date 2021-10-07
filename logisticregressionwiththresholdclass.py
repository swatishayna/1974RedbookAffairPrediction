from sklearn.linear_model import LogisticRegression
import pickle


# it seems like model works good with 85percent precision howsoever recall is extreamely low. 
class LogisticRegressionwithThreshold(LogisticRegression):
    def __init__(self,penalty,solver):
        super(LogisticRegressionwithThreshold,self).__init__()
        self.penalty =penalty
        self.solver =solver
        
    def predict(self, X, threshold =None):
        if threshold==None:
            return LogisticRegression.predict(self,X)
        else:
            y_scores = LogisticRegression.predict_proba(self, X)[:, 1]
            y_pred_with_threshold = (y_scores >= 0.8577829621936014).astype(int)
            return y_pred_with_threshold
    def output(self, input):
            model = pickle.load(open('affair_predict.pickle', 'rb'))
            
            return model.predict(input)





