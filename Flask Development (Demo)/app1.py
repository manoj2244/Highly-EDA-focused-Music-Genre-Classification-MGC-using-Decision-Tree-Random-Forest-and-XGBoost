
def obtained_music(X_new):



    import pickle

    # Load the trained model from the file
    with open("model1.pkl", "rb") as f:
        clf = pickle.load(f)

    

    prediction = clf.predict(X_new)
    return prediction